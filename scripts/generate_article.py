#!/usr/bin/env python3
"""
Publication automatique d'articles de blog — Digital Dreamsbox
Publie chaque semaine le prochain article pré-rédigé.
"""

import os, re, json, datetime, unicodedata
from html import escape as html_escape

ROOT          = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNAL_DIR   = os.path.join(ROOT, 'pages', 'journal')
JOURNAL_INDEX = os.path.join(ROOT, 'pages', 'journal.html')
STATE_FILE    = os.path.join(ROOT, 'scripts', 'blog_state.json')
SITEMAP_FILE  = os.path.join(ROOT, 'sitemap.xml')

_CFG_FILE = os.path.join(os.path.dirname(__file__), 'config_digitaldreamsbox.json')
with open(_CFG_FILE, encoding='utf-8') as _f:
    CFG = json.load(_f)

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

ARTICLES_DATA = {
    "vitrine-google-maps-artisan": {
        "meta_description": "Artisan en Moselle ? Découvrez comment optimiser votre fiche Google Maps pour capter plus d'appels et apparaître en premier dans les recherches locales.",
        "og_description": "Le guide pratique pour artisans : optimiser Google Maps et décrocher plus de chantiers en Moselle.",
        "lede": "80% des recherches locales aboutissent à un contact dans les 24 heures. Si votre fiche Google n'est pas optimisée, vous offrez vos chantiers à la concurrence.",
        "excerpt": "Votre fiche Google Maps peut vous rapporter des appels chaque jour. Voici comment la rendre imbattable.",
        "sommaire": [
            "Pourquoi Google Maps prime sur votre site web en local",
            "Les 5 éléments incontournables d'une fiche optimisée",
            "Avis clients : la méthode pour en obtenir sans insister",
            "Photos et publications : le contenu qui rassure",
            "Suivre ses résultats et s'améliorer chaque mois"
        ],
        "sections": [
            {
                "h2": "Pourquoi Google Maps prime sur votre site web en local",
                "html": "<p>Quand un propriétaire à Sarrebourg cherche un plombier d'urgence, il ne visite pas des sites web. Il tape \"plombier Sarrebourg\" sur son téléphone et appelle directement depuis le résultat affiché. Ce bloc de 3 fiches en haut de page, c'est le <strong>Local Pack</strong>. Il capte plus de 70% des clics. Les sites web classiques récupèrent les miettes.</p><p>Pour un artisan ou une PME locale, figurer dans ce Local Pack vaut souvent plus qu'un site parfaitement référencé. Et optimiser sa fiche Google Business Profile est gratuit, ne demande pas de compétences techniques, juste de la méthode et un peu de régularité.</p>"
            },
            {
                "h2": "Les 5 éléments incontournables d'une fiche optimisée",
                "html": "<p>Une fiche incomplète est pénalisée par l'algorithme et décourage les prospects. Commencez par ces cinq points :</p><ul><li><strong>Nom exact :</strong> Votre nom commercial tel qu'il figure sur vos devis. Pas de mots-clés artificiels ajoutés.</li><li><strong>Catégorie principale :</strong> La plus précise possible. \"Plombier-chauffagiste\" est plus efficace que \"Artisan\".</li><li><strong>Zone de service :</strong> Citez toutes vos communes. Sarrebourg, Phalsbourg, Sarreguemines, Réding, Lorquin...</li><li><strong>Horaires à jour :</strong> Pensez aux jours fériés. Un client qui appelle hors des horaires affichés peut signaler votre fiche.</li><li><strong>Numéro direct :</strong> Celui auquel vous décrochez réellement.</li></ul><p>Complétez la description avec vos spécialités et certifications (RGE, Qualibat, QualiPV). Chaque champ rempli renforce votre position dans les résultats.</p>"
            },
            {
                "h2": "Avis clients : la méthode pour en obtenir sans insister",
                "html": "<p>Les avis sont le facteur numéro un de classement dans le Local Pack. Un artisan avec 45 avis à 4,7 étoiles écrase presque toujours celui qui a 8 avis à 5 étoiles. La quantité compte autant que la note.</p><p>La méthode simple : créez un lien court vers votre formulaire d'avis et envoyez-le par SMS le jour même de la fin du chantier. Un message sobre suffit : \"Bonjour M. Martin, merci pour votre confiance. Un avis ici m'aiderait beaucoup si vous êtes satisfait : [lien].\"</p><ul><li>Ne promettez jamais de remise en échange d'un avis, c'est interdit par Google.</li><li>Répondez à tous vos avis, positifs et négatifs. Une réponse professionnelle à un avis négatif rassure plus que son absence.</li><li>Évitez de demander des avis depuis votre propre appareil : Google peut les filtrer.</li></ul>"
            },
            {
                "h2": "Photos et publications : le contenu qui rassure",
                "html": "<p>Une fiche avec des photos reçoit 42% de demandes d'itinéraire en plus et 35% de clics supplémentaires (source : Google). Pour un artisan, les photos avant/après de chantiers sont particulièrement convaincantes.</p><p>Visez un minimum de 10 photos : logo, véhicule, équipements, et 5 à 7 réalisations récentes avec accord du client. Renouvelez-les régulièrement.</p><p>Les <strong>publications Google Business</strong> sont l'outil le plus sous-utilisé par les artisans. Une fois par semaine : une offre de saison, un chantier réalisé, un conseil pratique. Cinq minutes qui signalent à Google que votre fiche est active.</p>"
            },
            {
                "h2": "Suivre ses résultats et s'améliorer chaque mois",
                "html": "<p>Google Business Profile propose des statistiques gratuites dans l'onglet \"Performance\". Trois chiffres à surveiller chaque mois :</p><ul><li><strong>Recherches indirectes :</strong> les requêtes du type \"plombier Sarrebourg\" montrent que vous captez des inconnus.</li><li><strong>Appels téléphoniques :</strong> si ce chiffre est faible malgré un bon classement, vérifiez votre numéro et vos horaires.</li><li><strong>Demandes d'itinéraires :</strong> utile si vous avez un showroom ou un atelier ouvert.</li></ul><p>Trente minutes par mois suffisent : répondre aux avis récents, ajouter des photos de nouveaux chantiers, mettre à jour les horaires. C'est exactement ce que vos concurrents ne font pas. Et c'est pour ça que ça marche.</p>"
            }
        ],
        "blockquote": "\"Les entreprises avec une fiche Google complète ont 70% plus de chances d'attirer des visites.\" (Google Business Profile, 2024)",
        "cta_title": "On audite votre présence Google ?",
        "cta_text": "On analyse votre fiche locale en 30 minutes et on vous dit exactement ce qui vous fait perdre des appels. Gratuit et sans engagement.",
        "faq": [
            {"q": "Combien de temps faut-il pour apparaître dans le Local Pack Google ?", "a": "Avec une fiche Google Business Profile complète et optimisée, vous pouvez apparaître dans le Local Pack en 2 à 6 semaines. Le délai dépend de la concurrence dans votre zone et de la qualité de votre fiche. Les premiers avis clients accélèrent significativement le processus."},
            {"q": "Google Maps peut-il remplacer un site web pour un artisan ?", "a": "Non, les deux sont complémentaires. Google Maps capte les prospects qui cherchent activement un artisan en urgence. Le site web rassure et convertit ceux qui veulent vérifier votre sérieux avant d'appeler. Sans site, vous perdez jusqu'à 40% des prospects qualifiés."},
            {"q": "Comment créer sa fiche Google Business Profile gratuitement ?", "a": "Rendez-vous sur business.google.com, cliquez sur \"Gérer maintenant\" et suivez les étapes. Vous devrez vérifier votre entreprise par courrier (code reçu en 5 à 14 jours) ou par téléphone. La fiche est entièrement gratuite et sans abonnement."}
        ],
        "related": [
            {"slug": "avis-google-comment-en-obtenir", "title": "Avis Google : comment en obtenir plus sans y passer des heures"},
            {"slug": "seo-local-sans-agence", "title": "SEO local : 6 actions gratuites qu'un artisan peut faire seul"}
        ]
    },
    "site-web-artisan-2026": {
        "meta_description": "Fiche Google ou site web ? Pour un artisan en 2026, les deux sont complémentaires. Voici pourquoi négliger l'un coûte des clients chaque mois.",
        "og_description": "En 2026, votre site web reste votre meilleur commercial disponible 24h/24. Voici pourquoi un artisan ne peut plus s'en passer.",
        "lede": "Beaucoup d'artisans pensent que leur fiche Google suffit. En réalité, sans site web, vous perdez les prospects qui vérifient votre sérieux avant d'appeler.",
        "excerpt": "En 2026, votre site web reste votre meilleur commercial. Voici pourquoi un artisan ne peut vraiment plus s'en passer.",
        "sommaire": [
            "Ce que fait votre site que Google ne peut pas faire",
            "Les 4 idées reçues qui freinent les artisans",
            "Ce qu'un client regarde sur votre site avant d'appeler",
            "Site vitrine ou site performant : la différence concrète",
            "Combien investir et quoi attendre en retour"
        ],
        "sections": [
            {
                "h2": "Ce que fait votre site que Google ne peut pas faire",
                "html": "<p>Votre fiche Google Business est excellente pour être trouvé. Mais quand un client hésite entre trois artisans, il visite leurs sites pour trancher. Ce moment de décision, c'est votre site qui doit le remporter.</p><p>Un site web vous permet de raconter qui vous êtes, de montrer vos réalisations, d'expliquer votre méthode et de rassurer sur vos garanties et certifications. Il capte aussi des requêtes SEO longues que votre fiche seule ne touche pas : \"rénovation salle de bain Sarrebourg devis\", \"isolation combles Phalsbourg artisan RGE\"...</p>"
            },
            {
                "h2": "Les 4 idées reçues qui freinent les artisans",
                "html": "<ul><li><strong>\"Mes clients viennent par le bouche-à-oreille.\"</strong> Vrai. Mais ces clients vérifient quand même votre site avant d'appeler. Un site absent ou vieillissant sème le doute.</li><li><strong>\"Je n'ai pas le temps.\"</strong> Un site bien conçu ne demande aucune mise à jour fréquente. Il travaille pendant que vous êtes sur le chantier.</li><li><strong>\"C'est trop cher.\"</strong> Un seul client décroché grâce au site rembourse souvent l'investissement. Le rapport coût/retour est meilleur que la publicité papier.</li><li><strong>\"Les réseaux sociaux suffisent.\"</strong> Vous ne possédez pas vos réseaux. Une page Facebook peut être suspendue du jour au lendemain. Votre site vous appartient.</li></ul>"
            },
            {
                "h2": "Ce qu'un client regarde sur votre site avant d'appeler",
                "html": "<p>Les comportements en ligne sont connus : un internaute passe en moyenne 45 secondes sur un site artisan avant de décider de rester ou de partir. Voici ce qu'il cherche, dans l'ordre :</p><ol><li>Est-ce que cet artisan intervient dans ma commune ?</li><li>A-t-il réalisé des chantiers similaires au mien ?</li><li>Quels sont ses délais et ses tarifs approximatifs ?</li><li>Y a-t-il des avis ou témoignages clients visibles ?</li><li>Comment le contacter rapidement ?</li></ol><p>Si votre site répond à ces cinq questions clairement et vite, le client appelle. Sinon, il revient sur Google et choisit le suivant.</p>"
            },
            {
                "h2": "Site vitrine ou site performant : la différence concrète",
                "html": "<p>Il y a une vraie différence entre un site qui existe et un site qui convertit. Un site vitrine basique présente l'entreprise mais ne génère aucun contact actif. Un site performant guide le visiteur vers un appel ou un formulaire : chargement rapide sur mobile, textes qui répondent aux vraies questions, boutons d'action visibles.</p><p>Concrètement : un artisan couvreur en Moselle avec un site optimisé sur \"couvreur Sarrebourg\" et \"réparation toiture Grand Est\" peut recevoir 3 à 8 demandes de devis par mois depuis son site seul. C'est souvent zéro avec un site vitrine mal conçu.</p>"
            },
            {
                "h2": "Combien investir et quoi attendre en retour",
                "html": "<p>Un site professionnel pour un artisan se situe entre 800 et 3 000 euros selon la complexité. C'est un investissement ponctuel, pas une dépense mensuelle.</p><p>Pour évaluer le retour : si votre marge sur un chantier moyen est de 500 euros et que votre site vous apporte 2 nouveaux clients par mois, il se rembourse en un mois. La vraie question n'est pas \"est-ce que ça vaut le coup ?\" mais \"quel est le coût de ne pas l'avoir ?\".</p><p>Chaque client qui vous cherche sur Google, trouve votre concurrent mieux présenté, et l'appelle à votre place : c'est votre manque à gagner réel. Chez Digital Dreamsbox, on accompagne les artisans du Grand Est dans la création de sites qui génèrent de vrais contacts.</p>"
            }
        ],
        "blockquote": "\"75% des internautes jugent la crédibilité d'une entreprise à travers la qualité de son site web.\" (Stanford Web Credibility Research)",
        "cta_title": "Votre site attire-t-il vraiment des clients ?",
        "cta_text": "On analyse votre site gratuitement et on vous dit ce qui bloque vos prospects. Résultat en 48h, sans engagement.",
        "faq": [
            {"q": "Un site Wix ou Jimdo est-il suffisant pour un artisan en 2026 ?", "a": "Pour débuter, oui. Pour être compétitif en SEO local, non. Les constructeurs en ligne ont des limitations techniques (vitesse, structure des URLs, balises) qui freinent le référencement. Si votre objectif est de générer des contacts depuis Google, un site professionnel optimisé sera plus efficace à moyen terme."},
            {"q": "Faut-il un site web si j'ai déjà une bonne fiche Google ?", "a": "Oui. La fiche Google génère des appels rapides, mais le site web convertit les prospects qui veulent vérifier votre sérieux avant de vous contacter. Les deux se complètent : 70% des prospects visitent le site web avant d'appeler, même s'ils vous ont trouvé via Google Maps."},
            {"q": "Combien de temps avant qu'un site génère ses premiers contacts ?", "a": "Entre 2 et 6 mois pour les premiers résultats organiques (SEO). En parallèle, un site bien conçu génère des contacts dès le premier jour via Google Ads ou vos partages sur les réseaux sociaux. Le SEO est un investissement long terme, la publicité donne des résultats immédiats."}
        ],
        "related": [
            {"slug": "budget-site-web-artisan", "title": "Combien coûte un vrai site web pour un artisan en 2026"},
            {"slug": "site-web-qui-convertit", "title": "Pourquoi votre site web ne génère pas de contacts"}
        ]
    },
    "reseaux-sociaux-pme-moselle": {
        "meta_description": "Instagram, Facebook, LinkedIn : quels réseaux sociaux choisir pour une PME en Moselle ? Le guide concret pour ne pas perdre du temps sur les mauvaises plateformes.",
        "og_description": "Réseaux sociaux pour PME en Moselle : ce qui génère vraiment des clients et ce qui ne sert à rien.",
        "lede": "Beaucoup de PME locales sont présentes partout sur les réseaux et ne génèrent aucun client. Le problème n'est pas la fréquence de publication, c'est la stratégie.",
        "excerpt": "Instagram, Facebook, LinkedIn : ce qui marche vraiment pour une PME en Moselle et ce qui ne sert à rien.",
        "sommaire": [
            "Pourquoi la plupart des PME gaspillent du temps sur les réseaux",
            "Choisir la bonne plateforme selon votre activité",
            "Le type de contenu qui génère de vraies demandes",
            "Fréquence et régularité : ce qui compte vraiment",
            "Mesurer ce qui marche et arrêter ce qui ne sert à rien"
        ],
        "sections": [
            {
                "h2": "Pourquoi la plupart des PME gaspillent du temps sur les réseaux",
                "html": "<p>Le piège classique : publier des photos génériques, des citations motivantes et des voeux de bonne année sans jamais montrer ce qu'on fait concrètement. Résultat : des likes de proches, zéro nouveau client.</p><p>Les réseaux sociaux génèrent des clients quand ils répondent à une question ou résolvent un problème. \"Avant/après rénovation à Sarreguemines\", \"comment on isole des combles de A à Z\", \"les 3 questions à poser avant de choisir un carreleur\" : ce type de contenu attire les bons prospects.</p>"
            },
            {
                "h2": "Choisir la bonne plateforme selon votre activité",
                "html": "<p>Vous n'avez pas à être partout. Choisissez une ou deux plateformes et soyez présent efficacement :</p><ul><li><strong>Facebook :</strong> toujours le réseau le plus utilisé en Moselle par les 35-60 ans. Indispensable pour les artisans, les commerces de proximité et les services aux particuliers. Les groupes locaux (\"Bon plan Sarrebourg\", \"Entraide Grand Est\") sont une mine d'or.</li><li><strong>Instagram :</strong> efficace pour les métiers visuels : décoration, menuiserie, paysagisme, cuisine. Moins pertinent pour la plomberie ou l'électricité pure.</li><li><strong>LinkedIn :</strong> réservé aux B2B. Si vous ciblez des entreprises ou des professionnels, c'est là. Pas pour les artisans qui travaillent exclusivement avec des particuliers.</li></ul>"
            },
            {
                "h2": "Le type de contenu qui génère de vraies demandes",
                "html": "<p>Ce qui fonctionne, ce sont les contenus qui montrent votre expertise et créent de la confiance :</p><ul><li><strong>Avant/après :</strong> une photo de chantier avant et une après. Simple, efficace, partageable.</li><li><strong>Coulisses :</strong> une vidéo de 30 secondes en intervention. Pas besoin de montage. L'authenticité vend mieux que la perfection.</li><li><strong>Conseils pratiques :</strong> \"Comment détecter une fuite sans appeler un plombier\" ou \"3 signes que votre toiture doit être vérifiée avant l'hiver\". Vous aidez, vous montrez votre expertise, vous restez en tête.</li><li><strong>Témoignages clients :</strong> une capture d'écran d'un message de satisfaction ou une courte vidéo client. Le plus persuasif de tous.</li></ul>"
            },
            {
                "h2": "Fréquence et régularité : ce qui compte vraiment",
                "html": "<p>Un post par semaine publié régulièrement vaut mieux que cinq posts en une semaine puis deux mois de silence. Les algorithmes favorisent la régularité. Vos abonnés aussi.</p><p>Pour tenir dans la durée, réduisez la friction : prenez des photos à chaque chantier (30 secondes sur place), et rédigez vos posts par batch une fois par mois. Une heure en soirée pour programmer quatre semaines de publications.</p><p>Utilisez un outil gratuit comme Meta Business Suite pour programmer vos publications Facebook et Instagram à l'avance. Publiez entre 18h et 20h en semaine et le samedi matin pour maximiser la portée en Moselle.</p>"
            },
            {
                "h2": "Mesurer ce qui marche et arrêter ce qui ne sert à rien",
                "html": "<p>Regardez vos statistiques une fois par mois. Les chiffres qui comptent pour une PME locale : les messages reçus, les clics vers votre site ou téléphone, et la portée (combien de personnes ont vu votre contenu, incluant les non-abonnés).</p><p>Les likes ne payent pas vos factures. Un post avec 8 likes et 2 demandes de devis est infiniment plus utile qu'un post avec 120 likes et aucun contact.</p><p>Si après 3 mois de publication régulière sur une plateforme vous n'avez reçu aucun contact qualifié, changez soit le type de contenu, soit la plateforme. Ne continuez pas par habitude.</p>"
            }
        ],
        "blockquote": "\"67% des consommateurs affirment que les réseaux sociaux influencent leurs décisions d'achat locales.\" (BrightLocal, 2024)",
        "cta_title": "On définit votre stratégie réseaux ?",
        "cta_text": "On vous aide à choisir les bonnes plateformes et le bon type de contenu pour votre activité. Un échange de 30 minutes suffit pour y voir clair.",
        "faq": [
            {"q": "Instagram ou Facebook : quel réseau choisir en priorité pour un artisan en Moselle ?", "a": "Facebook reste le réseau numéro un pour les artisans en Moselle. La tranche 35-60 ans, qui représente l'essentiel des clients particuliers, y est très active. Instagram est pertinent si votre métier est visuel (décoration, menuiserie, paysagisme). Commencez par Facebook avant d'ouvrir un Instagram."},
            {"q": "Faut-il vraiment être sur tous les réseaux sociaux ?", "a": "Non, c'est même contre-productif. Mieux vaut être très actif sur un ou deux réseaux que présent partout mais invisible. Choisissez une plateforme principale selon votre clientèle cible, maîtrisez-la, puis envisagez une deuxième plateforme uniquement si vous avez du temps disponible."},
            {"q": "Combien de fois par semaine faut-il publier sur les réseaux pour être efficace ?", "a": "Une à deux fois par semaine est suffisant pour un artisan, à condition d'être régulier. La régularité prime sur la fréquence. Un post par semaine pendant 6 mois vaut mieux que 5 posts par semaine pendant 3 semaines puis plus rien."}
        ],
        "related": [
            {"slug": "identite-visuelle-pme", "title": "Identité visuelle pour PME : paraître ou convaincre"},
            {"slug": "prospection-digitale-locale", "title": "Prospection digitale : trouver des clients locaux sans démarchage"}
        ]
    },
    "avis-google-comment-en-obtenir": {
        "meta_description": "Les avis Google sont le facteur numéro 1 de confiance pour les clients locaux. Voici la méthode simple pour en obtenir régulièrement sans y passer des heures.",
        "og_description": "Comment obtenir plus d'avis Google pour votre entreprise sans harceler vos clients ? La méthode simple et éprouvée.",
        "lede": "Un artisan avec 40 avis à 4,6 étoiles décroche plus de chantiers qu'un concurrent noté 5 étoiles avec 5 avis. La quantité compte autant que la note.",
        "excerpt": "Plus d'avis Google sans y passer des heures : la méthode concrète que les artisans et PME peuvent appliquer dès aujourd'hui.",
        "sommaire": [
            "Pourquoi les avis Google changent vraiment la donne",
            "La méthode SMS : simple, rapide, efficace",
            "Comment répondre aux avis (positifs et négatifs)",
            "Les erreurs qui font filtrer ou supprimer vos avis",
            "Automatiser la collecte sans outil payant"
        ],
        "sections": [
            {
                "h2": "Pourquoi les avis Google changent vraiment la donne",
                "html": "<p>Dans le Local Pack (les 3 entreprises affichées en haut des résultats Google), les avis influencent directement le classement. Plus vous en avez, plus ils sont récents, mieux vous vous positionnez.</p><p>Côté clients : 88% des consommateurs font autant confiance aux avis en ligne qu'à une recommandation personnelle (BrightLocal). Une fiche avec 50 avis inspirera confiance même à quelqu'un qui ne vous a jamais entendu parler. Une fiche avec 4 avis anciens, même parfaits, génère du doute.</p>"
            },
            {
                "h2": "La méthode SMS : simple, rapide, efficace",
                "html": "<p>La façon la plus efficace d'obtenir des avis : envoyer un SMS le jour même de la fin du chantier ou de la prestation, quand la satisfaction du client est au maximum.</p><p>Un modèle qui fonctionne : \"Bonjour [Prénom], merci pour votre confiance. Si vous êtes satisfait de notre intervention, un avis Google m'aiderait beaucoup : [lien court]. Merci et à bientôt !\"</p><p>Pour le lien court, allez dans votre fiche Google Business, cliquez sur \"Demander des avis\" et copiez le lien généré. Vous pouvez le raccourcir sur bit.ly pour faciliter le tap sur mobile.</p><p>Taux de conversion moyen : entre 25 et 40% des clients contactés laissent effectivement un avis quand on leur demande immédiatement après une prestation réussie.</p>"
            },
            {
                "h2": "Comment répondre aux avis (positifs et négatifs)",
                "html": "<p>Répondre à vos avis montre que vous êtes attentif et professionnel. Google favorise aussi les fiches dont le propriétaire est actif.</p><p><strong>Avis positifs :</strong> répondez en remerciant, en personnalisant (mentionnez le type de chantier ou la commune si possible), et en invitant à revenir ou à recommander. Pas besoin de trois paragraphes. Deux phrases suffisent.</p><p><strong>Avis négatifs :</strong> répondez toujours, calmement et professionnellement, même si l'avis est injuste. Expliquez les faits sans attaquer. Proposez de résoudre le problème en privé. Un avis négatif bien géré publiquement rassure souvent plus qu'une fiche sans aucun avis négatif.</p>"
            },
            {
                "h2": "Les erreurs qui font filtrer ou supprimer vos avis",
                "html": "<p>Google dispose d'algorithmes pour détecter les avis frauduleux. Ces pratiques peuvent faire supprimer vos avis, voire signaler votre fiche :</p><ul><li>Demander des avis en échange d'une remise ou d'un cadeau.</li><li>Demander à des amis ou à la famille de laisser des avis sans avoir utilisé votre service.</li><li>Faire laisser des avis depuis votre propre Wi-Fi ou appareil (même adresse IP que la fiche).</li><li>Demander des avis en masse à un groupe de clients en même temps : une hausse soudaine d'avis est suspecte.</li></ul><p>La méthode naturelle, un client à la fois, est la plus sûre et la plus durable.</p>"
            },
            {
                "h2": "Automatiser la collecte sans outil payant",
                "html": "<p>Si vous avez un logiciel de gestion de chantier ou un CRM, vérifiez s'il propose une fonctionnalité d'envoi automatique de demande d'avis après clôture d'un dossier. Certains outils comme Obat, Batiprix ou Jepilote intègrent cette option.</p><p>Sans logiciel : créez un simple rappel récurrent dans votre calendrier (chaque vendredi soir, par exemple) pour envoyer vos demandes d'avis à tous les clients de la semaine. Dix minutes hebdomadaires suffisent pour accumuler 4 à 6 avis par mois, soit 50 à 70 avis supplémentaires sur un an.</p><p>Cinquante avis à 4,5 étoiles en un an, ça transforme votre fiche Google et ça change votre volume d'appels entrants. C'est probablement l'action la plus rentable que vous pouvez faire cette semaine.</p>"
            }
        ],
        "blockquote": "\"88% des consommateurs font autant confiance aux avis en ligne qu'à une recommandation personnelle.\" (BrightLocal Local Consumer Review Survey)",
        "cta_title": "On optimise votre présence Google ensemble ?",
        "cta_text": "Audit de votre fiche Google Business gratuit et sans engagement. On vous dit exactement ce qui freine vos prospects avant qu'ils appellent.",
        "faq": [
            {"q": "Peut-on demander à sa famille ou ses amis de laisser des avis Google ?", "a": "Non. Google le détecte et filtre ces avis, voire les supprime. Les avis doivent provenir de vrais clients ayant eu une interaction avec votre entreprise. Des avis suspects peuvent aussi déclencher une suspension de votre fiche, ce qui est très difficile à résoudre."},
            {"q": "Comment réagir face à un faux avis négatif ?", "a": "Répondez calmement et professionnellement en expliquant que vous n'avez pas de trace de cette intervention. Signalez l'avis à Google via le bouton \"Signaler un avis\" en précisant qu'il ne concerne pas un vrai client. Google supprime environ 30% des avis signalés pour faux témoignage."},
            {"q": "Combien d'avis Google faut-il viser en priorité ?", "a": "L'objectif minimal pour être compétitif dans le Local Pack est de 30 à 50 avis avec une note supérieure à 4,5/5. En dessous de 15 avis, votre fiche est perçue comme peu établie. Visez 4 à 5 nouveaux avis par mois pour maintenir votre fiche active aux yeux de Google."}
        ],
        "related": [
            {"slug": "vitrine-google-maps-artisan", "title": "Google Maps pour artisans : apparaître en premier dans votre ville"},
            {"slug": "seo-local-sans-agence", "title": "SEO local : 6 actions gratuites qu'un artisan peut faire seul"}
        ]
    },
    "budget-site-web-artisan": {
        "meta_description": "Combien coûte un site web pour un artisan en 2026 ? De 0 à 5 000 euros selon les options. Voici ce que chaque budget vous apporte vraiment.",
        "og_description": "Site web artisan : les vrais prix en 2026 et ce que chaque budget vous apporte concrètement.",
        "lede": "Entre un site fait maison et une agence premium, les écarts de prix sont immenses. Voici ce que vous achetez vraiment à chaque niveau de budget.",
        "excerpt": "Combien coûte vraiment un site web professionnel pour un artisan en 2026 ? Les vrais prix et ce qu'on obtient.",
        "sommaire": [
            "Les différentes options et leurs vrais coûts",
            "Ce qu'un site gratuit ou bon marché ne peut pas faire",
            "Le budget optimal pour un artisan local",
            "Les coûts cachés à anticiper",
            "Comment évaluer le retour sur investissement"
        ],
        "sections": [
            {
                "h2": "Les différentes options et leurs vrais coûts",
                "html": "<p>Il existe plusieurs façons de se faire un site web, avec des coûts et des résultats très différents :</p><ul><li><strong>Constructeur en ligne (Wix, Jimdo, Squarespace) :</strong> 0 à 30 euros/mois. Simple à prendre en main, mais résultats SEO limités et design générique.</li><li><strong>Freelance ou agence bas de gamme :</strong> 500 à 1 500 euros. Variable selon la qualité. Attention aux sites livrés sans suivi ni optimisation.</li><li><strong>Agence locale spécialisée :</strong> 1 500 à 4 000 euros. Un site pensé pour convertir des visiteurs en clients, avec SEO local intégré.</li><li><strong>Agence premium ou grands groupes :</strong> 5 000 euros et plus. Rarement justifié pour un artisan ou une PME locale.</li></ul>"
            },
            {
                "h2": "Ce qu'un site gratuit ou bon marché ne peut pas faire",
                "html": "<p>Un site à 300 euros peut exister, être présentable visuellement, et ne jamais générer un seul appel. Voici pourquoi :</p><ul><li>Pas de travail SEO : votre site n'apparaîtra pas sur les requêtes de vos prospects.</li><li>Pas d'optimisation mobile : 70% des recherches locales se font sur téléphone.</li><li>Pas de stratégie de conversion : le visiteur arrive et repart sans agir.</li><li>Pas de suivi : vous ne savez pas si votre site génère des contacts ou non.</li></ul><p>Un site bon marché peut même vous faire du mal : un site lent, non sécurisé ou avec un design amateur nuit à votre crédibilité auprès de prospects qui vous découvrent pour la première fois.</p>"
            },
            {
                "h2": "Le budget optimal pour un artisan local",
                "html": "<p>Pour un artisan ou une PME en Moselle qui veut un site qui génère vraiment des clients, le budget réaliste est entre <strong>1 500 et 2 500 euros</strong>. Ce budget vous donne :</p><ul><li>Un site responsive (parfait sur mobile et desktop)</li><li>Un travail SEO local sur vos communes d'intervention</li><li>Des pages optimisées pour vos services principaux</li><li>Un formulaire de contact et des boutons d'appel visibles</li><li>Une formation basique pour ajouter des photos ou actualités vous-même</li></ul><p>En dessous de 1 000 euros, les compromis sur la qualité sont presque inévitables. Au-dessus de 3 500 euros, interrogez-vous sur ce que vous achetez vraiment.</p>"
            },
            {
                "h2": "Les coûts cachés à anticiper",
                "html": "<p>Le prix de création n'est pas le seul à prévoir. Voici ce qui s'ajoute souvent :</p><ul><li><strong>Nom de domaine :</strong> 10 à 15 euros/an. Incontournable.</li><li><strong>Hébergement :</strong> 5 à 20 euros/mois selon les prestataires.</li><li><strong>Maintenance et mises à jour :</strong> si votre site tourne sous WordPress, les mises à jour et la sécurité peuvent nécessiter une intervention régulière (50 à 150 euros/an).</li><li><strong>Photos professionnelles :</strong> 200 à 500 euros pour une séance photo de vos réalisations. Facultatif mais très impactant.</li></ul><p>Demandez toujours à votre prestataire le coût total sur 3 ans, pas seulement le prix de création.</p>"
            },
            {
                "h2": "Comment évaluer le retour sur investissement",
                "html": "<p>L'erreur courante est de regarder le coût du site sans calculer ce qu'il peut rapporter. Voici un calcul simple : si votre marge sur un chantier moyen est de 600 euros et que votre site génère 2 nouveaux clients par mois grâce au SEO, c'est 1 200 euros de marge mensuelle. Un site à 2 000 euros est remboursé en moins de deux mois.</p><p>Pour mesurer concrètement : demandez à vos nouveaux clients comment ils vous ont trouvé. Installez Google Analytics pour voir le trafic. Activez le suivi des appels dans Google Business pour compter les contacts générés.</p><p>Un site professionnel bien référencé, c'est un commercial qui travaille 24h/24 et 7j/7, sans charges sociales. Chez Digital Dreamsbox, on construit ce type de site pour les artisans et PME du Grand Est.</p>"
            }
        ],
        "blockquote": "\"Les PME qui investissent dans un site web professionnel génèrent en moyenne 39% de chiffre d'affaires supplémentaire sur 3 ans.\" (Étude Deloitte, Digital maturity & SMB growth)",
        "cta_title": "Quel budget pour votre projet ?",
        "cta_text": "On vous donne une estimation claire et transparente pour votre site, adaptée à votre activité et vos objectifs. Sans engagement et sans surprise.",
        "faq": [
            {"q": "Existe-t-il des aides pour financer la création d'un site web pour un artisan ?", "a": "Oui. Le chèque numérique France Num peut couvrir jusqu'à 500 euros de dépenses numériques pour les TPE. Certaines régions proposent aussi des aides spécifiques. En Moselle et Grand Est, rapprochez-vous de votre CMA ou de la CCI pour connaître les dispositifs disponibles."},
            {"q": "Un site web à 300 euros peut-il vraiment fonctionner ?", "a": "Visuellement oui, commercialement rarement. Un site à 300 euros est généralement réalisé sans travail SEO, sans optimisation mobile approfondie et sans stratégie de conversion. Il peut exister, mais il ne génèrera probablement aucun contact depuis Google. Le coût réel, c'est le manque à gagner."},
            {"q": "Faut-il payer une maintenance mensuelle après la création ?", "a": "Ce n'est pas obligatoire mais recommandé pour les sites sous WordPress (mises à jour de sécurité, sauvegardes). Prévoyez entre 30 et 80 euros par mois si vous souhaitez une maintenance complète. Si votre site est statique (HTML/CSS), la maintenance est quasi nulle."}
        ],
        "related": [
            {"slug": "site-web-artisan-2026", "title": "Pourquoi un site web reste indispensable pour un artisan en 2026"},
            {"slug": "site-web-qui-convertit", "title": "Pourquoi votre site web ne génère pas de contacts"}
        ]
    },
    "seo-local-sans-agence": {
        "meta_description": "6 actions SEO local gratuites qu'un artisan peut faire seul ce week-end pour améliorer son référencement Google et décrocher plus d'appels.",
        "og_description": "6 actions SEO local gratuites à faire seul ce week-end pour apparaître plus souvent dans Google.",
        "lede": "Le référencement local n'est pas réservé aux grandes entreprises avec budget marketing. Six actions gratuites peuvent changer votre visibilité dès ce week-end.",
        "excerpt": "Six actions SEO local gratuites à faire seul ce week-end pour décrocher plus d'appels entrants.",
        "sommaire": [
            "Action 1 : compléter et vérifier votre fiche Google Business",
            "Action 2 : ajouter vos mots-clés locaux sur votre site",
            "Action 3 : créer des pages par zone géographique",
            "Action 4 : soumettre votre site aux annuaires locaux",
            "Action 5 : optimiser vos balises title et meta description",
            "Action 6 : activer et configurer Google Search Console"
        ],
        "sections": [
            {
                "h2": "Action 1 : compléter et vérifier votre fiche Google Business",
                "html": "<p>Si vous n'avez pas encore de fiche Google Business Profile, créez-la en premier. C'est la base. Si vous en avez une, vérifiez qu'elle est complète à 100% : catégories, zones desservies, horaires, description, photos.</p><p>Ajoutez vos services un par un dans l'onglet \"Services\" de votre fiche. Chaque service listé est un mot-clé supplémentaire que Google peut associer à votre fiche. Un plombier qui liste \"débouchage\", \"installation chauffe-eau\", \"détection de fuite\" et \"plomberie sanitaire\" apparaît sur beaucoup plus de requêtes que celui qui a juste \"plomberie\".</p>"
            },
            {
                "h2": "Action 2 : ajouter vos mots-clés locaux sur votre site",
                "html": "<p>Parcourez votre site et vérifiez que vos mots-clés locaux apparaissent naturellement dans vos textes. Exemples : \"artisan plombier à Sarrebourg\", \"intervention dans tout le Grand Est\", \"devis gratuit en Moselle\".</p><p>Chaque page de service doit mentionner la zone géographique concernée. Pas de façon artificielle et répétitive, mais naturellement, comme si vous parliez à un client de la région. Google est capable de lire et comprendre le contexte géographique de votre contenu.</p>"
            },
            {
                "h2": "Action 3 : créer des pages par zone géographique",
                "html": "<p>Si vous intervenez dans plusieurs communes, créez une page dédiée par commune principale. Une page \"Plombier Phalsbourg\", une page \"Plombier Sarreguemines\", une page \"Plombier Sarrebourg\".</p><p>Chaque page doit avoir un contenu distinct et utile : spécificités locales, types de chantiers courants dans cette zone, exemples de réalisations. Pas du copier-coller avec juste le nom de la ville changé. Google détecte le contenu dupliqué et le pénalise.</p><p>Ces pages peuvent chacune se positionner sur des requêtes locales ciblées et multiplier votre surface de capture sur Google.</p>"
            },
            {
                "h2": "Action 4 : soumettre votre site aux annuaires locaux",
                "html": "<p>Les liens entrants depuis d'autres sites renforcent votre autorité SEO. Les annuaires locaux sont des sources de liens faciles et pertinentes :</p><ul><li>Pages Jaunes (pagesjaunes.fr)</li><li>Yelp</li><li>Chambre des Métiers de la Moselle (cma-moselle.fr)</li><li>Kompass</li><li>L'annuaire du Grand Est si disponible dans votre secteur</li></ul><p>Assurez-vous que votre nom, adresse et numéro de téléphone sont identiques partout (NAP consistency). Des informations incohérentes entre les annuaires nuisent à votre référencement local.</p>"
            },
            {
                "h2": "Action 5 : optimiser vos balises title et meta description",
                "html": "<p>Ce sont les textes qui apparaissent dans les résultats Google. Ils influencent le taux de clic, pas directement le classement, mais indirectement via le comportement des utilisateurs.</p><p>Pour chaque page, votre balise title doit contenir votre mot-clé principal et votre localisation. Exemple : \"Plombier Sarrebourg | Intervention rapide | Nom de votre entreprise\". La meta description doit donner envie de cliquer en 155 caractères : ce que vous faites, votre zone, votre différence.</p>"
            },
            {
                "h2": "Action 6 : activer et configurer Google Search Console",
                "html": "<p>Google Search Console est gratuit et indispensable. Il vous montre sur quelles requêtes votre site apparaît, quelles pages sont indexées, et si Google rencontre des problèmes techniques.</p><p>Pour l'activer : allez sur search.google.com/search-console, ajoutez votre site, et vérifiez la propriété via Google Analytics ou un fichier HTML. Soumettez ensuite votre sitemap (souvent accessible à votresite.fr/sitemap.xml).</p><p>Consultez Search Console une fois par mois. Les données de clics et d'impressions vous diront exactement sur quelles requêtes vous progressez et lesquelles méritent plus d'effort. C'est votre tableau de bord SEO gratuit.</p>"
            }
        ],
        "blockquote": "\"46% de toutes les recherches Google ont une intention locale.\" (Google Internal Data)",
        "cta_title": "On va plus loin ensemble ?",
        "cta_text": "Ces 6 actions sont un bon début. Pour un référencement complet et durable, notre équipe prend en charge votre SEO local de A à Z. Demandez un audit gratuit.",
        "faq": [
            {"q": "Le SEO local est-il vraiment gratuit pour un artisan ?", "a": "Les actions de base sont gratuites : optimiser votre fiche Google Business, collecter des avis, améliorer vos textes. En revanche, le temps est un coût réel. Si vous ne pouvez pas y consacrer 2 à 3 heures par mois, déléguer à une agence peut être plus rentable."},
            {"q": "Combien de temps faut-il attendre pour voir des résultats en SEO local ?", "a": "Les premières améliorations (meilleur classement local, plus d'appels) se voient généralement en 2 à 4 mois si vous appliquez plusieurs actions simultanément. Le SEO est un investissement progressif : les résultats s'accumulent et durent, contrairement à la publicité payante."},
            {"q": "Peut-on faire son SEO local sans agence ni expert ?", "a": "Oui, pour les bases. Un artisan motivé peut améliorer significativement sa visibilité locale en 3 mois en suivant les 6 actions de cet article. Pour aller plus loin (pages locales, netlinking, audit technique), l'aide d'un professionnel accélère les résultats."}
        ],
        "related": [
            {"slug": "vitrine-google-maps-artisan", "title": "Google Maps pour artisans : apparaître en premier dans votre ville"},
            {"slug": "avis-google-comment-en-obtenir", "title": "Avis Google : comment en obtenir plus sans y passer des heures"}
        ]
    },
    "identite-visuelle-pme": {
        "meta_description": "Logo, couleurs, typographie : votre identité visuelle dit tout de votre sérieux avant même que vous parliez. Voici pourquoi et comment construire une image qui convainc.",
        "og_description": "Identité visuelle PME : la différence entre un logo fait vite et une image de marque qui génère de la confiance.",
        "lede": "Un client vous voit pour la première fois : votre logo sur un devis, votre site, votre véhicule. En 3 secondes, il se forge une opinion. Votre identité visuelle décide pour lui.",
        "excerpt": "Logo, couleurs, typo : votre identité visuelle dit tout de votre sérieux avant que vous parliez. Voici comment construire une image forte.",
        "sommaire": [
            "Ce qu'une identité visuelle dit (et ne dit pas) de vous",
            "Logo : les erreurs courantes chez les PME",
            "Couleurs et typographie : les choix qui renforcent la confiance",
            "Appliquer son identité sur tous les supports",
            "Investir dans son image : ce que ça change concrètement"
        ],
        "sections": [
            {
                "h2": "Ce qu'une identité visuelle dit (et ne dit pas) de vous",
                "html": "<p>Votre identité visuelle, c'est l'ensemble des éléments graphiques qui vous représentent : logo, palette de couleurs, typographies, style photographique. Ce n'est pas qu'une question d'esthétique. C'est une question de confiance.</p><p>Une identité visuelle professionnelle dit : \"nous sommes sérieux, organisés, et nous resterons là si quelque chose se passe mal.\" Une identité approximative dit le contraire, même si votre travail est excellent.</p><p>Pour une PME en Moselle qui cherche à se différencier, l'identité visuelle est souvent le premier critère de sélection inconscient d'un prospect. Avant le prix. Avant la réputation.</p>"
            },
            {
                "h2": "Logo : les erreurs courantes chez les PME",
                "html": "<p>Les logos problématiques ont presque toujours les mêmes défauts :</p><ul><li><strong>Trop complexe :</strong> un logo avec cinq couleurs, des dégradés et un texte illisible en petit format. Sur un tampon ou une carte de visite, il devient illisible.</li><li><strong>Police générique :</strong> Comic Sans, Times New Roman ou Arial sur un logo, ça communique une chose : aucun soin n'a été apporté à l'image de l'entreprise.</li><li><strong>Clipart ou banque d'image :</strong> utiliser une icône téléchargée gratuitement que dix autres entreprises dans votre secteur utilisent aussi.</li><li><strong>Logo non vectoriel :</strong> un logo en JPEG qui se pixelise à l'impression. Un vrai logo doit exister en format vectoriel (SVG, AI, EPS) pour être utilisable à toutes les tailles.</li></ul>"
            },
            {
                "h2": "Couleurs et typographie : les choix qui renforcent la confiance",
                "html": "<p>Les couleurs ne sont pas neutres. Elles transmettent des valeurs :</p><ul><li><strong>Bleu :</strong> confiance, sérieux, stabilité. Très utilisé dans les services, la finance, l'artisanat de qualité.</li><li><strong>Vert :</strong> nature, santé, durabilité. Pertinent pour les métiers liés à l'environnement, l'agriculture, l'éco-construction.</li><li><strong>Noir et blanc :</strong> élégance, premium, intemporel. Efficace pour les métiers de luxe ou les services haut de gamme.</li><li><strong>Orange et jaune :</strong> énergie, dynamisme, accessibilité. Attention à ne pas paraître cheap si mal utilisés.</li></ul><p>Pour la typographie : deux polices maximum. Une pour les titres (avec caractère), une pour le texte courant (lisible, neutre). La cohérence entre tous vos supports est plus importante que le choix des polices en lui-même.</p>"
            },
            {
                "h2": "Appliquer son identité sur tous les supports",
                "html": "<p>Une identité visuelle forte est cohérente partout. Sur votre site web, vos devis, vos factures, vos cartes de visite, votre véhicule, vos réseaux sociaux, vos tenues de travail si vous en avez.</p><p>Cette cohérence crée ce qu'on appelle la <strong>reconnaissance de marque</strong>. Au bout de quelques rencontres avec votre identité visuelle, un prospect commence à vous associer inconsciemment à votre domaine d'activité dans sa zone. Quand il a besoin de votre service, votre nom vient en premier.</p><p>Pour appliquer votre charte graphique simplement, créez des modèles (templates) dans Canva pour vos publications réseaux, vos devis et vos cartes de visite. Une heure de setup, et vous pouvez produire des supports cohérents en quelques minutes.</p>"
            },
            {
                "h2": "Investir dans son image : ce que ça change concrètement",
                "html": "<p>Le retour d'un investissement en identité visuelle est difficile à mesurer précisément, mais ses effets sont tangibles. Les PME qui soignent leur image :</p><ul><li>Justifient des tarifs plus élevés (l'image premium légitime le prix premium).</li><li>Gagnent en confiance dans leurs échanges commerciaux.</li><li>Sont perçues comme plus stables et fiables par les nouveaux prospects.</li><li>Fidélisent mieux leurs clients existants qui sont fiers de travailler avec une entreprise qui a de l'allure.</li></ul><p>Un budget identité visuelle complète (logo, charte, déclinaisons) pour une PME locale se situe entre 500 et 2 000 euros selon la complexité. C'est un investissement ponctuel qui travaille pour vous pendant des années.</p>"
            }
        ],
        "blockquote": "\"Il faut 0,05 seconde aux utilisateurs pour se forger une opinion sur votre site et donc sur votre entreprise.\" (Étude Google / Université de Bâle)",
        "cta_title": "Votre image reflète-t-elle votre vraie valeur ?",
        "cta_text": "On réalise un audit visuel gratuit de votre identité actuelle et on vous dit ce qui peut être amélioré pour renforcer la confiance de vos prospects.",
        "faq": [
            {"q": "Quelle est la différence entre un logo et une identité visuelle ?", "a": "Le logo est un élément de l'identité visuelle, pas l'identité visuelle entière. Une identité visuelle complète comprend le logo, une palette de couleurs définie, une ou deux typographies cohérentes, un style photographique et des règles d'utilisation sur tous les supports. Le logo seul ne suffit pas à créer une image mémorable."},
            {"q": "Combien coûte une identité visuelle complète pour une PME ou un artisan ?", "a": "Entre 500 et 2 000 euros pour une identité professionnelle complète (logo, charte, déclinaisons). En dessous de 500 euros, attendez-vous à un logo simple sans charte complète. Les plateformes comme Canva permettent de faire quelque chose de convenable gratuitement, mais sans l'originalité d'une création sur-mesure."},
            {"q": "Peut-on faire son identité visuelle soi-même avec Canva ?", "a": "Oui, pour démarrer. Canva propose des modèles professionnels accessibles sans compétences en design. La limite : vous utilisez les mêmes modèles que des milliers d'autres entreprises. Pour vous démarquer vraiment, une identité sur-mesure créée par un professionnel est plus efficace à long terme."}
        ],
        "related": [
            {"slug": "branding-artisan-moselle", "title": "Branding pour artisans en Moselle : construire une image qui rassure"},
            {"slug": "site-web-artisan-2026", "title": "Pourquoi un site web reste indispensable pour un artisan en 2026"}
        ]
    },
    "google-ads-budget-minimum": {
        "meta_description": "Google Ads pour artisan en Grand Est : quel budget minimum pour que ça soit rentable ? Les vrais chiffres et la bonne stratégie pour démarrer.",
        "og_description": "Google Ads artisan Grand Est : quel budget minimum, quels résultats attendre, et comment éviter de gaspiller.",
        "lede": "Google Ads peut générer des appels en 48 heures. Mais avec un budget mal calibré ou une campagne mal configurée, c'est aussi la façon la plus rapide de perdre de l'argent.",
        "excerpt": "Google Ads pour artisan dans le Grand Est : quel budget minimum pour être rentable et comment ne pas gaspiller.",
        "sommaire": [
            "Comment fonctionne Google Ads pour un artisan local",
            "Le budget minimum pour avoir des résultats réels",
            "Les types de campagnes adaptées aux artisans",
            "Ce qui fait échouer la majorité des campagnes",
            "Gérer soi-même ou confier à une agence : le bon calcul"
        ],
        "sections": [
            {
                "h2": "Comment fonctionne Google Ads pour un artisan local",
                "html": "<p>Google Ads vous permet d'afficher votre entreprise en haut des résultats de recherche pour des mots-clés précis. Vous ne payez que quand quelqu'un clique sur votre annonce.</p><p>Pour un artisan, les campagnes les plus efficaces ciblent des requêtes avec intention d'achat immédiate : \"plombier urgence Sarrebourg\", \"couvreur devis Moselle\", \"électricien intervention rapide Grand Est\". Ces requêtes signifient que la personne a un besoin maintenant et cherche à appeler rapidement.</p>"
            },
            {
                "h2": "Le budget minimum pour avoir des résultats réels",
                "html": "<p>En Moselle et dans le Grand Est, les coûts par clic pour les métiers du bâtiment et des services se situent généralement entre <strong>1,50 et 5 euros par clic</strong> selon la concurrence et la spécialité.</p><p>Pour obtenir des données significatives et commencer à générer des appels, un budget minimum de <strong>300 à 500 euros par mois</strong> est recommandé. En dessous, vous n'aurez pas assez de volume pour optimiser les campagnes.</p><p>Avec 400 euros/mois, à 2,50 euros le clic en moyenne, vous obtenez environ 160 clics. Si votre site convertit à 10% (ce qui est réaliste pour un artisan local bien présenté), c'est 16 demandes de devis mensuelles. Avec un taux de transformation de 30%, ça fait 5 nouveaux clients par mois.</p>"
            },
            {
                "h2": "Les types de campagnes adaptées aux artisans",
                "html": "<p>Trois formats sont particulièrement adaptés aux artisans et PME locales :</p><ul><li><strong>Annonces de recherche classiques :</strong> votre annonce texte apparaît quand quelqu'un tape vos mots-clés. Le format le plus efficace pour les demandes avec intention d'achat forte.</li><li><strong>Annonces d'appel :</strong> une annonce qui affiche directement un bouton \"Appeler\" sur mobile. Idéal pour les urgences (plomberie, serrurerie, électricité).</li><li><strong>Local Services Ads (Annonces de services locaux) :</strong> disponibles pour certains métiers, ces annonces affichent votre badge \"Certifié Google\" et génèrent des leads qualifiés. Vous ne payez que pour les contacts réels, pas les clics.</li></ul>"
            },
            {
                "h2": "Ce qui fait échouer la majorité des campagnes",
                "html": "<p>Les erreurs classiques qui font brûler le budget sans résultat :</p><ul><li><strong>Ciblage géographique trop large :</strong> cibler toute l'Alsace-Moselle quand vous intervenez uniquement dans un rayon de 30 km.</li><li><strong>Mots-clés trop génériques :</strong> enchérir sur \"plombier\" (très concurrentiel, intention floue) plutôt que \"débouchage évier urgence Sarrebourg\" (plus précis, moins cher, plus qualifié).</li><li><strong>Page de destination inadaptée :</strong> envoyer les clics sur votre page d'accueil générale plutôt qu'une page dédiée au service annoncé.</li><li><strong>Absence de mots-clés négatifs :</strong> sans liste de mots-clés à exclure, vous payez pour des clics de personnes qui cherchent du travail ou des cours de plomberie.</li></ul>"
            },
            {
                "h2": "Gérer soi-même ou confier à une agence : le bon calcul",
                "html": "<p>Google Ads est techniquement accessible à tous, mais l'optimisation demande du temps et de l'expertise. Une campagne mal gérée peut facilement gaspiller 50% du budget.</p><p>Si vous gérez vous-même : comptez 3 à 5 heures par mois minimum pour analyser les données, ajuster les enchères et affiner les mots-clés. Google propose des formations gratuites via Google Skillshop.</p><p>Si vous confiez à une agence locale : prévoyez entre 200 et 400 euros/mois de frais de gestion en plus du budget publicitaire. C'est rentable si l'agence fait passer votre coût par lead de 50 euros à 20 euros. Demandez toujours à voir les résultats des campagnes en accès direct, pas seulement un rapport mensuel.</p>"
            }
        ],
        "blockquote": "\"Les annonces Google génèrent en moyenne 2 euros de revenu pour chaque euro dépensé.\" (Google Economic Impact Report)",
        "cta_title": "On calcule votre potentiel Google Ads ?",
        "cta_text": "On estime votre coût par lead et votre potentiel de retour sur investissement selon votre activité et votre zone. Gratuit, sans engagement, en 48h.",
        "faq": [
            {"q": "Peut-on faire Google Ads avec seulement 100 euros par mois ?", "a": "Techniquement oui, mais les résultats seront très limités. Avec 100 euros, vous obtenez environ 40 à 60 clics par mois selon votre secteur. C'est insuffisant pour optimiser les campagnes et générer un flux régulier de contacts. Le seuil minimal efficace pour un artisan local est de 300 euros par mois."},
            {"q": "Google Ads ou SEO : que choisir en priorité pour un artisan ?", "a": "Les deux ont leur rôle. Google Ads donne des résultats immédiats mais s'arrête quand vous stoppez le budget. Le SEO est plus lent mais génère du trafic durable et gratuit. La stratégie idéale : commencer par Google Ads pour générer des contacts rapidement, et investir en parallèle dans le SEO pour réduire progressivement votre dépendance à la publicité."},
            {"q": "Faut-il confier la gestion de ses Google Ads à un professionnel ?", "a": "Pour un budget de 300 euros ou plus par mois, oui. Une campagne mal gérée peut gaspiller 50% du budget. Un professionnel identifie les mots-clés pertinents, exclut les requêtes inutiles et optimise les enchères. Les frais de gestion (150 à 300 euros/mois) sont souvent rentabilisés dès le premier mois grâce aux économies réalisées."}
        ],
        "related": [
            {"slug": "seo-local-sans-agence", "title": "SEO local : 6 actions gratuites qu'un artisan peut faire seul"},
            {"slug": "site-web-qui-convertit", "title": "Pourquoi votre site web ne génère pas de contacts"}
        ]
    },
    "site-web-qui-convertit": {
        "meta_description": "Votre site reçoit des visites mais génère peu de contacts ? Voici les 5 raisons les plus fréquentes et comment les corriger pour transformer vos visiteurs en clients.",
        "og_description": "Pourquoi votre site ne génère pas de contacts et comment corriger ça : les 5 raisons les plus fréquentes.",
        "lede": "Un site avec du trafic qui ne génère pas d'appels, c'est une vitrine fermée. Le problème n'est presque jamais le trafic : c'est ce qui se passe une fois que le visiteur arrive.",
        "excerpt": "Votre site a du trafic mais pas de contacts ? Voici les 5 raisons et comment les corriger rapidement.",
        "sommaire": [
            "Raison 1 : votre proposition de valeur n'est pas claire",
            "Raison 2 : votre site est difficile à utiliser sur mobile",
            "Raison 3 : vos appels à l'action sont invisibles",
            "Raison 4 : votre site ne rassure pas assez",
            "Raison 5 : votre formulaire est trop long ou trop compliqué"
        ],
        "sections": [
            {
                "h2": "Raison 1 : votre proposition de valeur n'est pas claire",
                "html": "<p>Dans les premières secondes sur votre site, un visiteur doit comprendre instantanément : ce que vous faites, pour qui, et dans quelle zone. Si c'est flou ou trop générique, il repart.</p><p>Testez votre propre site : quelqu'un qui ne vous connaît pas peut-il comprendre en 5 secondes que vous êtes un électricien qui intervient à Sarrebourg et ses environs ? Si votre page d'accueil commence par \"Bienvenue sur notre site\" ou une phrase creuse, vous perdez des prospects dès l'arrivée.</p><p>La correction : un titre de page d'accueil direct et géolocalisé, visible sans scroller. \"Électricien à Sarrebourg. Devis gratuit sous 24h.\" C'est suffisant.</p>"
            },
            {
                "h2": "Raison 2 : votre site est difficile à utiliser sur mobile",
                "html": "<p>Plus de 70% des recherches locales se font sur smartphone. Si votre site n'est pas optimisé mobile, vous perdez la majorité de vos prospects dès le chargement.</p><p>Les problèmes courants : texte trop petit à lire sans zoomer, boutons trop petits à cliquer, images qui débordent de l'écran, formulaires difficiles à remplir au doigt.</p><p>Testez votre site sur votre téléphone maintenant. Si vous devez zoomer ou scroller horizontalement, votre site perd des clients quotidiennement. Google pénalise aussi les sites non adaptés au mobile dans ses résultats de recherche.</p>"
            },
            {
                "h2": "Raison 3 : vos appels à l'action sont invisibles",
                "html": "<p>Un appel à l'action (CTA), c'est le bouton ou le lien qui guide le visiteur vers la prochaine étape : appeler, demander un devis, envoyer un message. Si ce bouton n'est pas visible sans scroller sur toutes les pages, vous perdez des conversions.</p><p>Les bonnes pratiques : un bouton \"Appeler\" ou \"Demander un devis\" visible en haut de chaque page, une couleur contrastée qui le fait ressortir, et un texte d'action clair (\"Demander un devis gratuit\" plutôt que juste \"Contact\").</p><p>Sur mobile, le numéro de téléphone doit être cliquable directement. Vérifiez que votre numéro est affiché en format \"tel:\" dans le code de votre site.</p>"
            },
            {
                "h2": "Raison 4 : votre site ne rassure pas assez",
                "html": "<p>Un prospect qui ne vous connaît pas cherche des preuves que vous êtes fiable avant de vous confier un chantier. Votre site doit fournir ces preuves :</p><ul><li>Photos de réalisations réelles (pas de stock photos).</li><li>Avis clients visibles sur le site, pas seulement sur Google.</li><li>Certifications et labels (RGE, Qualibat, assurance décennale mentionnée).</li><li>Années d'expérience, nombre de chantiers réalisés si impressionnant.</li><li>Photo de vous ou de votre équipe : les clients font confiance à des visages, pas à des logos.</li></ul><p>Chaque élément de réassurance réduit la résistance à l'action et augmente le taux de conversion.</p>"
            },
            {
                "h2": "Raison 5 : votre formulaire est trop long ou trop compliqué",
                "html": "<p>Chaque champ supplémentaire dans un formulaire réduit les conversions. Pour un premier contact, vous n'avez besoin que de trois informations : nom, téléphone ou email, et une brève description du besoin.</p><p>Ne demandez pas : numéro SIRET, adresse complète, date de naissance ou téléphone fixe ET portable. Ces informations, vous les obtiendrez lors de l'échange téléphonique. Ne bloquez pas le premier contact avec des exigences qui découragent.</p><p>Alternative au formulaire : proposez aussi un bouton d'appel direct et, si vous utilisez WhatsApp pour votre activité, un lien WhatsApp. Plus vous facilitez le premier contact, plus vous recevez de demandes.</p>"
            }
        ],
        "blockquote": "\"Un site bien optimisé pour la conversion peut générer 3 fois plus de contacts avec le même trafic.\" (Baymard Institute, UX Research)",
        "cta_title": "On diagnostique votre site gratuitement ?",
        "cta_text": "On identifie exactement ce qui freine vos conversions et on vous propose les corrections prioritaires. Audit offert, résultat en 48h.",
        "faq": [
            {"q": "Comment savoir si mon site génère vraiment des contacts ?", "a": "Installez Google Analytics 4 (gratuit) et activez le suivi des conversions : soumission de formulaire, clic sur le numéro de téléphone. Google Business Profile indique aussi les appels générés directement depuis votre fiche. Sans ces mesures, vous pilotez à l'aveugle."},
            {"q": "Mon site est beau mais ne génère pas d'appels. Pourquoi ?", "a": "Un site esthétique et un site qui convertit sont deux choses différentes. Les causes les plus fréquentes : pas assez de boutons d'appel visibles, proposition de valeur floue, formulaire trop long, pas de preuve sociale (avis, photos de chantiers), ou site trop lent sur mobile. Un audit de conversion identifie le problème exact."},
            {"q": "Quel taux de conversion est normal pour un site artisan ?", "a": "Entre 3% et 8% des visiteurs en contact direct est un bon objectif pour un site artisan local. En dessous de 2%, il y a clairement un problème de conversion à résoudre. Au-dessus de 10%, votre site est excellent. Ces chiffres varient selon le secteur et la qualité du trafic entrant."}
        ],
        "related": [
            {"slug": "refonte-site-web-quand", "title": "Refonte de site web : les 5 signes qu'il est temps de tout recommencer"},
            {"slug": "budget-site-web-artisan", "title": "Combien coûte un vrai site web pour un artisan en 2026"}
        ]
    },
    "branding-artisan-moselle": {
        "meta_description": "Construire une image de marque forte en Moselle quand on est artisan : pourquoi c'est possible, comment commencer, et ce que ça change sur vos tarifs et votre clientèle.",
        "og_description": "Branding artisan en Moselle : comment construire une image forte qui justifie des tarifs plus élevés et attire de meilleurs clients.",
        "lede": "Le branding n'est pas réservé aux grandes marques. Un artisan avec une image forte en Moselle attire des clients qui ne discutent pas le prix. Voici comment y arriver.",
        "excerpt": "Un artisan avec une image forte attire de meilleurs clients et justifie des tarifs plus élevés. Voici comment construire ce capital en Moselle.",
        "sommaire": [
            "Pourquoi le branding change la relation avec vos clients",
            "Les 3 piliers d'une image forte pour un artisan",
            "Votre histoire : l'atout que vous sous-estimez",
            "Construire sa réputation localement, étape par étape",
            "Ce que le branding change concrètement sur vos tarifs"
        ],
        "sections": [
            {
                "h2": "Pourquoi le branding change la relation avec vos clients",
                "html": "<p>Un artisan sans image de marque définie est perçu comme interchangeable. Un client va comparer uniquement sur le prix parce qu'il n'a pas d'autre critère de différenciation. C'est la position la plus inconfortable : vous êtes toujours en compétition sur le moins cher.</p><p>Un artisan avec une image forte, une identité visuelle cohérente et une réputation locale établie est perçu différemment. Les clients qui viennent vers lui savent déjà qu'il est sérieux et ne cherchent pas à négocier. Ils cherchent à travailler avec lui spécifiquement.</p>"
            },
            {
                "h2": "Les 3 piliers d'une image forte pour un artisan",
                "html": "<p>Pas besoin d'un budget marketing de grande entreprise. Pour un artisan en Moselle, trois éléments suffisent à construire une image forte :</p><ul><li><strong>Une identité visuelle cohérente :</strong> logo professionnel, couleurs définies, typographie uniforme sur tous les supports. Devis, site, réseaux, véhicule. La cohérence crée la reconnaissance.</li><li><strong>Un positionnement clair :</strong> en quoi êtes-vous différent des dix autres artisans de votre métier dans le secteur ? Rapidité d'intervention, spécialité précise, garantie étendue, approche écologique ? Choisissez un angle et tenez-le.</li><li><strong>Une présence locale visible :</strong> fiche Google optimisée, réseaux sociaux actifs, témoignages clients récents. La réputation locale se construit par accumulation.</li></ul>"
            },
            {
                "h2": "Votre histoire : l'atout que vous sous-estimez",
                "html": "<p>Chaque artisan a une histoire : pourquoi ce métier, depuis quand, ce qui vous distingue dans la façon de travailler. Cette histoire est un outil de branding puissant que la plupart n'utilisent jamais.</p><p>Les clients achètent à des personnes avant d'acheter des services. Une page \"À propos\" bien rédigée, une vidéo de 60 secondes de présentation, quelques posts sur vos débuts et votre parcours : ces contenus créent un lien émotionnel que le concurrent avec le prix le plus bas ne peut pas reproduire.</p><p>\"Artisan charpentier à Sarrebourg depuis 20 ans, j'ai appris le métier avec mon père\" est infiniment plus engageant que \"Notre entreprise est spécialisée dans les travaux de charpente\".</p>"
            },
            {
                "h2": "Construire sa réputation localement, étape par étape",
                "html": "<p>La réputation locale se construit avec de la régularité, pas avec un grand coup marketing. Voici ce qui fonctionne :</p><ul><li>Demandez un avis Google à chaque client satisfait, systématiquement.</li><li>Publiez des photos de chantiers sur Facebook ou Instagram une à deux fois par semaine.</li><li>Participez aux groupes Facebook locaux. Répondez aux questions dans votre domaine sans chercher à vendre directement.</li><li>Sponsorisez un événement local ou une équipe sportive si votre budget le permet. La visibilité locale vaut souvent plus que de la publicité en ligne.</li></ul><p>En 12 mois de régularité sur ces quatre points, votre nom devient une référence dans votre commune et ses alentours.</p>"
            },
            {
                "h2": "Ce que le branding change concrètement sur vos tarifs",
                "html": "<p>La conséquence la plus concrète d'une image forte : vous pouvez facturer 15 à 30% plus cher que vos concurrents sans image, pour le même travail. Parce que les clients perçoivent plus de valeur et cherchent moins à négocier.</p><p>Ce n'est pas de la manipulation. C'est que votre image forte communique des informations réelles : sérieux, expérience, fiabilité, pérennité. Ces informations ont une valeur réelle pour un client qui cherche quelqu'un à qui faire confiance pour rénover sa maison.</p><p>Investir 1 500 euros dans une identité visuelle professionnelle, une fiche Google optimisée et une présence réseaux cohérente peut vous permettre d'augmenter vos tarifs de 10%, ce qui, sur un chiffre d'affaires de 150 000 euros, représente 15 000 euros supplémentaires par an.</p>"
            }
        ],
        "blockquote": "\"Les entreprises avec une image de marque forte génèrent en moyenne 23% de revenus supplémentaires.\" (Forbes Brand Consistency Report)",
        "cta_title": "On construit votre image ensemble ?",
        "cta_text": "Audit de votre identité actuelle, recommandations concrètes, plan d'action. On commence par un échange gratuit de 30 minutes.",
        "faq": [
            {"q": "Le branding est-il vraiment utile pour un artisan local en Moselle ?", "a": "Oui, et souvent plus qu'il ne le pense. En Moselle, les artisans sont nombreux dans tous les corps de métier. Un artisan avec une image forte, cohérente et professionnelle se distingue immédiatement de la concurrence et peut pratiquer des tarifs 10 à 20% plus élevés sans perdre de clients."},
            {"q": "Comment se différencier de la concurrence artisanale dans le Grand Est ?", "a": "Choisissez un angle précis : spécialité technique (renovation énergétique, matériaux écologiques), engagement (devis sous 24h, garantie étendue), ou territoire (artisan 100% local de Sarrebourg). Un positionnement clair, même simple, vaut mieux qu'une communication générique qui dit la même chose que tout le monde."},
            {"q": "Peut-on construire une vraie image de marque sans gros budget ?", "a": "Oui, avec de la régularité et de la cohérence. Un logo professionnel (300 à 600 euros), un site soigné, des photos de qualité de vos chantiers et une présence réseaux régulière : c'est suffisant pour construire une image forte localement. Le secret n'est pas le budget, c'est la constance."}
        ],
        "related": [
            {"slug": "identite-visuelle-pme", "title": "Identité visuelle pour PME : la différence entre paraître et convaincre"},
            {"slug": "prospection-digitale-locale", "title": "Prospection digitale : trouver des clients locaux sans démarchage"}
        ]
    },
    "prospection-digitale-locale": {
        "meta_description": "Trouver des clients locaux sans démarchage téléphonique ni porte-à-porte : les méthodes digitales qui fonctionnent pour les artisans et PME en Moselle.",
        "og_description": "Prospection digitale locale : comment trouver des clients sans démarchage agressif grâce aux bons outils.",
        "lede": "Le démarchage téléphonique agace et le porte-à-porte prend du temps. Le digital permet de prospecter de façon intelligente, en attirant les clients au lieu de les chasser.",
        "excerpt": "Trouver des clients locaux sans démarchage : les méthodes digitales qui fonctionnent pour artisans et PME en Moselle.",
        "sommaire": [
            "L'inbound vs l'outbound : pourquoi attirer plutôt que chasser",
            "Les groupes Facebook locaux : un vivier de prospects",
            "LinkedIn pour trouver des clients professionnels",
            "Le partenariat avec d'autres artisans locaux",
            "Construire un flux régulier de prospects sans y passer ses soirées"
        ],
        "sections": [
            {
                "h2": "L'inbound vs l'outbound : pourquoi attirer plutôt que chasser",
                "html": "<p>La prospection traditionnelle (appels à froid, démarchage, distribution de flyers) repose sur le volume : vous contactez 100 personnes pour en convaincre 2. C'est épuisant et souvent inefficace pour une PME avec peu de temps disponible.</p><p>La prospection digitale inbound fonctionne à l'inverse : vous créez du contenu utile ou une présence visible, et les prospects viennent vers vous quand ils ont besoin de votre service. Le temps investi en amont génère des résultats dans la durée.</p><p>Concrètement : un artisan avec une fiche Google optimisée, 80 avis positifs et un site bien référencé reçoit des appels entrants sans prospecter activement. C'est l'objectif à atteindre.</p>"
            },
            {
                "h2": "Les groupes Facebook locaux : un vivier de prospects",
                "html": "<p>Dans la plupart des communes de Moselle et du Grand Est, il existe des groupes Facebook locaux actifs. \"Bon plan Sarrebourg\", \"Entraide Sarreguemines\", \"Que faire à Phalsbourg\"... Ces groupes regroupent des milliers de résidents qui y posent régulièrement des questions du type \"quelqu'un connaît un bon plombier dans le coin ?\".</p><p>Stratégie simple : rejoignez ces groupes avec votre profil personnel ou une page entreprise. Répondez aux questions dans votre domaine sans chercher à vendre directement. Quand quelqu'un demande une recommandation dans votre métier, d'autres membres peuvent citer votre nom.</p><p>Ne spammez pas ces groupes avec des publicités. Les publications promotionnelles non sollicitées sont souvent supprimées et nuisent à votre image.</p>"
            },
            {
                "h2": "LinkedIn pour trouver des clients professionnels",
                "html": "<p>Si vous travaillez avec des entreprises, des collectivités ou des professionnels, LinkedIn est un outil de prospection très efficace. Le principe : vous connectez avec des responsables d'entreprises, des gérants d'immeubles, des directeurs techniques dans votre zone géographique, et vous construisez progressivement votre réseau.</p><p>Sur LinkedIn, le contenu qui fonctionne pour un artisan ou une PME B2B : des études de cas (\"voici comment on a réalisé X pour Y en Z semaines\"), des conseils préventifs (\"comment éviter les problèmes de X avant l'hiver\"), et des partages d'actualités de votre secteur avec votre opinion.</p><p>Deux à trois posts par semaine et des interactions régulières suffisent pour développer un réseau qualifié en 6 mois.</p>"
            },
            {
                "h2": "Le partenariat avec d'autres artisans locaux",
                "html": "<p>L'un des canaux de prospection les plus sous-utilisés par les artisans : le partenariat entre corps de métier complémentaires. Un plombier et un carreleur se recommandent mutuellement. Un électricien et un peintre se complètent. Un menuisier et un serrurier travaillent souvent sur les mêmes chantiers.</p><p>Identifiez 5 à 10 artisans complémentaires dans votre zone, rencontrez-les (même informellement), et proposez des recommandations croisées. Chaque partenariat bien entretenu peut vous apporter 2 à 5 nouveaux clients par an sans aucune dépense marketing.</p><p>Vous pouvez formaliser ces partenariats en rejoignant le réseau de la Chambre des Métiers de la Moselle ou des associations d'artisans locaux.</p>"
            },
            {
                "h2": "Construire un flux régulier de prospects sans y passer ses soirées",
                "html": "<p>L'objectif n'est pas de consacrer des heures chaque soir à la prospection, mais de mettre en place des systèmes qui travaillent pour vous :</p><ul><li>Fiche Google optimisée et à jour : elle génère des appels 24h/24 sans intervention.</li><li>Demande d'avis systématique après chaque chantier : chaque avis renforce votre positionnement pour les semaines suivantes.</li><li>Un post par semaine sur les réseaux : 20 minutes, planifié à l'avance.</li><li>Partenariats actifs avec 3 artisans complémentaires : quelques appels par trimestre pour entretenir la relation.</li></ul><p>En 2 à 3 heures par semaine maximum, ces quatre actions combinées construisent un flux de prospects régulier qui rend le démarchage agressif inutile.</p>"
            }
        ],
        "blockquote": "\"Les leads générés par l'inbound marketing coûtent en moyenne 61% moins cher que ceux générés par l'outbound.\" (HubSpot State of Marketing Report)",
        "cta_title": "On met en place votre système de prospection ?",
        "cta_text": "On analyse votre situation actuelle et on vous propose un plan d'action personnalisé pour générer des prospects réguliers. Premier échange offert.",
        "faq": [
            {"q": "Quelle est la meilleure façon de prospecter pour un artisan local en 2026 ?", "a": "La combinaison la plus efficace : fiche Google optimisée (pour les recherches actives), présence Facebook locale (pour la recommandation), et demande d'avis systématique (pour la crédibilité). Ces trois actions combinées génèrent un flux continu de prospects sans démarchage actif."},
            {"q": "Les groupes Facebook locaux fonctionnent-ils vraiment pour trouver des clients ?", "a": "Oui, particulièrement en zone rurale et semi-urbaine comme la Moselle. Les groupes type 'Bon plan Sarrebourg' ou 'Entraide Phalsbourg' regroupent des milliers de résidents actifs. La clé est d'y être présent comme expert, pas comme vendeur : répondez aux questions, partagez des conseils, et les recommandations viendront naturellement."},
            {"q": "Combien de temps avant de voir les premiers résultats d'une prospection digitale ?", "a": "Les premiers contacts arrivent généralement en 4 à 8 semaines si vous appliquez plusieurs actions simultanément (fiche Google, réseaux, avis). La prospection digitale est un système cumulatif : chaque action renforce les autres. Au bout de 6 mois de régularité, le flux de prospects devient prévisible."}
        ],
        "related": [
            {"slug": "reseaux-sociaux-pme-moselle", "title": "Réseaux sociaux pour PME locales : ce qui marche en Moselle"},
            {"slug": "vitrine-google-maps-artisan", "title": "Google Maps pour artisans : apparaître en premier dans votre ville"}
        ]
    },
    "refonte-site-web-quand": {
        "meta_description": "Votre site web a vieilli ? Voici les 5 signes qui indiquent qu'il est temps de refondre votre site plutôt que de continuer à le rafistoler.",
        "og_description": "Les 5 signes que votre site web a besoin d'une refonte complète plutôt que de simples retouches.",
        "lede": "Rafistoler un site vieillissant coûte plus cher à long terme que de le refondre. Voici les 5 signaux d'alarme qui indiquent qu'il est temps de repartir de zéro.",
        "excerpt": "Votre site a vieilli. Voici les 5 signes concrets qui indiquent qu'une refonte complète est nécessaire.",
        "sommaire": [
            "Signe 1 : votre site n'est pas adapté au mobile",
            "Signe 2 : votre site est lent et vous le savez",
            "Signe 3 : vous ne pouvez plus le modifier vous-même",
            "Signe 4 : il ne génère aucun contact mesurable",
            "Signe 5 : votre image a évolué mais pas votre site"
        ],
        "sections": [
            {
                "h2": "Signe 1 : votre site n'est pas adapté au mobile",
                "html": "<p>Si votre site nécessite de zoomer ou de scroller horizontalement sur un téléphone, il date d'avant 2015 au plus tard. Depuis, le responsive design est un standard incontournable.</p><p>L'impact est double : côté utilisateur, c'est une expérience frustrante qui pousse à partir. Côté Google, les sites non adaptés au mobile sont pénalisés dans les résultats de recherche depuis 2015. Si votre site n'est pas responsive, il est probablement invisible pour la majorité de vos prospects potentiels.</p><p>Ce problème ne se règle pas avec des retouches CSS. Il faut reconstruire le site sur des bases modernes.</p>"
            },
            {
                "h2": "Signe 2 : votre site est lent et vous le savez",
                "html": "<p>Testez votre site sur PageSpeed Insights (pagespeed.web.dev). Si votre score mobile est en dessous de 50, votre site est clairement trop lent. Un site qui prend plus de 3 secondes à charger perd 53% de ses visiteurs mobiles avant même que la page s'affiche.</p><p>Un site lent est souvent symptomatique de problèmes structurels : mauvais hébergement, thème surchargé, images non compressées, code obsolète. Ces problèmes s'accumulent avec le temps et ne se résolvent plus avec des optimisations ponctuelles. La refonte est souvent plus rapide et moins chère que l'accumulation de rafistolages.</p>"
            },
            {
                "h2": "Signe 3 : vous ne pouvez plus le modifier vous-même",
                "html": "<p>Si vous devez appeler quelqu'un ou payer une prestation chaque fois que vous voulez changer une ligne de texte ou ajouter une photo, c'est un problème structurel. Un site moderne doit vous donner une autonomie minimale sur le contenu de base.</p><p>Cela dit, l'autonomie totale n'est pas toujours l'objectif. Certains artisans préfèrent déléguer entièrement la maintenance. Ce qui pose problème, c'est quand la modification est impossible techniquement : site construit sur une technologie abandonnée, développeur introuvable, code source perdu.</p>"
            },
            {
                "h2": "Signe 4 : il ne génère aucun contact mesurable",
                "html": "<p>Si vous ne savez pas combien de visiteurs viennent sur votre site, ni si l'un d'eux a jamais rempli votre formulaire, c'est que le suivi est absent. Et un site sans suivi est un site qu'on ne peut pas améliorer.</p><p>Si malgré un suivi en place, votre site génère zéro contact depuis des mois alors qu'il reçoit du trafic, le problème est structurel : mauvaise proposition de valeur, mauvais CTA, mauvais design de conversion. Ces problèmes se règlent rarement avec des retouches : ils nécessitent une nouvelle approche de A à Z.</p>"
            },
            {
                "h2": "Signe 5 : votre image a évolué mais pas votre site",
                "html": "<p>Votre entreprise a grandi, changé de positionnement, ajouté des services ou gagné en maturité. Mais votre site reflète encore ce que vous étiez il y a 5 ou 8 ans. Ce décalage est perçu par vos prospects, même inconsciemment.</p><p>Si vous montrez votre site à un prospect qualifié et que vous ressentez de la gêne, c'est le signal le plus clair qu'une refonte est nécessaire. Votre site doit vous représenter fièrement, pas vous faire rougir.</p><p>Une refonte bien menée n'est pas une dépense : c'est un repositionnement commercial. Un nouveau site qui reflète votre niveau actuel peut débloquer des prospects que vous n'osiez pas contacter, justifier des tarifs que vous n'osiez pas afficher, et ouvrir des marchés que vous pensiez hors de portée.</p>"
            }
        ],
        "blockquote": "\"Un site web vieillissant peut coûter jusqu'à 30% du chiffre d'affaires potentiel en prospects perdus.\" (Estimation Forrester Research, Digital Experience Impact)",
        "cta_title": "Votre site a besoin d'une refonte ?",
        "cta_text": "On analyse votre site actuel gratuitement et on vous dit honnêtement si une refonte est nécessaire, et ce qu'elle peut vous rapporter. Sans engagement.",
        "faq": [
            {"q": "Combien coûte une refonte de site web pour un artisan ou une PME ?", "a": "Entre 1 500 et 3 500 euros pour une refonte complète incluant nouvelle identité, nouveau contenu et optimisation SEO. Si seul le design change sans refonte du contenu et de la structure, comptez 800 à 1 500 euros. Une refonte mal planifiée peut coûter plus cher qu'une création from scratch."},
            {"q": "La refonte d'un site web va-t-elle faire perdre mon référencement actuel ?", "a": "Pas si elle est bien gérée. La clé : conserver les URLs existantes (ou mettre en place des redirections 301), ne pas supprimer les pages qui génèrent du trafic, et migrer le contenu qui fonctionne. Une refonte technique bien exécutée améliore généralement le SEO à moyen terme."},
            {"q": "Peut-on moderniser un site ancien sans le recréer entièrement ?", "a": "Oui, parfois. Si la structure du site est saine et que seul le design vieillit, un reskin (habillage graphique) est possible sans tout reconstruire. En revanche, si le site est lent, non mobile-friendly ou construit sur une technologie abandonnée, la reconstruction complète est souvent plus rapide et moins chère que le rafistolage."}
        ],
        "related": [
            {"slug": "site-web-qui-convertit", "title": "Pourquoi votre site web ne génère pas de contacts"},
            {"slug": "budget-site-web-artisan", "title": "Combien coûte un vrai site web pour un artisan en 2026"}
        ]
    }
}

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
    state['used_slugs'] = []
    return TOPICS[0]

