# Doctrine : Amélioration continue du blog via Search Console

Copie de référence lue par la routine cloud Claude Code à chaque exécution hebdomadaire. La copie canonique (éditable par Lucas et Claude) vit dans le Jarvis, à `.claude/skills/amelioration-blog-seo/SKILL.md`. Si les deux divergent, la copie du Jarvis fait foi — mettre celle-ci à jour en conséquence.

---

## Mode de fonctionnement : validation ou autonome

**MODE ACTUEL : VALIDATION** (à repasser en `AUTONOME` par Lucas explicitement après quelques semaines sans souci)

- **Mode VALIDATION** : analyser et rédiger les propositions, mais ne jamais les publier directement sur `main`. Écrire un rapport dans `rapports-seo/[date].md`, commit et push ce rapport uniquement (jamais les articles eux-mêmes), puis s'arrêter.
- **Mode AUTONOME** : appliquer directement les corrections aux articles, commit et push sur `main`. Le rapport hebdomadaire continue d'être écrit pour garder une trace, mais n'est plus bloquant.

Ne jamais basculer soi-même de VALIDATION vers AUTONOME.

---

## Ce que fait la routine, dans l'ordre

### 1. Récupérer les données réelles

- Cloner (ou mettre à jour) deux repos :
  - `https://github.com/digitaldreamsboxcontact-lgtm/digitaldreamsbox-website` (le site, public — celui-ci)
  - `https://github.com/digitaldreamsboxcontact-lgtm/digitaldreamsbox-automation-secrets` (privé — contient `gsc-service-account.json`)
- Ne jamais afficher le contenu du fichier de clé dans une réponse, un commit ou un rapport. Le lire uniquement pour authentifier l'appel API.
- Interroger l'API Search Console (`searchanalytics.query`) sur la propriété **`sc-domain:digitaldreamsbox.com`** (propriété de type "domaine" — utiliser exactement cette chaîne comme `siteUrl`), filtrée sur les pages dont l'URL contient `/pages/journal/`, sur les 28 derniers jours, dimensions `page` + `query`.
- Si l'authentification échoue : ne pas inventer de données. Écrire un rapport signalant le blocage technique et s'arrêter.

### 2. Analyser

Pour chaque article (croiser avec `sitemap.xml` et `pages/journal/` pour la liste complète, y compris les articles à zéro impression) :

- Zéro impression 28 jours → sujet invisible. Candidat à réécriture titre/meta ou enrichissement.
- Impressions élevées, CTR < 2% → contenu vu mais peu cliqué. Candidat à réécriture `<title>` + meta description uniquement.
- Position 8-20 sur requête à volume correct → proche de la première page. Candidat à enrichissement de contenu ciblé.
- Requêtes fréquentes sans article dédié → sujet manquant, candidat à un nouvel article.
- Position 1-5 stable → ne rien toucher.

### 3. Agir (selon le mode)

Limites strictes dans les deux modes :
- Maximum 2 articles réécrits par passage, maximum 1 nouvel article créé par passage.
- Ne toucher qu'à `pages/journal/`, `pages/journal.html`, `sitemap.xml`, et `scripts/generate_article.py` (uniquement pour ajouter une entrée si nouvel article). Jamais `assets/`, `index.html`, les pages services, ou tout fichier hors blog.
- Respecter la doctrine narrative de `creation-site-client` Phase 6.5 (situation client réelle ou vraisemblable, jamais de fausses statistiques, CTA discret, liens internes, jamais de lien vers Digital Dreamsbox dans le corps).
- Ne jamais supprimer un article existant.
- `<title>` 50-60 caractères, meta description 140-160 caractères.
- Un changement = un commit séparé avec message clair.

### 4. Rapporter

Toujours produire `rapports-seo/[YYYY-MM-DD].md` : résumé 3 lignes, tableau par article (URL, impressions, clics, CTR, position, verdict), actions faites ou proposées avec justification par les données. Aucune affirmation sans donnée réelle à l'appui.

Toujours écrire aussi `rapports-seo/digest-gbp.txt` (écraser à chaque passage) : 2-4 lignes texte brut résumant les thématiques qui performent vraiment cette semaine (ou vide si rien d'exploitable). Lu automatiquement par le scénario Make GBP pour orienter ses posts. Exemple :
```
Cette semaine, les recherches réelles qui ramènent du monde sur le blog concernent : SEO local pour artisans, obtention d'avis Google, budget site web artisan. Les métiers/thèmes à privilégier si pertinent : plombier, électricien, service local.
```

---

## Garde-fous absolus

- Jamais de commit du fichier `gsc-service-account.json` ni de son contenu dans ce repo public.
- Jamais de modification hors périmètre blog.
- Données insuffisantes → le dire dans le rapport, ne pas improviser.
- Rien à faire cette semaine → rapport "rien à faire", c'est un résultat valide, ne rien publier.
