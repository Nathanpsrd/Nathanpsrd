import re
import argparse

README_FILE = "./README.md"
TOC_START = "<!-- TOC START -->"
TOC_END = "<!-- TOC END -->"

def slugify(text):
    text = text.strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)  # enlever les signes de ponctuation
    return re.sub(r'\s+', '-', text)

def extract_headings(lines, max_level):
    in_code_block = False
    headings = []
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = re.match(r'^(#{2,6})\s+(.*)', line)
        if match:
            level = len(match.group(1)) - 1  # 2 # => niveau 1, 3# => niveau 2, etc.
            if level <= max_level:
                title = match.group(2).strip()
                anchor = slugify(title)
                headings.append((level, title, anchor))
    return headings

def build_toc(headings):
    toc = []
    for level, title, anchor in headings:
        indent = "  " * (level - 1)
        toc.append(f"{indent}- [{title}](#{anchor})")
    return toc

def update_readme(max_level):
    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    headings = extract_headings(lines, max_level)
    toc = build_toc(headings)
    toc_block = [TOC_START + "\n"] + [line + "\n" for line in toc] + [TOC_END + "\n"]

    try:
        start = lines.index(TOC_START + "\n")
        end = lines.index(TOC_END + "\n") + 1
        lines = lines[:start] + toc_block + lines[end:]
    except ValueError:
        lines = toc_block + ["\n"] + lines

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Table des matières mise à jour dans {README_FILE} (niveaux jusqu'à {max_level})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère un sommaire cliquable pour README.md")
    parser.add_argument("-m", "--max-level", type=int, default=3,
                        help="Niveau maximal de titres à inclure (par défaut 3 pour ## à ####)")
    args = parser.parse_args()
    update_readme(args.max_level)

## scripts/generate_toc.py

### Usage

###```bash
### python generate_toc.py           # max_level=3 par défaut (##, ###, ####)
### python generate_toc.py -m 2      # Pour n’avoir que ## et ###
### python generate_toc.py -m 4      # Pour n’avoir que ##, ###, #### et #####
###```