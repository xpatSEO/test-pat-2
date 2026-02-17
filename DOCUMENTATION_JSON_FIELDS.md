# Documentation des champs - page_ID_3866_data.json

## Vue d'ensemble
Fichier JSON contenant les données d'une page WordPress (ID: 3866) pour le cabinet comptable Keobiz à Rouen.

---

## 1. Structure principale

### 1.1 post_data
Contient toutes les informations de base de la publication WordPress.

| Champ | Type | Description | Exemple |
|-------|------|-------------|---------|
| `ID` | integer | Identifiant unique de la page | 3866 |
| `post_author` | string | ID de l'auteur | "12" |
| `post_date` | datetime | Date de publication (heure locale) | "2022-03-07 14:58:25" |
| `post_date_gmt` | datetime | Date de publication (GMT) | "2022-03-07 13:58:25" |
| `post_content` | string | Contenu HTML/Gutenberg de la page | Blocs ACF (voir section 2) |
| `post_title` | string | Titre de la page | "Cabinet Rouen" |
| `post_excerpt` | string | Extrait de la page | "" (vide) |
| `post_status` | string | Statut de publication | "publish" |
| `comment_status` | string | Statut des commentaires | "closed" |
| `ping_status` | string | Statut des pings | "closed" |
| `post_password` | string | Mot de passe de protection | "" (vide) |
| `post_name` | string | Slug URL de la page | "cabinet-rouen" |
| `to_ping` | string | URLs à notifier | "" (vide) |
| `pinged` | string | URLs notifiées | "" (vide) |
| `post_modified` | datetime | Date de modification (locale) | "2026-01-16 16:01:21" |
| `post_modified_gmt` | datetime | Date de modification (GMT) | "2026-01-16 15:01:21" |
| `post_content_filtered` | string | Contenu filtré | "" (vide) |
| `post_parent` | integer | ID de la page parente | 0 |
| `guid` | string | URL unique globale | "https://staging.site.keobiz.fr/?page_id=3866" |
| `menu_order` | integer | Ordre dans le menu | 108 |
| `post_type` | string | Type de publication | "page" |
| `post_mime_type` | string | Type MIME | "" (vide) |
| `comment_count` | string | Nombre de commentaires | "0" |
| `filter` | string | Filtre appliqué | "raw" |

---

## 2. Blocs ACF dans post_content

### 2.1 acf/header-breadcrumb
En-tête de la page avec fil d'Ariane et appel à l'action.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_header_title` | HTML | Titre principal avec span | "Notre cabinet à Rouen pour <span>simplifier et optimiser</span> votre gestion comptable" |
| `kb_header_desc` | text | Description sous le titre | "La gestion d'une entreprise consomme du temps..." |
| `kb_header_img` | integer | ID de l'image d'en-tête | 23676 |
| `kb_header_show_btn` | boolean | Afficher le bouton CTA | "1" |
| `kb_header_btn_txt` | string | Texte du bouton | "Obtenir un devis" |
| `kb_header_btn_url` | string | URL du bouton | "/nous-contacter/" |
| `kb_header_mention` | string | Mention sous le bouton | "Gratuit et sans engagement." |
| `kb_header_img_experts` | integer | ID image des experts | 24652 |
| `kb_header_coupon_active` | boolean | Coupon actif | "0" |

### 2.2 acf/partners-new
Section des partenaires.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_partners_title` | string | Titre de la section | "" (vide) |
| `kb_partners_subtitle` | string | Sous-titre | "Nos partenaires, acteurs de notre succès." |
| `kb_partners_list` | integer | Nombre de partenaires | 10 |
| `kb_partners_list_{n}_kb_partners_item_title` | string | Titre du partenaire n | "" (vide pour tous) |
| `kb_partners_list_{n}_kb_partners_item_img` | integer | ID image partenaire n | 23752, 23751, 23750, etc. |

**Note**: n varie de 0 à 9 (10 partenaires au total)

### 2.3 acf/intro-image
Section d'introduction avec image.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_intro_image_title` | HTML | Titre avec span | "À quoi sert un cabinet d'expert à <span>Rouen</span> ?" |
| `kb_intro_image_img` | integer | ID de l'image | 23766 |
| `kb_intro_image_description` | HTML | Description longue | Texte explicatif avec balises strong |
| `kb_intro_image_btn` | string | URL du bouton | "/nous-contacter/" |

