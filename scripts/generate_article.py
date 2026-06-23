#!/usr/bin/env python3
"""
Génération automatique d'articles de blog — Digital Dreamsbox
Appelle Gemini API, crée le HTML et met à jour journal.html.
"""

import os, re, json, datetime, unicodedata
import google.generativeai as genai

# ── Chemins ────────────────────────────────────────────────────────────────
ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL_DIR   = os.path.join(ROOT, 'pages', 'journal')
JOURNAL_INDEX = os.path.join(ROOT, 'pages', 'journal.html')
STATE_FILE    = os.path.join(ROOT, 'scripts', 'blog_state.json')

# ── Sujets d'articles ─────────────────────────────────────────────────────
TOPICS = [
    {
        "slug": "vitrine-google-maps-artisan",
        "title": "Google Maps pour artisans : comment apparaître en premier dans votre ville",
        "h1_end": "apparaître en premier dans <span class=\"blue\">votre ville.</span>",
        "category": "SEO local", "mark": "SEO", "type": "Guide", "duration": "6"
    },
    {
        "slug": "site-web-artisan-2026",
        "title": "Pourquoi un site web reste indispensable pour un artisan en 2026",
        "h1_end": "reste indispensable pour un artisan <span class=\"blue\">en 2026.</span>",
        "category": "Présence digitale", "mark": "WEB", "type": "Article", "duration": "5"
    },
    {
        "slug": "reseaux-sociaux-pme-moselle",
        "title": "Réseaux sociaux pour PME locales : ce qui marche vraiment en Moselle",
        "h1_end": "ce qui marche vraiment <span class=\"blue\">en Moselle.</span>",
        "category": "Réseaux sociaux", "mark": "RS", "type": "Guide", "duration": "7"
    },
    {
        "slug": "avis-google-comment-en-obtenir",
        "title": "Avis Google : comment en obtenir plus sans y passer des heures",
        "h1_end": "comment en obtenir plus <span class=\"blue\">sans y passer des heures.</span>",
        "category": "SEO local", "mark": "SEO", "type": "Article", "duration": "5"
    },
    {
        "slug": "budget-site-web-artisan",
        "title": "Combien coûte un vrai site web pour un artisan en 2026",
        "h1_end": "combien coûte un vrai site web pour un artisan <span class=\"blue\">en 2026.</span>",
        "category": "Site web", "mark": "WEB", "type": "Guide", "duration": "6"
    },
    {
        "slug": "seo-local-sans-agence",
        "title": "SEO local : 6 actions gratuites qu'un artisan peut faire seul ce week-end",
        "h1_end": "6 actions gratuites qu'un artisan peut faire <span class=\"blue\">seul ce week-end.</span>",
        "category": "SEO local", "mark": "SEO", "type": "Article", "duration": "7"
    },
    {
        "slug": "identite-visuelle-pme",
        "title": "Identité visuelle pour PME : la différence entre paraître et convaincre",
        "h1_end": "la différence entre paraître <span class=\"blue\">et convaincre.</span>",
        "category": "Branding", "mark": "ID", "type": "Guide", "duration": "8"
    },
    {
        "slug": "google-ads-budget-minimum",
        "title": "Google Ads : quel budget minimum pour un artisan du Grand Est",
        "h1_end": "quel budget minimum pour un artisan <span class=\"blue\">du Grand Est.</span>",
        "category": "Google Ads", "mark": "ADS", "type": "Étude", "duration": "6"
    },
    {
        "slug": "site-web-qui-convertit",
        "title": "Pourquoi votre site web ne génère pas de contacts (et comment y remédier)",
        "h1_end": "ne génère pas de contacts <span class=\"blue\">(et comment y remédier).</span>",
        "category": "Site web", "mark": "WEB", "type": "Article", "duration": "6"
    },
    {
        "slug": "branding-artisan-moselle",
        "title": "Branding pour artisans en Moselle : construire une image qui rassure",
        "h1_end": "construire une image qui <span class=\"blue\">rassure.</span>",
        "category": "Branding", "mark": "ID", "type": "Guide", "duration": "7"
    },
    {
        "slug": "prospection-digitale-locale",
        "title": "Prospection digitale : trouver des clients locaux sans démarchage agressif",
        "h1_end": "trouver des clients locaux <span class=\"blue\">sans démarchage agressif.</span>",
        "category": "Développement commercial", "mark": "BIZ", "type": "Article", "duration": "6"
    },
    {
        "slug": "refonte-site-web-quand",
        "title": "Refonte de site web : les 5 signes qu'il est temps de tout recommencer",
        "h1_end": "les 5 signes qu'il est <span class=\"blue\">temps de tout recommencer.</span>",
        "category": "Site web", "mark": "WEB", "type": "Article", "duration": "5"
    },
]

