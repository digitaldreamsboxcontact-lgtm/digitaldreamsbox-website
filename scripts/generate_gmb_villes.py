#!/usr/bin/env python3
"""
Génère les pages fiche Google Business par ville pour digitaldreamsbox.com
Usage: python3 scripts/generate_gmb_villes.py
"""
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..")

VILLES = [
    {
        "slug": "sarreguemines",
        "nom": "Sarreguemines",
        "region": "Moselle",
        "zone": "Sarreguemines, Sarralbe, Puttelange et le secteur de la Sarre",
        "contexte": "À Sarreguemines, quand quelqu'un cherche un artisan ou un prestataire sur Google Maps, il voit en premier les fiches les mieux tenues. Une fiche sans publication récente, sans réponse aux avis, sans photos à jour : elle existe mais elle ne travaille pas. C'est autant de contacts qui partent chez un concurrent mieux visible.",
        "contexte2": "On gère votre fiche Google Business à votre place, entièrement, pour que vous n'ayez rien à faire. Chaque semaine une publication, chaque avis une réponse, chaque mois un rapport chiffré.",
        "metiers": "artisans, commerces et PME de Sarreguemines",
        "faq_q": "Vous intervenez bien sur Sarreguemines et les communes autour ?",
        "faq_r": "Oui. On couvre Sarreguemines, Sarralbe, Puttelange-aux-Lacs et toute la zone de la Sarre mosellane. On se déplace pour le premier échange si vous préférez, ou on travaille entièrement à distance.",
    },
    {
        "slug": "sarrebourg",
        "nom": "Sarrebourg",
        "region": "Moselle",
        "zone": "Sarrebourg, Phalsbourg, Mittersheim et l'arrondissement de Sarrebourg",
        "contexte": "À Sarrebourg, la concurrence sur Google Maps est encore faible pour beaucoup de métiers. C'est le bon moment pour prendre les premières positions avant que vos concurrents s'y mettent. Une fiche active, avec des publications régulières et des avis bien gérés, fait la différence sur les requêtes locales.",
        "contexte2": "On est basés à Mittersheim, à quelques minutes de Sarrebourg. On connaît le territoire et les entreprises qui y travaillent. On gère votre fiche pour qu'elle soit toujours vivante, toujours à jour.",
        "metiers": "artisans, prestataires de services et commerces de Sarrebourg",
        "faq_q": "Vous intervenez sur Sarrebourg et les communes de l'arrondissement ?",
        "faq_r": "Oui. On est basés à Mittersheim, à proximité directe de Sarrebourg. On intervient sur toute la zone : Sarrebourg, Phalsbourg, Héming, Réding et les communes alentour. Audit en présentiel ou à distance selon votre préférence.",
    },
    {
        "slug": "saint-avold",
        "nom": "Saint-Avold",
        "region": "Moselle",
        "zone": "Saint-Avold, L'Hôpital, Carling et le secteur de Saint-Avold",
        "contexte": "À Saint-Avold, entre les artisans indépendants et les PME du secteur industriel, la fiche Google Business est souvent le premier point de contact avec un nouveau client. Une fiche négligée coûte des appels. Une fiche active en génère.",
        "contexte2": "On prend en main votre fiche entièrement : publications hebdomadaires, réponse aux avis, photos, mise à jour des informations. Vous faites votre métier, votre fiche travaille pour vous.",
        "metiers": "artisans, garages, PME et prestataires de Saint-Avold",
        "faq_q": "Vous intervenez bien sur Saint-Avold et les communes autour ?",
        "faq_r": "Oui. On couvre Saint-Avold, L'Hôpital, Carling, Farebersviller et tout le secteur. On se déplace si vous le souhaitez ou on travaille à distance selon la formule qui vous convient le mieux.",
    },
    {
        "slug": "nancy",
        "nom": "Nancy",
        "region": "Meurthe-et-Moselle",
        "zone": "Nancy, Vandoeuvre, Laxou, Essey et l'agglomération du Grand Nancy",
        "contexte": "À Nancy, la concurrence sur Google Maps est plus dense qu'en Moselle. Les entreprises qui ressortent ne sont pas forcément les meilleures : ce sont celles qui ont une fiche active, des avis récents et des publications régulières. Sans ça, même une excellente entreprise reste invisible.",
        "contexte2": "On gère votre fiche Google Business pour qu'elle soit toujours vivante et bien positionnée sur les requêtes locales du Grand Nancy. Publications hebdomadaires, réponses aux avis, rapport mensuel chiffré.",
        "metiers": "PME, prestataires de services, artisans et commerces de Nancy",
        "faq_q": "Vous intervenez bien sur Nancy et l'agglomération du Grand Nancy ?",
        "faq_r": "Oui. On couvre Nancy et toute l'agglomération : Vandoeuvre, Laxou, Essey, Maxéville, Jarville. On travaille principalement à distance mais on peut se déplacer selon la nature du projet.",
    },
    {
        "slug": "saverne",
        "nom": "Saverne",
        "region": "Bas-Rhin",
        "zone": "Saverne, Dettwiller, Marmoutier et le secteur de Saverne en Alsace",
        "contexte": "À Saverne et dans le secteur alsacien, les recherches locales sur Google Maps sont en forte croissance. Les artisans et PME qui ont une fiche active captent une part de trafic que les autres laissent filer. Le secteur est encore peu optimisé : c'est une opportunité à saisir maintenant.",
        "contexte2": "On gère votre fiche Google Business pour les entreprises de Saverne et du Bas-Rhin. Publications, avis, photos, mise à jour : tout est pris en charge. Le financement Grand Est s'applique à votre zone.",
        "metiers": "artisans, commerces et PME de Saverne et du Bas-Rhin",
        "faq_q": "Vous intervenez bien sur Saverne et les communes du secteur alsacien ?",
        "faq_r": "Oui. On couvre Saverne, Dettwiller, Marmoutier, Steinbourg et les communes alentour. On travaille à distance ou en présentiel. Le Parcours Modernisation PME Grand Est s'applique aux entreprises du Bas-Rhin.",
    },
    {
        "slug": "morhange",
        "nom": "Morhange",
        "region": "Moselle",
        "zone": "Morhange, Faulquemont et le secteur de Morhange",
        "contexte": "À Morhange et dans le secteur, beaucoup d'artisans et de PME n'ont pas encore de fiche Google Business sérieusement tenue. C'est précisément là où l'avance se prend le plus facilement : être présent et actif avant que la concurrence s'y mette.",
        "contexte2": "On prend en charge votre fiche entièrement. Publications régulières, réponse aux avis, photos récentes, informations à jour. Vous n'avez rien à faire, on s'occupe de tout.",
        "metiers": "artisans locaux et PME de Morhange et Faulquemont",
        "faq_q": "Vous intervenez bien sur Morhange et les communes autour ?",
        "faq_r": "Oui. On couvre Morhange, Faulquemont et les communes du secteur. On travaille entièrement à distance ce qui nous permet d'intervenir rapidement partout en Moselle.",
    },
    {
        "slug": "dieuze",
        "nom": "Dieuze",
        "region": "Moselle",
        "zone": "Dieuze, Vic-sur-Seille et le secteur du Saulnois",
        "contexte": "À Dieuze et dans le Saulnois, les entreprises locales ont peu de concurrence en ligne. Une fiche Google Business bien tenue peut vous positionner en premier sur des requêtes locales sans que vous ayez à vous battre contre des dizaines de concurrents. C'est un avantage rare à exploiter.",
        "contexte2": "On gère votre fiche pour que cette avance reste dans la durée. Publications, avis, photos, rapport mensuel : tout est pris en charge. Essai 2 mois sans engagement pour voir les résultats concrets.",
        "metiers": "artisans et PME de Dieuze et du Saulnois",
        "faq_q": "Vous intervenez bien sur Dieuze et le secteur du Saulnois ?",
        "faq_r": "Oui. On couvre Dieuze, Vic-sur-Seille et les communes du Saulnois. On travaille entièrement à distance ce qui nous permet d'intervenir rapidement sans contrainte géographique.",
    },
    {
        "slug": "forbach",
        "nom": "Forbach",
        "region": "Moselle",
        "zone": "Forbach, Freyming-Merlebach, Stiring-Wendel et tout le bassin houiller mosellan",
        "contexte": "À Forbach et dans le bassin houiller, quand un client cherche un artisan ou un prestataire sur Google Maps, il voit en premier les fiches les mieux tenues. Une fiche sans publication depuis 6 mois, sans réponse aux avis, sans photos récentes : elle existe mais elle ne travaille pas pour vous.",
        "contexte2": "On prend en main votre fiche entièrement. Chaque semaine une publication, chaque avis une réponse, chaque mois un rapport avec les chiffres réels : vues, appels, demandes d'itinéraire. Vous ne touchez à rien.",
        "metiers": "artisans, commerces et PME de Forbach et du bassin houiller",
        "faq_q": "Vous intervenez bien sur Forbach et le bassin houiller mosellan ?",
        "faq_r": "Oui. On intervient sur Forbach, Freyming-Merlebach, Stiring-Wendel, Farebersviller et toute la zone du bassin houiller. On se déplace sur demande ou on travaille entièrement à distance.",
    },
]