### 2.4 acf/horaire-block
Bloc des horaires et coordonnées.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_horaire_title` | HTML | Titre de la section | "<span>Rendez-nous visite</span> dans nos <br />locaux à Rouen" |
| `kb_horaire_subtitle` | string | Sous-titre | "" (vide) |
| `kb_horaire_email` | email | Email de contact | "info@staging.site.keobiz.fr" |
| `kb_horaire_address` | string | Adresse | "14-18 Rue Henri Rivière," |
| `kb_horaire_postal_code` | string | Code postal | "76000" |
| `kb_horaire_city` | string | Ville | "Rouen" |
| `kb_horaire_country` | string | Code pays | "FR" |
| `kb_horaire_phone` | string | Téléphone | "+33 01 76 41 05 60" |
| `kb_horaire_map` | HTML | Iframe Google Maps | iframe embed code |
| `kb_horaire_itineraire` | URL | Lien Google Maps itinéraire | URL Google Maps |
| `kb_horaire_list` | integer | Nombre de jours | 7 |

**Détail des horaires (kb_horaire_list_{n}):**

| Jour (n) | kb_horaire_item_day | kb_horaire_item_hour |
|----------|---------------------|----------------------|
| 0 | "Lundi" | "09:00-13:00 - 14:00-18:30" |
| 1 | "Mardi" | "09:00-13:00 - 14:00-18:30" |
| 2 | "Mercredi" | "09:00-13:00 - 14:00-18:30" |
| 3 | "Jeudi" | "09:00-13:00 - 14:00-18:30" |
| 4 | "Vendredi" | "09:00-13:00 - 14:00-17:00" |
| 5 | "Samedi" | "Fermé" |
| 6 | "Dimanche" | "Fermé" |

### 2.5 acf/form-image
Formulaire avec image.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_form_img_title` | HTML | Titre du formulaire | "Optez pour nos services <br />et lancez-vous !" |
| `kb_form_img_subtitle` | string | Sous-titre | "Recevez votre devis gratuit..." |
| `kb_form_img_list` | string | ID de liste | "25" |
| `kb_form_img_image` | integer | ID de l'image | 23658 |
| `kb_form_img_image_desc` | HTML | Description image | "<span>10h</span> de gagnés dans <br />la semaine !" |

### 2.6 acf/avantages-style2
Section des avantages (style 2).

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_avantages_style2_title` | HTML | Titre de la section | "Pourquoi travailler avec <span>nos professionnels</span>..." |
| `kb_avantages_style2_subtitle` | string | Sous-titre | "Faire confiance à notre cabinet..." |
| `kb_avantages_style2_left_description` | HTML | Description à gauche | Texte avec H2 et strong |
| `kb_avantages_style2_left_link` | string | Lien CTA gauche | "/nous-contacter/" |
| `kb_avantages_style2_list` | integer | Nombre d'avantages | 5 |

**Détail des avantages (kb_avantages_style2_list_{n}):**

| n | Icon ID | Titre | Description |
|---|---------|-------|-------------|
| 0 | 23806 | "Accompagnement au plus près de vos besoins" | "Un chargé de mission comptable dédié..." |
| 1 | 23809 | "La sécurisation de vos données sensibles" | "Innovation et expertise combinées..." |
| 2 | 23800 | "Le meilleur de l'humain et de la technologie" | "Keobiz est un professionnel..." |
| 3 | 23799 | "Une tarification compétitive et adaptée..." | "Des prix adaptés à chaque entreprise..." |
| 4 | 23811 | "Un suivi comptable partout en France" | "Bénéficiez d'une assistance dédiée..." |

Tous ont un lien vers `/nous-contacter/`

### 2.7 acf/carousel-metier
Carrousel des métiers/secteurs.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_carousel_metier_title` | HTML | Titre | "Quels secteurs d'activités sont <span>pris en charge</span>..." |
| `kb_carousel_metier_subtitle` | string | Sous-titre | "Inscrit au tableau de l'Ordre..." |
| `metiers` | array | Liste d'IDs de métiers | ["986","940","678","18501","955","946","943"] |