# ── Utilitaires ────────────────────────────────────────────────────────────
MONTHS_FR = ['janvier','février','mars','avril','mai','juin',
             'juillet','août','septembre','octobre','novembre','décembre']

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, encoding='utf-8') as f:
            return json.load(f)
    return {"used_slugs": [], "article_count": 3}

def save_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def pick_topic(state):
    used = state.get('used_slugs', [])
    for t in TOPICS:
        if t['slug'] not in used:
            return t
    # Tous utilisés : on repart au début
    state['used_slugs'] = []
    return TOPICS[0]

def thumb_variant(n):
    return f"v{(n % 3) + 1}"

# ── Appel Gemini ───────────────────────────────────────────────────────────
def generate_content(topic):
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""Tu es le rédacteur de Digital Dreamsbox, agence web & branding à Sarrebourg (Moselle, Grand Est, France).
Tu écris des articles de blog professionnels en français pour des artisans et PME locales.

STYLE OBLIGATOIRE :
- Direct, sans jargon. Chiffres et exemples concrets.
- Exemples locaux : Moselle, Grand Est, Sarrebourg, Phalsbourg, Sarreguemines.
- Jamais de tirets longs (—). Jamais de phrases d'introduction creuses.
- Ton expert mais accessible. Pas condescendant.
- Entre 750 et 1000 mots de contenu visible.

SUJET DE L'ARTICLE : {topic['title']}
CATÉGORIE : {topic['category']}

Retourne UNIQUEMENT un objet JSON valide, sans balises markdown, avec ces champs :
{{
  "meta_description": "description SEO max 155 caractères avec mot-clé principal",
  "og_description": "description partage social max 120 caractères",
  "lede": "2 phrases d'accroche percutantes pour le hero (max 220 caractères total)",
  "excerpt": "1 phrase courte et incisive pour la card de liste (max 110 caractères)",
  "sommaire": ["point 1", "point 2", "point 3", "point 4", "point 5"],
  "sections": [
    {{
      "h2": "Titre de section",
      "html": "<p>Contenu en HTML. Utilise <strong>, <em>, <ul><li>, <ol><li> si pertinent.</p>"
    }}
  ],
  "blockquote": "Citation ou statistique percutante avec source entre parenthèses",
  "cta_title": "Titre du call-to-action en fin d'article (court, direct)",
  "cta_text": "1-2 phrases pour le CTA (offre concrète, sans engagement)"
}}