def get_article_data(topic):
    return ARTICLES_DATA[topic['slug']]

def thumb_variant(n):
    return f"v{(n % 3) + 1}"

# ── Construction du HTML ───────────────────────────────────────────────────
def build_article_html(topic, data, pub_date, pub_date_fr):
    sections_html = ''
    for s in data['sections']:
        sections_html += f'\n        <h2>{s["h2"]}</h2>\n        {s["html"]}\n'

    # FAQ inline HTML
    faq_items = data.get('faq', [])
    if faq_items:
        faq_html = '\n        <h2>Questions fréquentes</h2>\n'
        for item in faq_items:
            faq_html += f'        <h3>{item["q"]}</h3>\n        <p>{item["a"]}</p>\n'
        sections_html += faq_html

    sommaire_items = '\n'.join(f'            <li>{item}</li>' for item in data['sommaire'])

    # Liens internes dynamiques depuis les données de l'article
    raw_related = data.get('related', [])
    if raw_related:
        related_html = '\n'.join(
            f'            <li><a href="{r["slug"]}.html" style="color:var(--sky);">{r["title"]}</a></li>'
            for r in raw_related
        )
    else:
        related_html = '            <li><a href="vitrine-google-maps-artisan.html" style="color:var(--sky);">Google Maps pour artisans</a></li>'

    # Schema Article
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": topic['title'],
        "description": data['meta_description'],
        "image": f"https://{CFG['domain']}/{CFG['og_image']}",
        "datePublished": pub_date,
        "author": {"@type": "Organization", "name": CFG["brand_name"]},
        "publisher": {"@type": "Organization", "name": CFG["brand_name"],
                      "logo": {"@type": "ImageObject", "url": f"https://{CFG['domain']}/{CFG['logo_full']}"}}
    }

    # Schema FAQPage si FAQ présente
    schemas = [article_schema]
    if faq_items:
        schemas.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": item["q"],
                 "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
                for item in faq_items
            ]
        })

    schema = json.dumps(schemas if len(schemas) > 1 else schemas[0], ensure_ascii=False, indent=4)

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0" />
  <meta name="theme-color" content="#1a2536" />

  <title>{html_escape(topic['title'])} · Digital Dreamsbox</title>
  <meta name="description" content="{html_escape(data['meta_description'])}" />
  <link rel="canonical" href="https://{CFG["domain"]}/pages/journal/{topic['slug']}.html" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{html_escape(topic['title'])}" />
  <meta property="og:description" content="{html_escape(data['og_description'])}" />
  <meta property="og:image" content="https://{CFG["domain"]}/{CFG["og_image"]}" />
  <link rel="icon" type="image/x-icon" href="../../favicon.ico" />
  <link rel="icon" type="image/png" href="../../favicon-light.png" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=Poppins:wght@400;500;600;700&amp;family=Phudu:wght@400;500;600;700&amp;family=Righteous&amp;family=Baloo+2:wght@400;500;600;700&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=Phudu:wght@400;500;600;700&family=Righteous&family=Baloo+2:wght@400;500;600;700&display=swap" rel="stylesheet" /></noscript>
  <link rel="stylesheet" href="../../styles.css" />

  <script type="application/ld+json">
  {schema}
  </script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga_id"]}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{CFG["ga_id"]}');
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
      <a href="tel:{CFG["phone"]}" class="btn btn-ghost nav-call"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>Appeler</a>
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
      <div class="footer-col"><h5>Contact</h5><ul><li><a href="tel:{CFG["phone"]}">{CFG["phone_display"]}</a></li><li><a href="mailto:{CFG["email"]}">{CFG["email"]}</a></li></ul></div>
      <div class="footer-col"><h5>Réseaux</h5><ul><li><a href="{CFG["social"]["youtube"]}" target="_blank" rel="noopener">YouTube</a></li><li><a href="{CFG["social"]["instagram"]}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{CFG["social"]["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a></li></ul></div>
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

    html = re.sub(
        r'(</div>\s*</div>\s*</section>\s*\n*</main>)',
        new_card + r'\n    \1',
        html,
        count=1
    )

    with open(JOURNAL_INDEX, 'w', encoding='utf-8') as f:
        f.write(html)