### 2.8 acf/offers-new-block
Bloc des offres.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_offers_title` | HTML | Titre | "Des offres <span>adaptées à vos besoins.</span>" |
| `kb_offers_subtitle` | string | Sous-titre | "" (vide) |
| `kb_offers_list` | array | Liste d'IDs d'offres | ["25896","24919","25897","25898"] |

### 2.9 acf/list-simulators
Liste des simulateurs.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_list_simulators_title` | HTML | Titre | "Des outils de simulation pour <br /><span>vous guider</span>..." |
| `kb_list_simulators_subtitle` | string | Sous-titre | "" (vide) |
| `kb_list_simulators_link_all` | object | Lien vers tous les outils | {title, url, target} |
| `kb_list_simulators_items` | integer | Nombre de simulateurs | 6 |

**Détail des simulateurs (kb_list_simulators_items_{n}):**

| n | Icon ID | Titre | URL ID |
|---|---------|-------|--------|
| 0 | 23628 | "Calculez votre prix de vente" | 23154 |
| 1 | 23635 | "Calculez le coût de votre salarié" | 23681 |
| 2 | 23639 | "Calculateur des impôts sur les sociétés" | 23156 |
| 3 | 23620 | "Calculer les indemnités de frais kilométriques" | 23683 |
| 4 | 23631 | "Calculez le nombre de jours ouvrés" | 23689 |
| 5 | 23627 | "Calculez votre capital social" | 23152 |

### 2.10 acf/testimonials-new
Bloc des témoignages.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `data` | array | Données vides | [] (aucun témoignage configuré) |

### 2.11 acf/faq-post-new
Section FAQ.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_faq_title` | HTML | Titre | "Des réponses expertes à chacune de <br /> vos questions" |
| `kb_faq_mode` | string | Mode d'affichage | "unique" |
| `kb_faq_list` | integer | Nombre de questions | 4 |

**Détail des FAQ (kb_faq_list_{n}):**

| n | Question | Réponse (résumé) |
|---|----------|------------------|
| 0 | "Comment échanger avec nos experts-comptables ?" | Contact à distance ou sur place |
| 1 | "Le cabinet Keobiz est-il inscrit à l'Ordre..." | Oui, inscrit à l'Ordre |
| 2 | "Le cabinet Keobiz prend-il en charge la gestion de la paie ?" | Oui, gestion complète de la paie |
| 3 | "Nos experts-comptables sont-ils aussi commissaires aux comptes ?" | Ce sont deux compétences distinctes |

### 2.12 acf/info-block
Bloc d'information/CTA.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_info_title` | HTML | Titre | "Accélérez votre croissance avec Keobiz..." |
| `kb_info_description` | string | Description | "Libérez-vous de vos tâches chronophages..." |
| `kb_info_btn_txt` | string | Texte du bouton | "Appeler un conseiller" |
| `kb_info_btn_link` | string | Lien du bouton | "tel:0176410560" |

### 2.13 acf/masonry-blocks
Blocs en maçonnerie (articles longs).

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `kb_masonry_title` | string | Titre de la section | "" (vide) |
| `kb_masonry_subtitle` | string | Sous-titre | "" (vide) |
| `kb_masonry_articles` | integer | Nombre d'articles | 3 |

**Détail des articles (kb_masonry_articles_{n}):**

| n | Titre | Contenu |
|---|-------|---------|
| 0 | "Quels services sont proposés par votre <span>cabinet..." | Détails sur tous les services (comptabilité, création, business plan, etc.) |
| 1 | "Pourquoi faire appel à un comptable à Rouen ?" | Avantages de faire appel à un expert-comptable |
| 2 | "Pourquoi travailler avec nos professionnels..." | 5 raisons de choisir Keobiz |

---