L'article doit avoir exactement 5 sections h2. Pas de conclusion séparée, intègre-la dans la dernière section.
Chaque section : 2-4 paragraphes, avec listes à puces si pertinent.
"""

    resp = model.generate_content(prompt)
    raw = resp.text.strip()

    # Extraire le JSON même si Gemini ajoute du texte autour
    match = re.search(r'\{[\s\S]*\}', raw)
    if not match:
        raise ValueError(f"Pas de JSON dans la réponse Gemini :\n{raw[:400]}")
    return json.loads(match.group())

# ── Construction du HTML ───────────────────────────────────────────────────
def build_article_html(topic, data, pub_date, pub_date_fr):
    sections_html = ''
    for s in data['sections']:
        sections_html += f'\n        <h2>{s["h2"]}</h2>\n        {s["html"]}\n'

    sommaire_items = '\n'.join(f'            <li>{item}</li>' for item in data['sommaire'])

    # Les 2 premiers articles existants comme "Aller plus loin"
    related = [
        ('<a href="seo-fiche-google.html" style="color:var(--sky);">Fiche Google Business : 5 erreurs qui coûtent des appels</a>'
         if topic['slug'] != 'seo-fiche-google' else
         '<a href="branding-logo-identite.html" style="color:var(--sky);">Logo vs identité visuelle</a>'),
        ('<a href="google-ads-plombier.html" style="color:var(--sky);">Google Ads pour un plombier : combien investir ?</a>'
         if topic['slug'] != 'google-ads-plombier' else
         '<a href="branding-logo-identite.html" style="color:var(--sky);">Logo vs identité visuelle</a>'),
    ]
    related_html = '\n'.join(f'            <li>{r}</li>' for r in related)

    # Échapper les accolades pour f-string
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": topic['title'],
        "description": data['meta_description'],
        "image": "https://digitaldreamsbox.com/assets/logo-full.jpg",
        "datePublished": pub_date,
        "author": {"@type": "Organization", "name": "Digital Dreamsbox"},
        "publisher": {"@type": "Organization", "name": "Digital Dreamsbox",
                      "logo": {"@type": "ImageObject", "url": "https://digitaldreamsbox.com/assets/logo-full.jpg"}}
    }, ensure_ascii=False, indent=4)

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0" />
  <meta name="theme-color" content="#1a2536" />

  <title>{topic['title']} · Digital Dreamsbox</title>
  <meta name="description" content="{data['meta_description']}" />
  <link rel="canonical" href="https://digitaldreamsbox.com/pages/journal/{topic['slug']}.html" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{topic['title']}" />
  <meta property="og:description" content="{data['og_description']}" />
  <meta property="og:image" content="https://digitaldreamsbox.com/assets/logo-full.jpg" />
  <link rel="icon" type="image/x-icon" href="../../favicon.ico" />
  <link rel="icon" type="image/png" href="../../favicon-light.png" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=Phudu:wght@400;500;600;700&family=Righteous&family=Baloo+2:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../styles.css" />

  <script type="application/ld+json">
  {schema}
  </script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GNMMKY3BZB"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-GNMMKY3BZB');
  </script>
</head>
<body>
<div id="pt-overlay"></div>
<script>if(sessionStorage.getItem('pt')){{sessionStorage.removeItem('pt');var _o=document.getElementById('pt-overlay');_o.style.opacity='1';_o.style.pointerEvents='all';setTimeout(function(){{_o.style.transition='opacity 150ms ease-out';_o.style.opacity='0';_o.style.pointerEvents='none';}},60);}}</script>
<div id="bg-blobs"><div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div></div>

<header class="site-header" role="banner">
  <div class="shell-wide nav">
    <a href="../../index.html" class="brand"><img src="../../mq02h9of-NVlogo-3d-d_d.png" alt="Logo Digital Dreamsbox" width="46" height="46" /><span class="brand-text"><span class="b1">Digital</span><span class="b2">Dreamsbox</span></span></a>
    <nav class="nav-links" aria-label="Navigation principale">
      <a href="../agence.html">Agence</a>
      <a href="../services.html">Services</a>
      <a href="../galerie.html">Galerie</a>
      <a href="../journal.html" aria-current="page">Journal</a>
    </nav>
    <div class="nav-cta">
      <a href="tel:+33688848145" class="btn btn-ghost nav-call"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>Appeler</a>
      <a href="../contact.html" class="btn btn-primary" data-magnet>Nous contacter<svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a>
    </div>
    <button class="nav-toggle" aria-expanded="false" aria-label="Menu"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
  </div>
</header>

<main>

<section class="page-hero">
  <div class="shell-wide inner">
    <div>
      <div class="crumbs reveal">
        <a href="../../index.html">Accueil</a>
        <span class="sep">/</span>
        <a href="../journal.html">Journal</a>
        <span class="sep">/</span>
        <span>{topic['category']}</span>
      </div>
      <span class="eyebrow reveal">{topic['type']} · {topic['duration']} min · {topic['category']}</span>
      <h1 class="reveal" style="--rd:60ms;">{topic['h1_end']}</h1>
    </div>
    <p class="lede reveal" style="--rd:140ms;">{data['lede']}</p>
  </div>
</section>

<section class="article">
  <div class="shell">
    <div class="article-grid">
      <article class="article-body reveal">
        {sections_html}
        <blockquote>{data['blockquote']}</blockquote>

        <div class="article-cta">
          <div>
            <h3>{data['cta_title']}</h3>
            <p>{data['cta_text']}</p>
          </div>
          <a href="../../index.html#contact" class="btn btn-primary" data-magnet>Demander un audit gratuit<svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a>
        </div>
      </article>

      <aside class="article-aside">
        <div class="box">
          <h4>Au sommaire</h4>
          <ul>
{sommaire_items}
          </ul>
        </div>
        <div class="box">
          <h4>Infos article</h4>
          <div class="meta-line"><span>Publié</span><span>{pub_date_fr}</span></div>
          <div class="meta-line"><span>Lecture</span><span>{topic['duration']} min</span></div>
          <div class="meta-line"><span>Catégorie</span><span>{topic['category']}</span></div>
          <div class="meta-line"><span>Auteur</span><span>Digital Dreamsbox</span></div>
        </div>
        <div class="box">
          <h4>Aller plus loin</h4>
          <ul>
{related_html}
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>

</main>

<footer class="site-footer" role="contentinfo">
  <div class="shell">
    <div class="footer-top">
      <div><div class="brand"><img src="../../mq02h9of-NVlogo-3d-d_d.png" alt="" width="46" height="46" /><span class="brand-text"><span class="b1">Digital</span><span class="b2">Dreamsbox</span></span></div><p class="footer-blurb">Agence de marque &amp; design visuel.</p></div>
      <div class="footer-col"><h5>Services</h5><ul><li><a href="../services.html#branding">Branding</a></li><li><a href="../services.html#sites-web">Sites web</a></li><li><a href="../services.html#google-ads">Google Ads</a></li></ul></div>
      <div class="footer-col"><h5>Agence</h5><ul><li><a href="../agence.html">Qui sommes-nous</a></li><li><a href="../galerie.html">Galerie</a></li><li><a href="../journal.html">Journal</a></li><li><a href="../../index.html#faq">FAQ</a></li></ul></div>
      <div class="footer-col"><h5>Contact</h5><ul><li><a href="tel:+33688848145">06 88 84 81 45</a></li><li><a href="mailto:contact@digitaldreamsbox.com">contact@digitaldreamsbox.com</a></li></ul></div>
      <div class="footer-col"><h5>Réseaux</h5><ul><li><a href="https://www.youtube.com/@DigitalDreamsbox" target="_blank" rel="noopener">YouTube</a></li><li><a href="https://www.instagram.com/digital_dreamsbox/" target="_blank" rel="noopener">Instagram</a></li><li><a href="https://www.linkedin.com/in/digital-dreamsbox-749b29371" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>&copy; <span data-year>2026</span> Digital Dreamsbox &mdash; Tous droits réservés.</span><span><a href="../mentions-legales.html">Mentions légales</a> &middot; <a href="../confidentialite.html">Politique de confidentialité</a> &middot; <a href="../cgv.html">CGV</a></span></div>
  </div>
</footer>

<script src="../../script.js" defer></script>
</body>
</html>'''

# ── Mise à jour journal.html ───────────────────────────────────────────────
def update_journal_index(topic, data, article_count):
    with open(JOURNAL_INDEX, 'r', encoding='utf-8') as f:
        html = f.read()

    variant = thumb_variant(article_count)
    delay = (article_count % 3) * 80

    new_card = f'''
      <a href="journal/{topic['slug']}.html" class="bcard reveal" style="--rd:{delay}ms;">
        <div class="thumb {variant}">
          <div class="grid"></div>
          <div class="mark" aria-hidden="true">{topic['mark']}</div>
          <span class="tag">{topic['category']}</span>
        </div>
        <div class="body">
          <span class="meta">{topic['type']} · {topic['duration']} min</span>
          <h3>{topic['title']}</h3>
          <p>{data['excerpt']}</p>
          <span class="read">Lire l'article<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span>
        </div>
      </a>'''

    # Insérer juste avant la fermeture du blog-grid
    html = re.sub(
        r'(</div>\s*</div>\s*</section>\s*\n*</main>)',
        new_card + r'\n    \1',
        html,
        count=1
    )

    with open(JOURNAL_INDEX, 'w', encoding='utf-8') as f:
        f.write(html)

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    state = load_state()
    topic = pick_topic(state)

    print(f"Sujet choisi : {topic['title']}")

    data = generate_content(topic)
    print("Contenu généré par Gemini.")

    today = datetime.date.today()
    pub_date    = today.isoformat()
    pub_date_fr = f"{today.day} {MONTHS_FR[today.month - 1]} {today.year}"

    article_html = build_article_html(topic, data, pub_date, pub_date_fr)

    # Écrire le fichier article
    out_path = os.path.join(JOURNAL_DIR, f"{topic['slug']}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(article_html)
    print(f"Article créé : {out_path}")

    # Mettre à jour journal.html
    update_journal_index(topic, data, state['article_count'])
    print("journal.html mis à jour.")

    # Sauvegarder l'état
    state['used_slugs'].append(topic['slug'])
    state['article_count'] += 1
    save_state(state)

    print(f"Terminé. Article publié : {topic['slug']}.html")

if __name__ == '__main__':
    main()
