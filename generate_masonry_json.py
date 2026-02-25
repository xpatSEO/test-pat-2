#!/usr/bin/env python3
"""
Script de génération du JSON masonry-blocks pour les 25 villes.

Lit le fichier articles_export_25.csv et le JSON template de Rouen,
puis génère un fichier JSON unique contenant les données masonry
mises à jour pour chaque ville.
"""

import csv
import json
import re
import copy
import sys
from pathlib import Path

# --- Configuration ---
BASE_DIR = Path(__file__).parent
CSV_INPUT = BASE_DIR / "articles_export_25.csv"
JSON_TEMPLATE = BASE_DIR / "page_ID_3866_data_test-2.json"
JSON_OUTPUT = BASE_DIR / "pages_25_villes_masonry.json"

# Clés ACF des champs masonry (field references extraites du template)
FIELD_MASONRY_TITLE = "field_67b702fe6ea62"
FIELD_MASONRY_TXT = "field_67b703206ea63"
FIELD_MASONRY_ARTICLES = "field_67b70368a75ac"
FIELD_MASONRY_BLOCK_TITLE = "field_67b705152d6db"
FIELD_MASONRY_BLOCK_SUBTITLE = "field_67b7052d2d6dc"


def read_csv(path: Path) -> list[dict]:
    """Lit le CSV séparateur ; et retourne une liste de dicts par ville."""
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows


def build_masonry_data(row: dict) -> dict:
    """Construit l'objet data du bloc masonry-blocks à partir d'une ligne CSV."""
    data = {
        "kb_masonry_title": "",
        "_kb_masonry_title": FIELD_MASONRY_BLOCK_TITLE,
        "kb_masonry_subtitle": "",
        "_kb_masonry_subtitle": FIELD_MASONRY_BLOCK_SUBTITLE,
    }

    articles_count = 0
    for i in range(3):
        title_key = f"kb_masonry_articles_{i}_kb_masonry_title"
        txt_key = f"kb_masonry_articles_{i}_kb_masonry_txt"

        title = row.get(title_key, "").strip()
        txt = row.get(txt_key, "").strip()

        if title or txt:
            data[title_key] = title
            data[f"_{title_key}"] = FIELD_MASONRY_TITLE
            data[txt_key] = txt
            data[f"_{txt_key}"] = FIELD_MASONRY_TXT
            articles_count += 1

    data["kb_masonry_articles"] = articles_count
    data["_kb_masonry_articles"] = FIELD_MASONRY_ARTICLES

    return data


def build_masonry_block_comment(data: dict) -> str:
    """Génère le commentaire Gutenberg <!-- wp:acf/masonry-blocks ... -->."""
    block = {
        "name": "acf/masonry-blocks",
        "data": data,
        "mode": "edit",
    }
    json_str = json.dumps(block, ensure_ascii=False)
    return f"<!-- wp:acf/masonry-blocks {json_str} /-->"


def update_post_content(original_content: str, new_masonry_comment: str) -> str:
    """Remplace le bloc masonry-blocks dans le post_content existant."""
    pattern = r"<!-- wp:acf/masonry-blocks \{.*?\} /-->"
    match = re.search(pattern, original_content, re.DOTALL)
    if match:
        return original_content[:match.start()] + new_masonry_comment + original_content[match.end():]
    else:
        # Si pas de bloc masonry existant, on l'ajoute à la fin
        return original_content + "\n\n" + new_masonry_comment


def main():
    # Charger le template JSON (Rouen)
    with open(JSON_TEMPLATE, encoding="utf-8") as f:
        template_list = json.load(f)

    template = template_list[0]

    # Charger le CSV
    rows = read_csv(CSV_INPUT)
    print(f"Villes trouvées dans le CSV : {len(rows)}")

    results = []

    for row in rows:
        ville = row.get("ville", "").strip()
        if not ville:
            continue

        # Copier le template
        page = copy.deepcopy(template)

        # Mettre à jour les identifiants de la ville
        page["post_data"]["post_title"] = f"Cabinet {ville.title()}"
        page["post_data"]["post_name"] = f"cabinet-{ville.lower()}"

        # Construire les données masonry
        masonry_data = build_masonry_data(row)
        masonry_comment = build_masonry_block_comment(masonry_data)

        # Mettre à jour le post_content
        page["post_data"]["post_content"] = update_post_content(
            page["post_data"]["post_content"],
            masonry_comment,
        )

        # Ajouter un champ ville pour faciliter l'identification
        page["ville"] = ville

        results.append(page)
        print(f"  ✓ {ville} — {masonry_data['kb_masonry_articles']} articles masonry")

    # Écrire le JSON de sortie
    with open(JSON_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nFichier généré : {JSON_OUTPUT}")
    print(f"Total : {len(results)} villes traitées")


if __name__ == "__main__":
    main()
