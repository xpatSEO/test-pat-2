#!/usr/bin/env python3
"""
Script de génération du JSON masonry-blocks pour les 25 villes.

Lit le fichier articles_export_25.csv et le JSON template de Rouen,
puis génère un fichier JSON unique contenant les données masonry
mises à jour pour chaque ville, et remplace toutes les références
à la ville template (Rouen) dans les contenus textuels.
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

# Ville utilisée dans le template d'origine
TEMPLATE_CITY = "Rouen"

# Clés ACF des champs masonry (field references extraites du template)
FIELD_MASONRY_TITLE = "field_67b702fe6ea62"
FIELD_MASONRY_TXT = "field_67b703206ea63"
FIELD_MASONRY_ARTICLES = "field_67b70368a75ac"
FIELD_MASONRY_BLOCK_TITLE = "field_67b705152d6db"
FIELD_MASONRY_BLOCK_SUBTITLE = "field_67b7052d2d6dc"

# Champs textuels à modifier par bloc Gutenberg (cf. CHAMPS_A_MODIFIER.md)
# Format : { "nom-du-bloc": [liste de clés data à traiter] }
BLOCK_FIELDS_TO_REPLACE = {
    "header-breadcrumb": [
        "kb_header_title",
        "kb_header_desc",
    ],
    "intro-image": [
        "kb_intro_image_title",
        "kb_intro_image_description",
    ],
    "horaire-block": [
        "kb_horaire_title",
        "kb_horaire_city",
    ],
    "faq-post-new": [
        # Les réponses FAQ seront traitées dynamiquement (toutes les clés *_answer)
    ],
}

# Le bloc avantages-style2 a un bug : mentionne "Paris" au lieu de "Rouen"
AVANTAGES_FIELDS = ["kb_avantages_style2_subtitle"]

# Champs post_meta à mettre à jour
META_FIELDS_TO_REPLACE = [
    "title",
    "_yoast_wpseo_metadesc",
    "_yoast_wpseo_title",
]


def format_city_name(ville: str) -> str:
    """Capitalisation correcte des noms de villes françaises.

    Gère les articles/prépositions en position intermédiaire :
    'aix-en-provence' → 'Aix-en-Provence'
    'noisy-le-grand'  → 'Noisy-le-Grand'
    'la-rochelle'     → 'La-Rochelle'
    """
    small_words = {
        "en", "le", "la", "les", "de", "du", "des",
        "sur", "sous", "lès", "lez",
    }
    parts = ville.split("-")
    result = []
    for i, part in enumerate(parts):
        if i > 0 and part.lower() in small_words:
            result.append(part.lower())
        else:
            result.append(part.capitalize())
    return "-".join(result)


# ---------------------------------------------------------------------------
# Remplacement des références ville dans les blocs Gutenberg du post_content
# ---------------------------------------------------------------------------

def _process_single_block(block_str: str, ville: str) -> str:
    """Remplace les références à la ville template dans un bloc Gutenberg."""
    # Extraire le nom du bloc
    name_match = re.match(r"<!-- wp:acf/([\w-]+) ", block_str)
    if not name_match:
        return block_str
    block_name = name_match.group(1)

    # Extraire le JSON imbriqué
    json_start = block_str.index("{")
    json_end = block_str.rindex("}") + 1
    json_str = block_str[json_start:json_end]

    try:
        block_obj = json.loads(json_str)
    except json.JSONDecodeError:
        return block_str

    data = block_obj.get("data", {})
    if not isinstance(data, dict):
        return block_str

    modified = False

    # --- Bloc avantages-style2 : corriger le bug "Paris" ---
    if block_name == "avantages-style2":
        for field in AVANTAGES_FIELDS:
            if field in data and isinstance(data[field], str):
                new_val = data[field].replace("Paris", ville).replace(TEMPLATE_CITY, ville)
                if new_val != data[field]:
                    data[field] = new_val
                    modified = True

    # --- Blocs avec liste de champs explicite ---
    elif block_name in BLOCK_FIELDS_TO_REPLACE:
        fields = BLOCK_FIELDS_TO_REPLACE[block_name]
        for field in fields:
            if field in data and isinstance(data[field], str):
                new_val = data[field].replace(TEMPLATE_CITY, ville)
                if new_val != data[field]:
                    data[field] = new_val
                    modified = True

    # --- Bloc FAQ : traiter dynamiquement toutes les clés *_answer ---
    if block_name == "faq-post-new":
        for key in list(data.keys()):
            if "kb_faq" in key and "answer" in key and isinstance(data[key], str):
                new_val = data[key].replace(TEMPLATE_CITY, ville)
                if new_val != data[key]:
                    data[key] = new_val
                    modified = True

    if modified:
        block_obj["data"] = data
        new_json = json.dumps(block_obj, ensure_ascii=False)
        return f"<!-- wp:acf/{block_name} {new_json} /-->"

    return block_str


def replace_city_in_content(content: str, ville: str) -> str:
    """Parcourt tous les blocs Gutenberg du post_content et remplace
    les références à la ville template par la ville cible."""
    result = []
    i = 0
    while i < len(content):
        block_start = content.find("<!-- wp:acf/", i)
        if block_start == -1:
            result.append(content[i:])
            break
        # Texte entre les blocs
        result.append(content[i:block_start])
        # Trouver la fin du bloc
        block_end = content.find(" /-->", block_start)
        if block_end == -1:
            result.append(content[block_start:])
            break
        block_end += len(" /-->")
        block_str = content[block_start:block_end]
        # Traiter le bloc
        result.append(_process_single_block(block_str, ville))
        i = block_end
    return "".join(result)


def replace_city_in_meta(meta: dict, ville: str) -> None:
    """Remplace les références à la ville template dans les champs post_meta."""
    for field in META_FIELDS_TO_REPLACE:
        if field in meta:
            val = meta[field]
            if isinstance(val, list):
                meta[field] = [
                    v.replace(TEMPLATE_CITY, ville) if isinstance(v, str) else v
                    for v in val
                ]
            elif isinstance(val, str):
                meta[field] = val.replace(TEMPLATE_CITY, ville)


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

        # Nom proprement formaté de la ville
        ville_formatted = format_city_name(ville)

        # Mettre à jour les identifiants de la ville
        page["post_data"]["post_title"] = f"Cabinet {ville_formatted}"
        page["post_data"]["post_name"] = f"cabinet-{ville.lower()}"

        # Construire les données masonry
        masonry_data = build_masonry_data(row)
        masonry_comment = build_masonry_block_comment(masonry_data)

        # Mettre à jour le post_content (masonry)
        page["post_data"]["post_content"] = update_post_content(
            page["post_data"]["post_content"],
            masonry_comment,
        )

        # Remplacer toutes les références à la ville template dans le contenu
        page["post_data"]["post_content"] = replace_city_in_content(
            page["post_data"]["post_content"],
            ville_formatted,
        )

        # Remplacer les références ville dans les post_meta (title, Yoast SEO…)
        replace_city_in_meta(page["post_meta"], ville_formatted)

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
