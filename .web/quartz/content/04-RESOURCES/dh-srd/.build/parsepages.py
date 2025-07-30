import os
import re
import base64
import json
import fitz  # PyMuPDF
import mdformat
from collections import Counter, defaultdict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# --- Prompt Templates ---
SYSTEM_PROMPT = {
    "role": "system",
    "content": """
You are an OCR+Markdown assistant.

Strictly preserve heading levels (# through ######), paragraph spacing, bold/italic formatting, and tables.

Do NOT omit sparse content. Titles, subtitles, and author credits should all be represented.

Do NOT include page numbers, decorative symbols, or artifacts.

Do not use soft line breaks within paragraphs - instead, each paragraph and heading must be fully separated by two newlines.

Do NOT preserve formatting used for visual alignment or spacing.

⚠️ If this page is a Table of Contents:
- Remove all decorative dot leaders (e.g. “. . . . .”) and page numbers (e.g. “...12”).
- Extract only the clean section titles as bullet points or headings.
""",
}

PROMPT_TEMPLATE = """
You are continuing a Markdown document from a prior page. Preserve structural consistency.

This is page {page_number}. The top of this page may continue a previously started section — do not restart heading levels unless visually clear.

Extract all text — even if the page contains only a title, subtitle, author credits, or sparse content.
"""

# --- Utilities ---


def extract_heading_hierarchy(md):
    """
    Extract headings from markdown, return as a list of dicts.
    """
    headings = []
    for line in md.splitlines():
        if match := re.match(r"^(#{1,6}) (.+?)$", line.strip()):
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append({"level": level, "title": title})
    return headings


def extract_plain_hierarchy(headings):
    """Return list of plain markdown headings, in document order, no styles."""
    return [f"{'#' * h['level']} {h['title']}" for h in headings]


def extract_current_lineage(headings):
    """Return the current stack of headings, as plain markdown, no styles."""
    stack = {}
    for h in headings:
        level = h["level"]
        stack[level] = f"{'#' * level} {h['title']}"
        # Prune deeper levels
        stack = {k: v for k, v in stack.items() if k <= level}
    return [stack[k] for k in sorted(stack.keys())]


def write_heading_summary_file(headings, md_path):
    """
    Write all headings seen so far to a flat markdown file for hierarchy.md.
    """
    with open(md_path, "w", encoding="utf-8") as f:
        for h in headings:
            f.write(f"{'#' * h['level']} {h['title']}\n")


def pdf_page_to_image(pdf_path, page_num, zoom=2.0, image_dir=None):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    matrix = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=matrix)
    image_data = pix.pil_tobytes("png")
    if image_dir:
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, f"page_{page_num + 1:03}.png")
        pix.save(image_path)
        print(f"Saved image: {image_path}")
    doc.close()
    return image_data


def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")


def lint_markdown(md: str) -> str:
    md = md.replace("\\\n", "\n")
    return mdformat.text(md)


def image_to_markdown(
    encoded_image, page_number, previous_markdown=None, heading_context=None
):
    messages = [SYSTEM_PROMPT]

    if previous_markdown:
        messages.append(
            {
                "role": "user",
                "content": (
                    "Here is the markdown from the previous page:\n\n"
                    f"{previous_markdown.strip()}"
                ),
            }
        )

    if heading_context:
        hierarchy_plain = extract_plain_hierarchy(heading_context)
        lineage_plain = extract_current_lineage(heading_context)

        if hierarchy_plain:
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Hierarchy of markdown headings so far:\n\n"
                        + "\n".join(hierarchy_plain)
                    ),
                }
            )
        if lineage_plain:
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Current markdown heading lineage:\n\n"
                        + "\n".join(lineage_plain)
                    ),
                }
            )
        print(json.dumps(messages, indent=2))

    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": PROMPT_TEMPLATE.format(page_number=page_number),
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{encoded_image}"},
                },
            ],
        }
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.1,
        max_tokens=4096,
    )

    content = response.choices[0].message.content.strip()

    # Remove ``` wrappers if present
    if content.startswith("```"):
        lines = content.splitlines()
        lines = lines[1:] if lines[0].strip().startswith("```") else lines
        lines = lines[:-1] if lines and lines[-1].strip() == "```" else lines
        content = "\n".join(lines).strip()

    if "unable to extract text" in content.lower() or "another page" in content.lower():
        print(f"⚠️ GPT gave a generic refusal on page {page_number}.")
        os.exit(1)

    return content


def pdf_to_markdown_images(pdf_path, markdown_dir, image_dir):
    os.makedirs(markdown_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")

    previous_md = None
    cumulative_headings = []
    hierarchy_md_path = os.path.join(markdown_dir, "hierarchy.md")

    for page_num in range(total_pages):
        page_index = page_num + 1
        md_path = os.path.join(markdown_dir, f"page_{page_index:03}.md")
        img_path = os.path.join(image_dir, f"page_{page_index:03}.png")

        if os.path.exists(md_path):
            print(f"✓ Skipping GPT: {md_path} already exists")
            with open(md_path, "r", encoding="utf-8") as f:
                previous_md = f.read()
            cumulative_headings.extend(extract_heading_hierarchy(previous_md))
        else:
            if os.path.exists(img_path):
                print(f"✓ Using cached image: {img_path}")
                with open(img_path, "rb") as f:
                    img_bytes = f.read()
            else:
                print(f"🔄 Rendering image for page {page_index}...")
                img_bytes = pdf_page_to_image(pdf_path, page_num, image_dir=image_dir)

            encoded_img = encode_image(img_bytes)
            print(f"🧠 Sending page {page_index} to GPT-4o...")
            markdown = image_to_markdown(
                encoded_img,
                page_index,
                previous_markdown=previous_md,
                heading_context=cumulative_headings,
            )

            cleaned_markdown = lint_markdown(markdown)

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(cleaned_markdown)

            previous_md = cleaned_markdown
            cumulative_headings.extend(extract_heading_hierarchy(previous_md))
            print(f"💾 Saved markdown: {md_path}")

        write_heading_summary_file(cumulative_headings, hierarchy_md_path)

    print(f"📚 Final heading hierarchy saved: {hierarchy_md_path}")
    doc.close()


if __name__ == "__main__":
    pdf_path = "DH-SRD-May202025.pdf"
    markdown_dir = "../pages"
    image_dir = "../images"
    pdf_to_markdown_images(pdf_path, markdown_dir, image_dir)
