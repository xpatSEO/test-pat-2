#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 25 JSON files for different cities based on template
"""

import json
import random
import re

# List of cities with their post_name
CITIES = [
    ("Paris", "cabinet-paris"),
    ("Rouen", "cabinet-rouen"),
    ("Tours", "cabinet-tours"),
    ("Toulouse", "cabinet-toulouse"),
    ("Strasbourg", "cabinet-strasbourg"),
    ("Rennes", "cabinet-rennes"),
    ("Perpignan", "cabinet-perpignan"),
    ("Reims", "cabinet-reims"),
    ("Orléans", "cabinet-orleans"),
    ("Noisy-le-Grand", "cabinet-noisy-le-grand"),
    ("Nantes", "cabinet-nantes"),
    ("Nancy", "cabinet-nancy"),
    ("Montpellier", "cabinet-montpellier"),
    ("Marseille", "cabinet-marseille"),
    ("Laval", "cabinet-laval"),
    ("Lyon", "cabinet-lyon"),
    ("Lille", "cabinet-lille"),
    ("La Rochelle", "cabinet-la-rochelle"),
    ("Grenoble", "cabinet-grenoble"),
    ("Dijon", "cabinet-dijon"),
    ("Évreux", "cabinet-evreux"),
    ("Bordeaux", "cabinet-bordeaux"),
    ("Angers", "cabinet-angers"),
    ("Aix-en-Provence", "cabinet-aix-en-provence"),
    ("Agen", "cabinet-agen")
]

def load_template():
    """Load the template JSON file"""
    with open('page_ID_3866_data_test-2.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_articles():
    """Load articles from export file"""
    with open('articles-export-2026-02-18.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_html(html_content):
    """Clean HTML content and extract text"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html_content)
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&eacute;', 'é')
    text = text.replace('&egrave;', 'è')
    text = text.replace('&ecirc;', 'ê')
    text = text.replace('&agrave;', 'à')
    text = text.replace('&ccedil;', 'ç')
    text = text.replace('&ocirc;', 'ô')
    text = text.replace('&ucirc;', 'û')
    text = text.replace('&icirc;', 'î')
    text = text.replace('&acirc;', 'â')
    text = text.replace('&rsquo;', "'")
    text = text.replace('&lsquo;', "'")
    text = text.replace('&rdquo;', '"')
    text = text.replace('&ldquo;', '"')
    text = text.replace('&hellip;', '...')
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_paragraphs(text, num_paragraphs=3):
    """Split text into roughly equal paragraphs"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) < num_paragraphs:
        return [text]

    sentences_per_para = len(sentences) // num_paragraphs
    paragraphs = []

    for i in range(num_paragraphs):
        if i == num_paragraphs - 1:
            # Last paragraph gets remaining sentences
            para = ' '.join(sentences[i * sentences_per_para:])
        else:
            para = ' '.join(sentences[i * sentences_per_para:(i + 1) * sentences_per_para])
        paragraphs.append(para)

    return paragraphs

def replace_city_in_text(text, city_name):
    """Replace Rouen with the target city name"""
    # Replace various forms
    replacements = {
        'Rouen': city_name,
        'rouen': city_name.lower(),
        'rouennais': f'{city_name.lower()}ais',
        'Métropole Rouen Normandie': f'Métropole de {city_name}',
        'Seine-Maritime': 'région',
        'Normandie': 'région'
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def generate_city_json(city_name, post_name, template, articles):
    """Generate JSON for a specific city"""
    data = json.loads(json.dumps(template))  # Deep copy

    # Select 3 random articles
    selected_articles = random.sample(articles, min(3, len(articles)))

    # Update post_data
    post_data = data[0]['post_data']
    post_data['post_name'] = post_name
    post_data['post_title'] = f"Cabinet {city_name}"
    post_data['guid'] = f"https://staging.site.keobiz.fr/?page_id={post_name}"

    # Replace city references in post_content
    post_content = post_data['post_content']
    post_content = replace_city_in_text(post_content, city_name)

    # Update masonry block content with articles
    for i, article in enumerate(selected_articles[:3]):
        content_html = article.get('content_html', '')
        cleaned_text = clean_html(content_html)

        if len(cleaned_text) > 100:  # Only use if substantial content
            # Update title
            title_key = f"kb_masonry_articles_{i}_kb_masonry_title"
            title = article.get('title', f'Article {i+1} pour {city_name}')
            title = replace_city_in_text(title, city_name)
            post_content = re.sub(
                f'"{title_key}":"[^"]*"',
                f'"{title_key}":"{title}"',
                post_content
            )

            # Update text content
            txt_key = f"kb_masonry_articles_{i}_kb_masonry_txt"
            # Escape quotes and backslashes for JSON
            escaped_text = cleaned_text.replace('\\', '\\\\').replace('"', '\\"')
            escaped_text = replace_city_in_text(escaped_text, city_name)
            post_content = re.sub(
                f'"{txt_key}":"[^"]*"',
                f'"{txt_key}":"{escaped_text}"',
                post_content
            )

    post_data['post_content'] = post_content

    # Update post_meta title
    data[0]['post_meta']['title'] = [f"Cabinet {city_name}", f"Cabinet {city_name}"]

    return data

def main():
    """Main execution"""
    print("Loading template and articles...")
    template = load_template()
    articles = load_articles()

    print(f"Loaded {len(articles)} articles")

    for city_name, post_name in CITIES:
        print(f"Generating {post_name}.json for {city_name}...")
        city_data = generate_city_json(city_name, post_name, template, articles)

        output_file = f"page_ID_{post_name}_data.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(city_data, f, ensure_ascii=False, indent=2)

        print(f"  ✓ Created {output_file}")

    print("\n✅ All 25 files generated successfully!")

if __name__ == "__main__":
    main()