TEMPLATE = """<!doctype html>
<html lang="fr"><head>
<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="theme-color" content="#0B1526">

  <title>Fiche Google Business à {nom} — Digital Dreamsbox | Essai 2 mois sans engagement</title>
  <meta name="description" content="Votre fiche Google Business à {nom} tourne toute l'année sans que vous leviez le petit doigt. Publications, avis, photos. Essai 2 mois sans engagement. Artisans et PME de {nom}, {region}.">
  <link rel="canonical" href="https://digitaldreamsbox.com/fiche-google-business-{slug}.html">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="Fiche Google Business à {nom} — Digital Dreamsbox">
  <meta property="og:description" content="Votre fiche Google tourne 52 semaines par an. Vous ne touchez à rien. Essai 2 mois sans engagement. {nom}, {region}.">
  <meta property="og:url" content="https://digitaldreamsbox.com/fiche-google-business-{slug}.html">
  <meta property="og:image" content="https://digitaldreamsbox.com/assets/og-image.webp">
  <meta property="og:site_name" content="Digital Dreamsbox">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Fiche Google Business à {nom} — Digital Dreamsbox">
  <meta name="twitter:description" content="Votre fiche Google tourne 52 semaines par an. Essai 2 mois sans engagement. {nom}.">
  <meta name="twitter:image" content="https://digitaldreamsbox.com/assets/og-image.webp">

  <link rel="icon" type="image/x-icon" href="favicon.ico" /><link rel="icon" type="image/png" href="favicon-light.png">
  <link rel="apple-touch-icon" href="favicon-light.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=Phudu:wght@400;500;600;700&family=Righteous&family=Baloo+2:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">

  <script type="application/ld+json">
  [
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Fiche Google Business à {nom} — Digital Dreamsbox",
      "url": "https://digitaldreamsbox.com/fiche-google-business-{slug}.html",
      "description": "Digital Dreamsbox gère la fiche Google Business des {metiers}. Publications hebdomadaires, réponse aux avis, photos. Essai 2 mois sans engagement.",
      "inLanguage": "fr",
      "breadcrumb": {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://digitaldreamsbox.com/"}},
          {{"@type": "ListItem", "position": 2, "name": "Fiche Google Business artisans", "item": "https://digitaldreamsbox.com/fiche-google-business-artisan.html"}},
          {{"@type": "ListItem", "position": 3, "name": "Fiche Google Business {nom}"}}
        ]
      }}
    }},
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Digital Dreamsbox",
      "url": "https://digitaldreamsbox.com/",
      "telephone": "+33688848145",
      "email": "contact@digitaldreamsbox.com",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Mittersheim",
        "addressRegion": "Moselle",
        "postalCode": "57930",
        "addressCountry": "FR"
      }},
      "areaServed": ["{nom}", "{region}", "Grand Est"]
    }},
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "{faq_q}",
          "acceptedAnswer": {{"@type": "Answer", "text": "{faq_r}"}}
        }},
        {{
          "@type": "Question",
          "name": "Comment fonctionne l'essai 2 mois sans engagement ?",
          "acceptedAnswer": {{"@type": "Answer", "text": "On démarre sur 2 mois. On gère votre fiche, vous recevez un rapport à J+30 et J+60 avec les chiffres réels. Si les résultats vous convainquent, on continue. Sinon, on s'arrête sans pénalité ni frais cachés."}}
        }},
        {{
          "@type": "Question",
          "name": "Pourquoi la fiche Google Business est-elle importante à {nom} ?",
          "acceptedAnswer": {{"@type": "Answer", "text": "Quand un client cherche un artisan ou un prestataire à {nom} sur Google Maps, il voit en premier les fiches les mieux tenues. Une fiche active génère jusqu'à 7 fois plus de clics qu'une fiche négligée. C'est le premier point de contact avec la majorité de vos futurs clients."}}
        }}
      ]
    }}
  ]
  </script>

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-GNMMKY3BZB"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-GNMMKY3BZB');
    gtag('config', 'AW-18121297118');
  </script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T9M3KKHB" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<div id="pt-overlay"></div>
<script>if(sessionStorage.getItem('pt')){{sessionStorage.removeItem('pt');var _o=document.getElementById('pt-overlay');_o.style.opacity='1';_o.style.pointerEvents='all';setTimeout(function(){{_o.style.transition='opacity 150ms ease-out';_o.style.opacity='0';_o.style.pointerEvents='none';}},60);}}</script>
<div id="bg-blobs"><div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div></div>

<header class="site-header" role="banner">
  <div class="shell-wide nav">
    <a href="index.html" class="brand" aria-label="Digital Dreamsbox — Accueil">
      <img src="mq02h9of-NVlogo-3d-d_d.png" alt="Logo Digital Dreamsbox" width="46" height="46">
      <span class="brand-text"><span class="b1">Digital</span><span class="b2">Dreamsbox</span></span>
    </a>
    <nav class="nav-links" role="navigation" aria-label="Navigation principale">
      <a href="pages/agence.html">Agence</a>
      <a href="pages/services.html">Services</a>
      <a href="pages/galerie.html">Galerie</a>
      <a href="pages/journal.html">Journal</a>
    </nav>
    <div class="nav-cta">
      <a href="tel:+33688848145" class="btn btn-ghost nav-call" aria-label="Appeler Digital Dreamsbox">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"></path></svg>
        Appeler
      </a>
      <a href="#contact" class="btn btn-primary" data-magnet="">Essai 2 mois <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg></a>
    </div>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"></path></svg>
    </button>
  </div>
</header>

<main id="top">

<section class="hero" aria-labelledby="hero-title">
  <div class="shell hero-shell">
    <span class="eyebrow reveal">Google Business · {nom}, {region}</span>
    <h1 id="hero-title" class="hero-title reveal" style="--rd:60ms;">
      Votre fiche Google<br>
      travaille pour vous<br>
      à <span class="accent">{nom}.</span>
    </h1>
    <p class="hero-sub reveal" style="--rd:140ms;">
      Publications, avis, photos, mise à jour continue.<br class="brk-md">
      Pour les {metiers}.<br class="brk-md">
      Essai 2 mois sans engagement. Dès 70€/mois.
    </p>
    <div class="hero-ctas reveal" style="--rd:220ms;">
      <a href="#contact" class="btn btn-primary" data-magnet="">
        Démarrer l'essai 2 mois
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
      <a href="fiche-google-business-artisan.html" class="btn btn-ghost">
        Voir le service complet
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
    </div>
    <div class="hero-meta reveal" style="--rd:320ms;">
      <div><span class="k">Zone couverte</span><span class="v">{nom} &amp; {region}</span></div>
      <div><span class="k">Engagement</span><span class="v">2 mois d'essai sans engagement</span></div>
      <div><span class="k">Tarif</span><span class="v">Dès 70€/mois</span></div>
    </div>
  </div>
</section>

<section class="section-problem" aria-labelledby="context-title-{slug}">
  <div class="shell problem-grid">
    <div>
      <span class="eyebrow reveal">La réalité à {nom}</span>
      <h2 id="context-title-{slug}" class="problem-quote reveal" style="--rd:80ms;">
        Vos clients cherchent sur Google Maps. Votre fiche doit être à la hauteur.
      </h2>
      <p class="body-md reveal" style="--rd:160ms; margin-top:24px; max-width:46ch;">{contexte}</p>
      <p class="body-md reveal" style="--rd:200ms; margin-top:16px; max-width:46ch;">{contexte2}</p>
      <div style="margin-top:32px;" class="reveal">
        <a href="#contact" class="btn btn-solid">
          Démarrer l'essai 2 mois, dès 70€/mois
          <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
        </a>
      </div>
    </div>
    <div class="problem-stack">
      <article class="problem-card reveal from-r">
        <span class="num">01</span>
        <div>
          <h4>Une fiche sans publication depuis 6 mois, ça se voit.</h4>
          <p>Google valorise les fiches actives dans les résultats locaux. Une fiche qui ne bouge pas descend progressivement. Une fiche avec des publications hebdomadaires reste visible.</p>
        </div>
      </article>
      <article class="problem-card reveal from-r" style="--rd:80ms;">
        <span class="num">02</span>
        <div>
          <h4>Des avis sans réponse, ça coûte des clients.</h4>
          <p>95% des entreprises locales ne répondent jamais à leurs avis. Répondre, même à un avis négatif, montre que vous êtes présent et professionnel. On répond à chaque avis dans votre ton.</p>
        </div>
      </article>
      <article class="problem-card reveal from-r" style="--rd:160ms;">
        <span class="num">03</span>
        <div>
          <h4>Vous ne savez pas si votre fiche vous rapporte des clients.</h4>
          <p>Chaque mois, vous recevez les chiffres réels : vues, appels générés, demandes d'itinéraire, clics. Vous savez exactement ce que le service vous rapporte.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section style="padding:64px 0; border-top:1px solid var(--rule);">
  <div class="shell">
    <div class="about-facts">
      <div class="about-fact reveal">
        <div class="v">7×</div>
        <div class="k">Plus de clics</div>
        <div class="d">Un profil actif vs un profil incomplet. Source : Google 2026.</div>
      </div>
      <div class="about-fact reveal" style="--rd:80ms;">
        <div class="v">+9%</div>
        <div class="k">De CA par étoile</div>
        <div class="d">Chaque étoile gagnée sur votre note Google. Source : Harvard Business School.</div>
      </div>
      <div class="about-fact reveal" style="--rd:160ms;">
        <div class="v">95%</div>
        <div class="k">Ne répondent pas</div>
        <div class="d">Des entreprises locales ne répondent jamais à leurs avis. C'est votre avance à prendre.</div>
      </div>
      <div class="about-fact reveal" style="--rd:240ms;">
        <div class="v">2 mois</div>
        <div class="k">Sans engagement</div>
        <div class="d">Essai de 60 jours pour voir les résultats concrets avant de décider de continuer.</div>
      </div>
    </div>
  </div>
</section>

<section style="padding:64px 0; border-top:1px solid var(--rule);">
  <div class="shell">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:start;">
      <div>
        <span class="eyebrow reveal">Ce qu'on gère</span>
        <h2 class="h-section reveal" style="--rd:60ms;">Tout. Vous ne<br>touchez à rien.</h2>
        <p class="body-md reveal" style="--rd:140ms; margin-top:20px; max-width:44ch;">On prend en charge l'intégralité de votre présence Google Business. De la première publication au rapport mensuel, sans que vous ayez à intervenir.</p>
      </div>
      <div class="about-facts" style="display:flex; flex-direction:column; gap:20px;">
        <div class="about-fact reveal from-r" style="text-align:left;">
          <div class="v" style="font-size:1rem;">Publications</div>
          <div class="k">Chaque semaine</div>
          <div class="d">Un post sur votre fiche chaque semaine : réalisations, services, actualités. Votre fiche est toujours vivante.</div>
        </div>
        <div class="about-fact reveal from-r" style="--rd:80ms; text-align:left;">
          <div class="v" style="font-size:1rem;">Avis</div>
          <div class="k">Chaque réponse dans les 48h</div>
          <div class="d">On répond à chaque avis positif ou négatif dans votre ton. Aucun avis laissé sans réponse.</div>
        </div>
        <div class="about-fact reveal from-r" style="--rd:160ms; text-align:left;">
          <div class="v" style="font-size:1rem;">Rapport</div>
          <div class="k">Chaque mois</div>
          <div class="d">Vues, appels, demandes d'itinéraire, clics. Vous savez exactement ce que le service vous rapporte.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="padding:64px 0; border-top:1px solid var(--rule); background:linear-gradient(135deg, rgba(59,130,246,0.05) 0%, transparent 60%);">
  <div class="shell">
    <div style="text-align:center; max-width:52ch; margin:0 auto 40px;">
      <span class="eyebrow reveal">Et si vous voulez aller plus loin</span>
      <h2 class="h-section reveal" style="--rd:60ms;">Combinez Google Business<br>et automatisation.</h2>
      <p class="body-md reveal" style="--rd:120ms; margin-top:16px;">La fiche Google vous rend visible. Les outils d'automatisation vous font gagner 10 à 15 heures par semaine sur les tâches répétitives. Les deux ensemble, c'est la combinaison la plus efficace pour une PME ou un artisan.</p>
    </div>
    <div style="text-align:center;" class="reveal">
      <a href="automatisation-{slug}.html" class="btn btn-ghost">
        Découvrir l'automatisation à {nom}
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
    </div>
  </div>
</section>

<section class="section-faq" id="faq" aria-labelledby="faq-title-{slug}">
  <div class="shell faq-grid">
    <aside class="faq-side">
      <span class="eyebrow reveal">FAQ</span>
      <h2 id="faq-title-{slug}" class="h-section reveal" style="--rd:60ms;">Questions<br>fréquentes.</h2>
      <p class="body-md reveal" style="--rd:140ms;">Une question sur la gestion de votre fiche Google à {nom} ? On répond sous 24 h.</p>
      <div class="ctas reveal" style="--rd:220ms;">
        <a href="#contact" class="btn btn-solid">Démarrer l'essai 2 mois</a>
        <a href="tel:+33688848145" class="btn btn-ghost">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"></path></svg>
          Appeler
        </a>
      </div>
    </aside>
    <div class="faq-list reveal" style="--rd:120ms;">
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>{faq_q}</span>
          <span class="ic"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>
        </button>
        <div class="faq-a"><div class="faq-a-inner">{faq_r}</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>Comment fonctionne l'essai 2 mois sans engagement ?</span>
          <span class="ic"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>
        </button>
        <div class="faq-a"><div class="faq-a-inner">On démarre sur 2 mois. On gère votre fiche, vous recevez un rapport à J+30 et J+60 avec les chiffres réels : vues, appels, demandes d'itinéraire. Si les résultats vous convainquent, on continue. Sinon, on s'arrête sans pénalité ni frais cachés.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>Pourquoi la fiche Google Business est-elle importante à {nom} ?</span>
          <span class="ic"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>
        </button>
        <div class="faq-a"><div class="faq-a-inner">Quand un client cherche un artisan ou un prestataire à {nom} sur Google Maps, il voit en premier les fiches les mieux tenues. Une fiche active génère jusqu'à 7 fois plus de clics qu'une fiche négligée. C'est le premier point de contact avec la majorité de vos futurs clients locaux.</div></div>
      </div>
      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>Est-ce que ce service remplace un site web ?</span>
          <span class="ic"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>
        </button>
        <div class="faq-a"><div class="faq-a-inner">Non, mais il peut fonctionner seul dans un premier temps. La fiche Google Business vous rend visible sur Maps et dans les recherches locales immédiatement. Un site web renforce la crédibilité et convertit mieux les visiteurs. Les deux ensemble donnent les meilleurs résultats.</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section-contact" id="contact" aria-labelledby="contact-title-{slug}">
  <div class="shell contact-grid">
    <div class="contact-side">
      <span class="eyebrow reveal">Démarrer</span>
      <h2 id="contact-title-{slug}" class="reveal" style="--rd:60ms;">
        2 mois pour voir<br>ce que ça donne<br><span class="blue">à {nom}.</span>
      </h2>
      <p class="ctxt reveal" style="--rd:140ms;">Sans engagement. Si les résultats ne vous convainquent pas au bout de 60 jours, on s'arrête. Pas de pénalité, pas de préavis.</p>
      <div class="contact-actions reveal" style="--rd:220ms;">
        <a href="tel:+33688848145" class="btn btn-primary" data-magnet="">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"></path></svg>
          Appeler directement
        </a>
        <a href="#" class="btn btn-ghost" data-vcard="">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Ajouter au contact
        </a>
      </div>
    </div>
    <div class="contact-card reveal" style="--rd:200ms;">
      <h3>Démarrer l'essai 2 mois à {nom}</h3>
      <p class="sub">Réponse sous 24 h ouvrées. Aucun engagement.</p>
      <form id="contact-form" class="form" novalidate action="https://formspree.io/f/xaqzyzgk" method="POST">
        <div class="field"><label for="f-name">Nom &amp; prénom</label><input id="f-name" name="name" type="text" required autocomplete="name"></div>
        <div class="field"><label for="f-company">Entreprise &amp; activité</label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
        <div class="field"><label for="f-phone">Téléphone</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
        <div class="field">
          <label for="f-need">Ce qui vous intéresse</label>
          <select id="f-need" name="need" required>
            <option value="">Sélectionner</option>
            <option>Fiche Google Business uniquement (70€/mois)</option>
            <option>Fiche Google + automatisation</option>
            <option>Je veux d'abord en discuter</option>
          </select>
        </div>
        <input type="hidden" name="source_page" value="fiche-google-business-{slug}">
        <input type="hidden" name="ville" value="{nom}">
        <input type="hidden" name="_next" value="https://digitaldreamsbox.com/pages/merci.html">
        <div class="honeypot" aria-hidden="true"><label>Ne pas remplir<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="form-actions">
          <small>En envoyant, vous acceptez notre politique de confidentialité.</small>
          <button type="submit" class="btn btn-primary">Démarrer l'essai <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg></button>
        </div>
        <div class="form-success" role="status">Demande reçue. On vous recontacte sous 24 h ouvrées.</div>
      </form>
    </div>
  </div>
</section>

<section style="padding:48px 0; border-top:1px solid var(--rule);">
  <div class="shell" style="text-align:center;">
    <span class="eyebrow">Nos autres services à {nom}</span>
    <p style="color:var(--muted); margin:12px 0 28px; font-size:0.95rem;">Google Business, automatisation, site web. Un seul interlocuteur.</p>
    <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
      <a href="automatisation-{slug}.html" class="btn btn-ghost">Automatisation à {nom}</a>
      <a href="fiche-google-business-artisan.html" class="btn btn-ghost">Google Business artisans</a>
      <a href="index.html" class="btn btn-ghost">Retour à l'accueil</a>
    </div>
  </div>
</section>

</main>

<footer class="site-footer" role="contentinfo">
  <div class="shell">
    <div class="footer-top">
      <div>
        <div class="brand"><img src="mq02h9of-NVlogo-3d-d_d.png" alt="" width="46" height="46"></div>
        <p class="footer-blurb">Agence de marque &amp; design visuel.</p>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="pages/services.html#branding">Branding</a></li>
          <li><a href="pages/services.html#sites-web">Sites web</a></li>
          <li><a href="fiche-google-business-artisan.html">Google Business</a></li>
          <li><a href="automatisation-pme-artisan.html">Automatisation</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Agence</h5>
        <ul>
          <li><a href="pages/agence.html">Qui sommes-nous</a></li>
          <li><a href="pages/galerie.html">Galerie</a></li>
          <li><a href="pages/journal.html">Journal</a></li>
          <li><a href="pages/contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Google Business</h5>
        <ul>
          <li><a href="fiche-google-business-forbach.html">Forbach</a></li>
          <li><a href="fiche-google-business-sarreguemines.html">Sarreguemines</a></li>
          <li><a href="fiche-google-business-sarrebourg.html">Sarrebourg</a></li>
          <li><a href="fiche-google-business-saint-avold.html">Saint-Avold</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Digital Dreamsbox. Tous droits réservés.</p>
      <div class="footer-legal">
        <a href="pages/mentions-legales.html">Mentions légales</a>
        <a href="pages/cgv.html">CGV</a>
        <a href="pages/confidentialite.html">Confidentialité</a>
      </div>
    </div>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>"""


def generate():
    generated = []
    for v in VILLES:
        # Skip Forbach — already exists as a manually crafted page
        if v["slug"] == "forbach":
            print(f"  SKIP fiche-google-business-forbach.html (déjà créée manuellement)")
            continue
        content = TEMPLATE.format(**v)
        filename = f"fiche-google-business-{v['slug']}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        generated.append(filename)
        print(f"  OK  {filename}")
    print(f"\n{len(generated)} pages générées.")
    return generated


if __name__ == "__main__":
    print("Génération des pages fiche Google Business par ville...")
    generate()