def update_sitemap(topic, pub_date):
    with open(SITEMAP_FILE, 'r', encoding='utf-8') as f:
        xml = f.read()

    url = f"https://digitaldreamsbox.com/pages/journal/{topic['slug']}.html"
    if url in xml:
        return

    entry = f'  <url><loc>{url}</loc><lastmod>{pub_date}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>\n'
    xml = xml.replace('</urlset>', entry + '</urlset>')

    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write(xml)

# ── Main ───────────────────────────────────────────────────────────────────
def main():
    state = load_state()
    topic = pick_topic(state)

    print(f"Sujet choisi : {topic['title']}")

    data = get_article_data(topic)
    print("Contenu récupéré.")

    today = datetime.date.today()
    pub_date    = today.isoformat()
    pub_date_fr = f"{today.day} {MONTHS_FR[today.month - 1]} {today.year}"

    article_html = build_article_html(topic, data, pub_date, pub_date_fr)

    out_path = os.path.join(JOURNAL_DIR, f"{topic['slug']}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(article_html)
    print(f"Article créé : {out_path}")

    update_journal_index(topic, data, state['article_count'])
    print("journal.html mis à jour.")

    update_sitemap(topic, pub_date)
    print("sitemap.xml mis à jour.")

    state['used_slugs'].append(topic['slug'])
    state['article_count'] += 1
    save_state(state)

    print(f"Terminé. Article publié : {topic['slug']}.html")

if __name__ == '__main__':
    main()
