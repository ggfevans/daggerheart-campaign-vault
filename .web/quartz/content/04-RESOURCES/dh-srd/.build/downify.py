import os
import re
import json
import shutil
from jinja2 import Template
from titlecase import titlecase
from urllib.parse import quote


def clear_output_dir(output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)


def ensure_symlink(target, link_name):
    # Remove existing symlink or file
    if os.path.islink(link_name) or os.path.exists(link_name):
        os.remove(link_name)
    os.symlink(target, link_name)
    print(f"Linked {link_name} → {target}")


def url_encode(value):
    if not isinstance(value, str):
        value = str(value)
    return quote(value, safe="")


def safe_filename(name):
    return titlecase(re.sub(r"[^\w\-_ ]", "", name.strip()))


def find_matching_jobs(json_dir="json", md_dir="md"):
    jobs = []
    json_files = {
        os.path.splitext(f)[0]: os.path.join(json_dir, f)
        for f in os.listdir(json_dir)
        if f.endswith(".json")
    }
    md_files = {
        os.path.splitext(f)[0]: os.path.join(md_dir, f)
        for f in os.listdir(md_dir)
        if f.endswith(".md")
    }
    for table in sorted(json_files):
        if table in md_files:
            jobs.append((json_files[table], md_files[table], table))
    return jobs


def process_json_to_md(json_file, template_file, output_dir, feature_count=7):
    with open(template_file, encoding="utf-8-sig") as f:
        template = Template(f.read())
    with open(json_file, encoding="utf-8-sig") as jf:
        data = json.load(jf)
        for row in data:
            content = template.render(**row, url_encode=url_encode)
            content = content.strip() + "\n"
            filename = safe_filename(row["name"])  # assuming JSON keys are lower
            outpath = f"{output_dir}/{filename}.md"
            with open(outpath, "w", encoding="utf-8-sig") as outfile:
                outfile.write(content)
                print(outpath)


if __name__ == "__main__":
    jobs = find_matching_jobs()
    for json_file, template_file, table in jobs:
        output_dir = f"../{table}"
        clear_output_dir(output_dir)
        os.makedirs(output_dir, exist_ok=True)
        process_json_to_md(json_file, template_file, output_dir)
        link_name = f"docs/{table}"
        output_dir = f"../{output_dir}"
        ensure_symlink(output_dir, link_name)
