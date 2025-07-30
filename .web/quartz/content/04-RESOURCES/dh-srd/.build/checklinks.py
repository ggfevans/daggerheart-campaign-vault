import os
import re
from pathlib import Path
from urllib.parse import unquote


def find_md_links(md_text):
    # Find [text](link), skip images/external links
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\((?!http[s]?://|mailto:)([^)]+)\)")
    return pattern.findall(md_text)


def path_exists_case_sensitive(path: Path):
    """Returns True only if the file/folder exists with exact casing."""
    # Start at the filesystem root or relative root
    parts = path.parts
    if not parts:
        return False
    # Start traversal
    check_path = Path(parts[0])
    for part in parts[1:]:
        try:
            entries = os.listdir(check_path)
        except Exception:
            return False
        # Use exact match for this level
        match = next((e for e in entries if e == part), None)
        if not match:
            return False
        check_path = check_path / part
    return check_path.exists()


def check_links(base_path):
    for md_file in Path(base_path).rglob("*.md"):
        with md_file.open(encoding="utf-8") as f:
            content = f.read()
        links = find_md_links(content)
        for link in links:
            # Remove anchor and query
            clean_link = link.split("#")[0].split("?")[0].strip()
            if not clean_link:
                continue
            decoded_link = unquote(clean_link)
            # The link may contain ../ or ./ -- resolve it relative to the md_file's location
            rel_target = md_file.parent / decoded_link
            abs_target = rel_target.resolve()
            # Get the path components as they appear in the *relative* link
            # Build a version from base_path to abs_target using the real on-disk names
            try:
                # This handles links that point outside the base_path (ignore them)
                abs_target.relative_to(base_path)
            except ValueError:
                continue
            # Now, build a path from base_path using the actual spelling in each directory
            relative_parts = abs_target.relative_to(base_path).parts
            cursor = Path(base_path)
            real_path = Path(base_path)
            for part in relative_parts:
                try:
                    entries = os.listdir(cursor)
                except Exception:
                    real_path = None
                    break
                matches = [e for e in entries if e == part]
                if matches:
                    real_path = real_path / part
                    cursor = cursor / part
                else:
                    real_path = None
                    break
            if not real_path or not real_path.exists():
                print(
                    f"Missing (or wrong case): {link} (referenced in {md_file.relative_to(base_path)})"
                )


if __name__ == "__main__":
    check_links(Path("..").resolve())