## 3. post_meta
Métadonnées de la page WordPress.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `title` | array | Titres multiples | ["Cabinet Rouen", "Cabinet Rouen"] |
| `whodunit_config_virtual_page` | array | Config page virtuelle | ["0"] |
| `_yoast_wpseo_estimated-reading-time-minutes` | array | Temps de lecture estimé | ["0"] |
| `_wp_page_template` | array | Template WordPress | ["default"] |
| `_dp_original` | array | ID original Duplicate Post | ["134"] |
| `_edit_lock` | array | Verrou d'édition | ["1768575687:39"] |
| `_edit_last` | array | Dernier éditeur | ["39"] |
| `form_source` | array | Source du formulaire | ["KEO"] |
| `_yoast_wpseo_metadesc` | array | Meta description SEO | ["Faites appel aux services d'un cabinet comptable à Rouen..."] |
| `_yoast_wpseo_title` | array | Titre SEO | ["Keobiz - Le Cabinet d'Expertise comptable à Rouen"] |
| `_yoast_wpseo_wordproof_timestamp` | array | Timestamp WordProof | [""] |
| `hide_actions` | array | Masquer actions | ["0"] |
| `_pys_head_footer` | array | Scripts head/footer | Tableau de configuration |
| `hide_logo` | array | Masquer logo | ["0"] |
| `commentary` | array | Commentaire | [""] |
| `ao_post_optimize` | array | Optimisation Autoptimize | Configuration d'optimisation |
| `footnotes` | array | Notes de bas de page | [""] |
| `_custom_header_design` | array | Design header custom | ["yes"] |
| `_yoast_wpseo_content_score` | array | Score contenu Yoast | ["90"] |

---

## 4. taxonomies
Taxonomies WordPress associées.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `taxonomies` | array | Liste des taxonomies | [] (vide) |

---

## 5. feature_img
Image à la une.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `feature_img` | boolean | Image à la une définie | false |

---

## 6. acf_fields
Champs ACF de haut niveau.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `whodunit_config_virtual_page` | boolean | Page virtuelle | false |
| `form_source` | string | Source du formulaire | "KEO" |
| `hide_actions` | boolean | Masquer actions | false |
| `hide_logo` | boolean | Masquer logo | false |
| `commentary` | string | Commentaire | "" (vide) |

---

## 7. post_type
Type de publication WordPress.

| Champ | Type | Description | Valeur |
|-------|------|-------------|--------|
| `post_type` | string | Type de publication | "page" |

---

## Nomenclature des champs ACF

### Préfixes utilisés
- `kb_` : Keobiz (préfixe général)
- `_kb_` : Version privée/meta du champ (utilise le même field_id)

### Suffixes courants
- `_title` : Titre
- `_subtitle` : Sous-titre
- `_desc` / `_description` : Description
- `_img` / `_image` : Image (ID)
- `_btn` : Bouton
- `_txt` : Texte
- `_url` / `_link` : URL/Lien
- `_list` : Liste/Tableau
- `_item` : Élément d'une liste
- `_icon` : Icône

### Champs field_XXXXX
Chaque champ ACF a un identifiant unique au format `field_XXXXXXXXXXXXX` stocké dans la clé privée `_nom_du_champ`.

---

## IDs d'images référencées

| ID | Utilisation |
|----|-------------|
| 23676 | Image en-tête principale |
| 24652 | Image experts en-tête |
| 23752-23743 | Images partenaires (10 images) |
| 23766 | Image introduction |
| 23658 | Image formulaire |
| 23806, 23809, 23800, 23799, 23811 | Icônes avantages |
| 23628, 23635, 23639, 23620, 23631, 23627 | Icônes simulateurs |

---

## IDs de contenu référencés

### Métiers
- 986, 940, 678, 18501, 955, 946, 943

### Offres
- 25896, 24919, 25897, 25898

### Simulateurs (pages)
- 23154, 23681, 23156, 23683, 23689, 23152

---

## Notes techniques

1. **Encodage** : Les caractères spéciaux sont encodés en Unicode (\u00e9 pour é, etc.)
2. **HTML** : Plusieurs champs contiennent du HTML brut (balises strong, span, br, h2, etc.)
3. **Structure répétitive** : Les listes ACF utilisent la nomenclature `{nom_champ}_{index}_{sous_champ}`
4. **Champs privés** : Chaque champ ACF public a son équivalent privé préfixé par `_` contenant le field_id
5. **Mode** : Tous les blocs ACF ont `"mode": "edit"` indiquant qu'ils sont en mode édition
6. **className** : Certains blocs ont des classes CSS personnalisées (ex: "padding-top-0")

---

**Date de documentation** : 2026-02-17
**Version du fichier** : Dernière modification 2026-01-16 16:01:21
