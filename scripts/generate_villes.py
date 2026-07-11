#!/usr/bin/env python3
"""
Génère les pages SEO locales pour toutes les villes cibles de Digital Dreamsbox.
Exécuter depuis la racine du site : python3 scripts/generate_villes.py
"""

import os, json
from datetime import date

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()

_CFG_FILE = os.path.join(os.path.dirname(__file__), 'config_digitaldreamsbox.json')
with open(_CFG_FILE, encoding='utf-8') as _f:
    CFG = json.load(_f)

VILLES = [
    {
        "nom": "Sarrebourg",
        "slug": "sarrebourg",
        "dept": "Moselle",
        "region_label": "Pays de Sarrebourg",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Sarrebourg et du Pays de Sarrebourg. Basés ici. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Sarrebourg et du Pays de Sarrebourg.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Sarrebourg,<br class=\"brk-md\">\n      Phalsbourg, Lorquin, Mittersheim et tout le Pays de Sarrebourg.<br class=\"brk-md\">\n      Basés ici, on intervient sur place ou en distanciel.",
        "zones_label": "Sarrebourg & Pays de Sarrebourg",
        "area_served": ["Sarrebourg", "Phalsbourg", "Lorquin", "Fenétrange", "Moselle", "Grand Est"],
        "ctx_title": "Sarrebourg a un tissu économique réel. <em>Le problème :</em> il est presque invisible en ligne.",
        "ctx_p1": "Chef-lieu d'arrondissement en Moselle, Sarrebourg et son pays rassemblent des artisans, des commerçants, des PME de services qui travaillent bien, mais qui n'ont souvent aucune présence numérique à la hauteur de leur activité. Pendant ce temps, leurs concurrents de Metz ou de Strasbourg captent les recherches Google.",
        "ctx_p2": "On est basés à Sarrebourg. On connaît les entreprises, les quartiers, la réalité économique locale. On intervient pour corriger ça : un site qui ressort sur Google, une identité qui inspire confiance, une présence qui travaille pour vous même quand vous êtes sur chantier.",
        "pb4": "« Je cherche une agence qui connaît Sarrebourg et les environs. »",
        "pb4a": "La proximité avec Phalsbourg ouvre une clientèle vers l'Alsace. On conçoit des sites et des stratégies qui couvrent à la fois le Pays de Sarrebourg et les zones frontalières côté Bas-Rhin.",
        "faq": [
            ("Vous êtes bien basés à Sarrebourg ?",
             "Oui. Digital Dreamsbox est basée à Sarrebourg. On connaît le tissu économique local, les commerçants, les artisans, les PME du pays. On peut se déplacer pour les échanges ou travailler entièrement en distanciel, selon ce qui vous convient."),
            ("J'ai une petite entreprise à Sarrebourg, c'est fait pour moi ?",
             "C'est exactement notre cœur de cible. Artisans, commerçants, PME de services, professionnels indépendants. Pas besoin d'un gros budget ou d'une structure importante. Ce qu'on regarde, c'est votre potentiel local et ce qu'on peut faire pour vous rendre visible sur votre zone."),
            ("Vous intervenez aussi sur Phalsbourg, Lorquin, Mittersheim ?",
             "Oui. On couvre tout le Pays de Sarrebourg : Sarrebourg, Phalsbourg, Lorquin, Réchicourt-le-Château, Fenétrange, Mittersheim, Sarralbe et les communes alentour. Un seul interlocuteur pour toute votre zone."),
            ("Pourquoi choisir Digital Dreamsbox plutôt qu'une agence de Metz ou Strasbourg ?",
             "Parce qu'une agence de Metz ou Strasbourg ne connaît pas Sarrebourg et son marché. Nous, si. On connaît les entreprises locales, les particularités de la zone, et on se déplace si nécessaire. Vous avez un seul interlocuteur du début à la fin."),
            ("Je veux améliorer ma fiche Google Business, vous faites ça aussi ?",
             "Oui. L'optimisation GMB est l'une de nos prestations les plus demandées : catégorisation, photos, avis, publications régulières. C'est souvent le levier le plus rapide pour gagner en visibilité locale sans refaire tout un site."),
            ("Quel délai pour un site vitrine à Sarrebourg ?",
             "En moyenne 2 à 3 semaines pour un site vitrine bien construit. On établit un planning précis en début de projet pour que vous sachiez toujours où on en est."),
        ],
        "faq_intro": "Les questions qu'on entend à Sarrebourg. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Sarrebourg, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("agence-web-forbach.html", "Forbach"), ("agence-web-sarreguemines.html", "Sarreguemines"), ("agence-web-phalsbourg.html", "Phalsbourg"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Phalsbourg",
        "slug": "phalsbourg",
        "dept": "Moselle",
        "region_label": "Pays de Sarrebourg / Alsace Bossue",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Phalsbourg, porte d'Alsace. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Phalsbourg et de la porte d'Alsace.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Phalsbourg,<br class=\"brk-md\">\n      Saverne, Sarrebourg et toute la porte d'Alsace.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Phalsbourg & porte d'Alsace",
        "area_served": ["Phalsbourg", "Saverne", "Sarrebourg", "Moselle", "Bas-Rhin", "Grand Est"],
        "ctx_title": "Phalsbourg, entre Lorraine et Alsace. <em>Le problème :</em> les entreprises locales n'exploitent pas ce double marché.",
        "ctx_p1": "Ancienne place forte à la croisée des routes, Phalsbourg concentre des artisans, des commerçants et des PME qui ont un potentiel sur deux marchés : la Lorraine côté Sarrebourg et l'Alsace côté Saverne et Strasbourg. Mais sans présence numérique solide, c'est la concurrence qui capte ces clients.",
        "ctx_p2": "On intervient à Phalsbourg pour construire cette présence : un site optimisé pour les deux zones, une identité cohérente, une fiche Google Business qui ressort sur les requêtes locales.",
        "pb4": "« Je veux capter des clients côté Alsace et côté Lorraine. »",
        "pb4a": "La position de Phalsbourg à 30 km de Saverne est une opportunité réelle. On conçoit des sites et des stratégies qui couvrent les deux marchés sans doublon de budget.",
        "faq": [
            ("Vous intervenez bien à Phalsbourg ?",
             "Oui. Digital Dreamsbox intervient à Phalsbourg et dans toute la zone entre Sarrebourg et Saverne. On se déplace sur place pour le cadrage, ou on travaille entièrement en distanciel."),
            ("Vous pouvez couvrir à la fois la clientèle lorraine et alsacienne ?",
             "Oui. La position de Phalsbourg entre Moselle et Bas-Rhin est une vraie opportunité. On conçoit des sites et des stratégies référencées sur les deux zones géographiques, sans doublon."),
            ("Je suis artisan à Phalsbourg, quel est votre délai ?",
             "2 à 3 semaines pour un site vitrine complet. Le délai varie selon la complexité. On établit un planning écrit en début de projet."),
            ("Vous intervenez aussi sur Saverne et Sarrebourg ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui inclut Phalsbourg, Saverne, Lorquin et tout l'axe Lorraine-Alsace."),
            ("Pourquoi ne pas choisir une agence de Strasbourg ?",
             "Une agence de Strasbourg ne connaît pas le marché de Phalsbourg ni les artisans locaux. Nous, on est dans la région, on connaît la réalité du terrain et on se déplace si besoin."),
            ("Quel budget prévoir pour un site à Phalsbourg ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Phalsbourg. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Phalsbourg, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-forbach.html", "Forbach"), ("agence-web-sarreguemines.html", "Sarreguemines"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Saint-Avold",
        "slug": "saint-avold",
        "dept": "Moselle",
        "region_label": "Moselle Est",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Saint-Avold et de la Moselle Est. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Saint-Avold et de la Moselle Est.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Saint-Avold,<br class=\"brk-md\">\n      Freyming-Merlebach, Forbach et toute la Moselle Est.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Saint-Avold & Moselle Est",
        "area_served": ["Saint-Avold", "Freyming-Merlebach", "Forbach", "Moselle", "Grand Est"],
        "ctx_title": "Saint-Avold, zone économique active. <em>Le problème :</em> les PME locales restent invisibles en ligne.",
        "ctx_p1": "Saint-Avold concentre des artisans, des sous-traitants industriels, des commerces et des services qui travaillent bien, mais qui n'ont souvent pas de présence numérique à la hauteur de leur activité. La zone est concurrencée par des agences de Metz qui ne connaissent pas le tissu local.",
        "ctx_p2": "On intervient à Saint-Avold pour construire une présence efficace : site web optimisé pour la recherche locale, identité de marque cohérente, campagnes ciblées sur la zone.",
        "pb4": "« Ma zone s'étend aussi sur Forbach et Sarreguemines. »",
        "pb4a": "On couvre l'ensemble de la Moselle Est. Un seul interlocuteur, une stratégie cohérente pour toute votre zone d'activité, que ce soit Saint-Avold, Forbach ou Sarreguemines.",
        "faq": [
            ("Vous intervenez bien à Saint-Avold ?",
             "Oui. Digital Dreamsbox intervient à Saint-Avold et dans toute la Moselle Est. On se déplace sur place ou on travaille en distanciel selon ce qui vous convient."),
            ("Je suis sous-traitant industriel à Saint-Avold, vous avez des références dans mon secteur ?",
             "Notre cœur de cible, ce sont les artisans et PME locaux, y compris les sous-traitants industriels. On présente des cas clients documentés sur rendez-vous : le contexte, ce qu'on a fait, les résultats obtenus."),
            ("Vous couvrez aussi Freyming-Merlebach et Forbach ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Saint-Avold, Freyming-Merlebach et Forbach. Un seul interlocuteur pour toute votre zone."),
            ("Pourquoi choisir Digital Dreamsbox plutôt qu'une agence de Metz ?",
             "Une grande agence de Metz vous donnera un chef de projet junior et une méthodologie standardisée. Nous, on connaît le tissu économique de la Moselle Est, on se déplace si nécessaire, et vous avez le même interlocuteur du début à la fin."),
            ("Je veux améliorer ma visibilité sur Google localement, par quoi commencer ?",
             "La plupart du temps, on commence par la fiche Google Business : c'est le levier le plus rapide. Ensuite, selon votre secteur, on complète avec un site ou une campagne Google Ads ciblée sur votre zone."),
            ("Quel budget prévoir pour un site à Saint-Avold ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage de 30 minutes. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Saint-Avold. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Saint-Avold, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-forbach.html", "Forbach"), ("agence-web-sarreguemines.html", "Sarreguemines"), ("agence-web-phalsbourg.html", "Phalsbourg")],
    },
    {
        "nom": "Lunéville",
        "slug": "luneville",
        "dept": "Meurthe-et-Moselle",
        "region_label": "Meurthe-et-Moselle",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Lunéville et du pays de la Vezouze. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Lunéville et de Meurthe-et-Moselle.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Lunéville,<br class=\"brk-md\">\n      Baccarat, Badonviller et tout le pays de la Vezouze.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Lunéville & pays de la Vezouze",
        "area_served": ["Lunéville", "Baccarat", "Badonviller", "Meurthe-et-Moselle", "Grand Est"],
        "ctx_title": "Lunéville, sous-préfecture active. <em>Le problème :</em> les entreprises locales peinent à se démarquer en ligne.",
        "ctx_p1": "Lunéville et le pays de la Vezouze comptent des artisans, des commerçants et des PME qui ont une vraie clientèle locale. Mais face aux agences de Nancy qui dominent les recherches, ils sont invisibles sur Google et perdent des prospects qui ne savent pas qu'ils existent.",
        "ctx_p2": "On intervient à Lunéville depuis Sarrebourg (moins d'une heure) pour créer cette présence : site web optimisé pour la recherche locale, identité cohérente, fiche Google Business performante.",
        "pb4": "« Je veux me démarquer des artisans de Nancy qui captent mes clients. »",
        "pb4a": "Un site web local bien référencé sur Lunéville et le pays de la Vezouze, c'est la meilleure réponse à la concurrence des grandes villes. On vous positionne là où vos clients vous cherchent.",
        "faq": [
            ("Vous venez à Lunéville depuis Sarrebourg ?",
             "Oui. Lunéville est à moins d'une heure de Sarrebourg. On se déplace pour le cadrage et les présentations, ou on travaille entièrement en distanciel selon vos préférences."),
            ("Je suis artisan à Lunéville, avez-vous des références dans mon secteur ?",
             "Notre cœur de cible, ce sont les artisans et PME locaux : bâtiment, services, commerce, restauration. On présente des cas clients documentés sur rendez-vous."),
            ("Vous couvrez aussi Baccarat et Badonviller ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Lunéville, Baccarat, Badonviller et tout le pays de la Vezouze."),
            ("Pourquoi vous plutôt qu'une agence de Nancy ?",
             "Une agence de Nancy a ses propres clients prioritaires et des tarifs adaptés à Nancy. Nous, on intervient sur votre zone, on connaît les enjeux des PME rurales et semi-rurales, et vous avez un interlocuteur unique du début à la fin."),
            ("Combien coûte un site web à Lunéville ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
            ("Quel est le délai moyen pour un site vitrine ?",
             "2 à 3 semaines pour un site vitrine bien construit. Le délai varie selon la complexité et le contenu fourni. On établit un planning précis en début de projet."),
        ],
        "faq_intro": "Les questions qu'on entend à Lunéville. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Lunéville, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-phalsbourg.html", "Phalsbourg"), ("agence-web-saint-avold.html", "Saint-Avold"), ("agence-web-dieuze.html", "Dieuze")],
    },
    {
        "nom": "Dieuze",
        "slug": "dieuze",
        "dept": "Moselle",
        "region_label": "Pays de la Seille",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Dieuze et du Pays de la Seille. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Dieuze et du Pays de la Seille.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Dieuze,<br class=\"brk-md\">\n      Château-Salins, Morhange et tout le Pays de la Seille.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Dieuze & Pays de la Seille",
        "area_served": ["Dieuze", "Château-Salins", "Morhange", "Moselle", "Grand Est"],
        "ctx_title": "Dieuze et le Pays de la Seille. <em>Le problème :</em> une zone avec de la demande, mais presque personne en ligne.",
        "ctx_p1": "Dieuze et les communes du Pays de la Seille concentrent des artisans et des commerçants qui ont une vraie clientèle locale. La concurrence numérique est quasi inexistante dans cette zone, ce qui représente une opportunité rare : se positionner maintenant, avant que les autres le fassent.",
        "ctx_p2": "On intervient à Dieuze pour créer une présence numérique solide : un site qui ressort sur Google pour vos clients locaux, une fiche GMB optimisée, une identité qui inspire confiance.",
        "pb4": "« Dans ma zone, il n'y a pas beaucoup de concurrence numérique. »",
        "pb4a": "C'est exactement ça. Le Pays de la Seille est une zone où la concurrence en ligne est faible. Se positionner maintenant vous donne une avance durable sur vos concurrents locaux.",
        "faq": [
            ("Vous intervenez à Dieuze et dans le Pays de la Seille ?",
             "Oui. Digital Dreamsbox intervient à Dieuze et dans toute la zone du Pays de la Seille : Château-Salins, Morhange, et les communes alentour."),
            ("Il y a peu d'entreprises numériques dans ma zone, est-ce un avantage ?",
             "Oui, c'est une opportunité réelle. Moins de concurrence numérique signifie qu'une page bien référencée peut se positionner en premier sur Google avec moins d'efforts. C'est maintenant qu'il faut agir."),
            ("Je suis artisan à Dieuze, par quoi commencer ?",
             "En général, on commence par un audit de votre situation actuelle : fiche Google Business, visibilité locale, site existant. Ensuite, on vous propose un plan d'attaque adapté à votre budget et vos objectifs."),
            ("Vous couvrez aussi Château-Salins et Morhange ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Dieuze, Château-Salins, Morhange et tout le Pays de la Seille."),
            ("Pourquoi une agence de Sarrebourg pour Dieuze ?",
             "Parce qu'on est dans la région et qu'on connaît la réalité économique des zones rurales et semi-rurales de Moselle. On se déplace si nécessaire, sans frais supplémentaires dans notre rayon."),
            ("Quel budget pour commencer ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Dieuze. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Dieuze, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-chateau-salins.html", "Château-Salins"), ("agence-web-morhange.html", "Morhange"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Morhange",
        "slug": "morhange",
        "dept": "Moselle",
        "region_label": "Plateau lorrain",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Morhange et du plateau lorrain. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Morhange et du plateau lorrain mosellan.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Morhange,<br class=\"brk-md\">\n      Dieuze, Sarrebourg et tout le plateau lorrain mosellan.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Morhange & plateau lorrain",
        "area_served": ["Morhange", "Dieuze", "Sarrebourg", "Moselle", "Grand Est"],
        "ctx_title": "Morhange et le plateau lorrain. <em>Le problème :</em> des artisans qui travaillent bien, mais que Google ignore.",
        "ctx_p1": "Morhange concentre des artisans, des PME agricoles et de services qui ont une clientèle locale fidèle. Mais sans présence en ligne, leur visibilité s'arrête au bouche à oreille. Quand un client cherche leur métier sur Google, c'est quelqu'un d'autre qui ressort.",
        "ctx_p2": "On intervient à Morhange pour changer ça. Une fiche Google Business optimisée, un site local bien référencé : des actions concrètes qui génèrent des contacts sans dépenser des milliers d'euros.",
        "pb4": "« Mon secteur est rural, est-ce que le web peut vraiment m'aider ? »",
        "pb4a": "Oui. La zone rurale et semi-rurale est souvent sous-couverte numériquement. Un artisan bien positionné localement sur Google peut capter toute la demande de sa zone sans concurrence numérique forte.",
        "faq": [
            ("Vous intervenez à Morhange ?",
             "Oui. Digital Dreamsbox intervient à Morhange et dans tout le plateau lorrain mosellan. On se déplace pour le cadrage ou on travaille en distanciel."),
            ("Le web peut-il vraiment aider un artisan en zone rurale ?",
             "Oui, et souvent plus facilement qu'en ville. La concurrence numérique est moins forte, ce qui permet de se positionner rapidement sur Google avec un site bien optimisé et une fiche GMB complète."),
            ("Vous couvrez aussi Dieuze et Château-Salins ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Morhange, Dieuze, Château-Salins et tout le plateau lorrain."),
            ("Par quoi commencer quand on a zéro présence en ligne ?",
             "D'abord la fiche Google Business : c'est gratuit, rapide à optimiser, et ça donne de la visibilité immédiate sur les recherches locales. Ensuite le site, si les besoins le justifient."),
            ("Vous faites aussi les logos et l'identité visuelle ?",
             "Oui. Branding, logo, palette, typographies : on peut intervenir sur toute la dimension visuelle de votre activité, ou uniquement sur le web si c'est votre priorité."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage de 30 minutes. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Morhange. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Morhange, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-dieuze.html", "Dieuze"), ("agence-web-chateau-salins.html", "Château-Salins"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Saverne",
        "slug": "saverne",
        "dept": "Bas-Rhin",
        "region_label": "Alsace",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Saverne et du Bas-Rhin. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Saverne et du Bas-Rhin.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Saverne,<br class=\"brk-md\">\n      Phalsbourg, Wasselonne et tout le nord du Bas-Rhin.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Saverne & nord Bas-Rhin",
        "area_served": ["Saverne", "Phalsbourg", "Wasselonne", "Bas-Rhin", "Grand Est"],
        "ctx_title": "Saverne, entre Strasbourg et Sarrebourg. <em>Le problème :</em> trop d'entreprises restent dans l'ombre de la grande ville.",
        "ctx_p1": "Saverne et le nord du Bas-Rhin ont un tissu économique actif, mais beaucoup d'artisans et de PME de la zone restent invisibles en ligne face aux agences de Strasbourg qui dominent les résultats Google. Or, la clientèle locale cherche des prestataires de proximité.",
        "ctx_p2": "On intervient à Saverne depuis Sarrebourg (30 minutes) pour créer une présence numérique qui capte cette demande locale : site référencé, GMB optimisée, identité cohérente.",
        "pb4": "« Je veux capter les clients entre Saverne et Sarrebourg. »",
        "pb4a": "La zone entre Saverne et Sarrebourg est un couloir économique avec peu de concurrence numérique locale. On conçoit des stratégies qui couvrent les deux côtés de la frontière Lorraine-Alsace.",
        "faq": [
            ("Vous intervenez à Saverne depuis Sarrebourg ?",
             "Oui. Saverne est à 30 minutes de Sarrebourg. On se déplace sur place pour le cadrage et les présentations, ou on travaille entièrement en distanciel selon votre préférence."),
            ("Vous faites des sites bilingues français-allemand pour l'Alsace ?",
             "Oui. Pour les entreprises qui ont une clientèle germanophone côté Allemagne ou Suisse, on conçoit des sites bilingues avec une architecture SEO adaptée à chaque langue et chaque marché."),
            ("Vous couvrez aussi Wasselonne et le nord Bas-Rhin ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Saverne, Wasselonne, Phalsbourg et tout le nord du Bas-Rhin."),
            ("Pourquoi pas une agence de Strasbourg ?",
             "Une agence de Strasbourg a ses propres priorités et ne connaît pas nécessairement les enjeux des PME de Saverne. Nous, on est dans la région, on se déplace si besoin, et vous avez un interlocuteur unique."),
            ("Je veux juste une refonte de mon site, vous faites ça ?",
             "Oui. Refonte partielle ou complète, on s'adapte. On commence toujours par un audit de l'existant pour identifier ce qui mérite d'être gardé et ce qui doit être repensé."),
            ("Quel budget prévoir pour Saverne ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Saverne. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Saverne, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-phalsbourg.html", "Phalsbourg"), ("agence-web-forbach.html", "Forbach"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Sarralbe",
        "slug": "sarralbe",
        "dept": "Moselle",
        "region_label": "Vallée de la Sarre",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Sarralbe et de la vallée de la Sarre. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Sarralbe et de la vallée de la Sarre.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Sarralbe,<br class=\"brk-md\">\n      Puttelange-aux-Lacs, Sarreguemines et toute la vallée de la Sarre.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Sarralbe & vallée de la Sarre",
        "area_served": ["Sarralbe", "Puttelange-aux-Lacs", "Sarreguemines", "Moselle", "Grand Est"],
        "ctx_title": "Sarralbe et la vallée de la Sarre. <em>Le problème :</em> un marché local sous-exploité en ligne.",
        "ctx_p1": "Sarralbe et les communes de la vallée de la Sarre ont des artisans et des PME qui tournent bien, mais dont la présence en ligne est quasi inexistante. La demande locale est là, mais elle est captée par des concurrents plus visibles numériquement.",
        "ctx_p2": "On intervient à Sarralbe pour inverser ce rapport : un site optimisé pour les requêtes locales, une fiche Google Business complète, une identité cohérente qui inspire confiance dès le premier contact.",
        "pb4": "« Je travaille aussi sur Sarreguemines et Puttelange. »",
        "pb4a": "On couvre toute la vallée de la Sarre. Un seul interlocuteur, une stratégie cohérente pour l'ensemble de votre zone d'activité.",
        "faq": [
            ("Vous intervenez à Sarralbe ?",
             "Oui. Digital Dreamsbox intervient à Sarralbe et dans toute la vallée de la Sarre. On se déplace ou on travaille en distanciel selon vos préférences."),
            ("Vous couvrez aussi Puttelange et Sarreguemines ?",
             "Oui. Notre rayon couvre 100 km autour de Sarrebourg, ce qui inclut Sarralbe, Puttelange-aux-Lacs, Sarreguemines et toute la zone de la Sarre."),
            ("Je n'ai aucune présence en ligne, par où commencer ?",
             "Par la fiche Google Business : c'est gratuit, rapide à optimiser, et ça donne une visibilité immédiate sur les recherches locales. Ensuite on évalue si un site web est nécessaire selon votre activité."),
            ("Vous faites aussi la gestion des avis Google ?",
             "Oui. On intègre la gestion des avis dans notre offre GMB : stratégie de collecte, réponses, signalement des avis abusifs. Les avis sont un levier de conversion majeur pour les artisans locaux."),
            ("Pourquoi choisir Digital Dreamsbox ?",
             "Parce qu'on est dans la région, qu'on connaît les artisans et PME de Moselle, et qu'on vous donne un interlocuteur unique du début à la fin. Pas de sous-traitance, pas de chef de projet junior."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Sarralbe. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Sarralbe, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-sarreguemines.html", "Sarreguemines"), ("agence-web-saint-avold.html", "Saint-Avold"), ("agence-web-puttelange.html", "Puttelange-aux-Lacs")],
    },
    {
        "nom": "Château-Salins",
        "slug": "chateau-salins",
        "dept": "Moselle",
        "region_label": "Pays des étangs",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Château-Salins et du Pays des étangs. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Château-Salins et du Pays des étangs.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Château-Salins,<br class=\"brk-md\">\n      Dieuze, Morhange et tout le Pays des étangs de Moselle.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Château-Salins & Pays des étangs",
        "area_served": ["Château-Salins", "Dieuze", "Morhange", "Moselle", "Grand Est"],
        "ctx_title": "Château-Salins, au cœur du Pays des étangs. <em>Le problème :</em> une économie locale sans vitrine numérique.",
        "ctx_p1": "Château-Salins et le Pays des étangs ont une économie locale active : artisans, restaurateurs, producteurs, prestataires de services. Mais cette économie reste invisible sur le web, laissant la demande locale sans réponse visible en ligne.",
        "ctx_p2": "On intervient à Château-Salins pour créer cette visibilité : site web optimisé pour les recherches locales, fiche Google Business complète, présence cohérente qui capte les clients de la zone.",
        "pb4": "« Je veux aussi capter les touristes qui visitent les étangs. »",
        "pb4a": "La zone touristique du Pays des étangs attire une clientèle saisonnière. On conçoit des sites et des fiches GMB qui captent aussi ces visiteurs au moment où ils cherchent des prestataires locaux.",
        "faq": [
            ("Vous intervenez à Château-Salins ?",
             "Oui. Digital Dreamsbox intervient à Château-Salins et dans tout le Pays des étangs. On se déplace ou on travaille en distanciel."),
            ("Vous couvrez aussi Dieuze et Morhange ?",
             "Oui. Notre rayon couvre 100 km autour de Sarrebourg, ce qui inclut Château-Salins, Dieuze, Morhange et toute la zone."),
            ("Je suis restaurateur ou prestataire touristique, vous avez de l'expérience dans ce secteur ?",
             "Oui. On a travaillé avec des établissements de restauration et de tourisme local. On sait comment valoriser une adresse, construire une présence en ligne qui donne envie de réserver."),
            ("Comment améliorer ma visibilité pour la saison touristique ?",
             "On commence par la fiche Google Business : photos, horaires saisonniers, publications régulières. Ensuite, si le site le mérite, on optimise les pages clés pour les requêtes liées au tourisme local."),
            ("Pourquoi ne pas passer par une agence de Nancy ?",
             "Une agence de Nancy ne connaît pas le marché de Château-Salins et n'a pas l'habitude de travailler avec des entreprises de cette taille. Nous si, et on se déplace sans frais supplémentaires."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Château-Salins. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Château-Salins, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-dieuze.html", "Dieuze"), ("agence-web-morhange.html", "Morhange"), ("agence-web-saint-avold.html", "Saint-Avold")],
    },
    {
        "nom": "Bitche",
        "slug": "bitche",
        "dept": "Moselle",
        "region_label": "Pays de Bitche",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Bitche et du Pays de Bitche. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Bitche et du Pays de Bitche.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Bitche,<br class=\"brk-md\">\n      Rohrbach-lès-Bitche, Puttelange et tout le Pays de Bitche.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Bitche & Pays de Bitche",
        "area_served": ["Bitche", "Rohrbach-lès-Bitche", "Puttelange-aux-Lacs", "Moselle", "Grand Est"],
        "ctx_title": "Bitche et le Pays de Bitche. <em>Le problème :</em> une zone touristique sans présence numérique locale.",
        "ctx_p1": "Bitche et son pays attirent des touristes grâce à la citadelle Vauban et au parc naturel régional des Vosges du Nord. Mais les artisans et commerçants locaux ne captent pas cette demande en ligne. Ils restent invisibles pendant que des prestataires extérieurs récupèrent leurs clients potentiels.",
        "ctx_p2": "On intervient à Bitche pour corriger ça : un site web référencé, une fiche Google Business optimisée, une présence qui capte à la fois la clientèle locale et les visiteurs de passage.",
        "pb4": "« Je veux capter les touristes qui visitent la citadelle. »",
        "pb4a": "La citadelle de Bitche attire des milliers de visiteurs par an. Un site bien positionné sur les requêtes touristiques locales peut capter une part significative de cette demande.",
        "faq": [
            ("Vous intervenez à Bitche ?",
             "Oui. Digital Dreamsbox intervient à Bitche et dans tout le Pays de Bitche. On se déplace ou on travaille en distanciel selon vos préférences."),
            ("Vous couvrez aussi Rohrbach-lès-Bitche et Puttelange ?",
             "Oui. Notre rayon couvre 100 km autour de Sarrebourg, ce qui inclut Bitche, Rohrbach-lès-Bitche, Puttelange-aux-Lacs et tout le pays."),
            ("Je suis prestataire touristique, comment capter plus de visiteurs en ligne ?",
             "On commence par optimiser votre fiche Google Business avec des photos professionnelles et des catégories précises. Ensuite, si votre site existe, on l'optimise pour les requêtes touristiques liées à Bitche et à la citadelle."),
            ("Vous avez de l'expérience dans le tourisme local ?",
             "Oui. On a travaillé avec des établissements de restauration et de tourisme. On sait comment valoriser une adresse et construire une présence qui convertit les recherches en réservations."),
            ("Pourquoi une agence de Sarrebourg pour Bitche ?",
             "Parce qu'on est dans la région, qu'on connaît les enjeux du Pays de Bitche, et qu'on se déplace sans frais supplémentaires. Vous avez un interlocuteur unique du début à la fin."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Bitche. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Bitche, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-sarreguemines.html", "Sarreguemines"), ("agence-web-saint-avold.html", "Saint-Avold"), ("agence-web-puttelange.html", "Puttelange-aux-Lacs")],
    },
    {
        "nom": "Puttelange-aux-Lacs",
        "slug": "puttelange",
        "dept": "Moselle",
        "region_label": "Pays de Bitche",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Puttelange-aux-Lacs et du Pays de Bitche. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Puttelange-aux-Lacs.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Puttelange-aux-Lacs,<br class=\"brk-md\">\n      Sarralbe, Bitche et toute la zone lacustre de Moselle.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Puttelange-aux-Lacs & zone lacustre",
        "area_served": ["Puttelange-aux-Lacs", "Sarralbe", "Bitche", "Moselle", "Grand Est"],
        "ctx_title": "Puttelange-aux-Lacs, entre lacs et activité locale. <em>Le problème :</em> des entreprises locales sans visibilité en ligne.",
        "ctx_p1": "Puttelange-aux-Lacs et ses environs concentrent artisans, commerçants et prestataires de services dans une zone où la concurrence numérique est quasi inexistante. Être visible sur Google ici, c'est capter l'essentiel de la demande locale sans se battre contre des dizaines de concurrents.",
        "ctx_p2": "On intervient dans la zone pour créer cette présence : site web référencé, fiche Google Business optimisée, identité cohérente qui inspire confiance dès le premier contact.",
        "pb4": "« Il n'y a presque personne en ligne dans ma zone. »",
        "pb4a": "C'est votre avantage. Dans une zone avec peu de concurrence numérique, un site bien optimisé peut se positionner en premier sur Google rapidement et durablement.",
        "faq": [
            ("Vous intervenez à Puttelange-aux-Lacs ?",
             "Oui. Digital Dreamsbox intervient à Puttelange-aux-Lacs et dans toute la zone lacustre de Moselle."),
            ("Vous couvrez aussi Sarralbe et Bitche ?",
             "Oui. Notre rayon couvre 100 km autour de Sarrebourg, ce qui inclut Puttelange-aux-Lacs, Sarralbe et Bitche."),
            ("J'ai une activité liée aux lacs et au tourisme, vous pouvez m'aider ?",
             "Oui. On sait valoriser les activités touristiques et de loisirs en ligne : fiche GMB avec photos, site optimisé pour les requêtes saisonnières, et présence qui capte les visiteurs."),
            ("Par quoi commencer si j'ai zéro présence en ligne ?",
             "Par la fiche Google Business : rapide à créer, gratuite, et immédiatement visible sur Google Maps. Ensuite on évalue si un site web est nécessaire selon votre activité et vos objectifs."),
            ("Pourquoi vous plutôt qu'une agence de Sarreguemines ?",
             "On connaît la zone et ses enjeux. On se déplace si nécessaire et vous avez un interlocuteur unique du début à la fin, sans sous-traitance."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Puttelange-aux-Lacs. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Puttelange-aux-Lacs, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-sarralbe.html", "Sarralbe"), ("agence-web-bitche.html", "Bitche"), ("agence-web-sarreguemines.html", "Sarreguemines")],
    },
    {
        "nom": "Mittersheim",
        "slug": "mittersheim",
        "dept": "Moselle",
        "region_label": "Pays de Sarrebourg",
        "desc_meta": "Digital Dreamsbox est implantée à Mittersheim. Sites web, branding et Google Ads pour les artisans et PME du Pays de Sarrebourg. Basés ici. Devis offert sous 48 h.",
        "og_desc": "Digital Dreamsbox est basée à Mittersheim. Sites web, branding et Google Ads pour les artisans et PME du Pays de Sarrebourg.",
        "hero_sub": "Digital Dreamsbox est implantée à Mittersheim.<br class=\"brk-md\">\n      Sites web, branding et Google Ads pour les artisans et PME de la zone,<br class=\"brk-md\">\n      Sarrebourg, Dieuze, Sarralbe et tout le Pays de Sarrebourg.",
        "zones_label": "Mittersheim & Pays de Sarrebourg",
        "area_served": ["Mittersheim", "Sarrebourg", "Dieuze", "Sarralbe", "Moselle", "Grand Est"],
        "ctx_title": "Mittersheim, notre commune. <em>Le problème :</em> même ici, les artisans sont invisibles en ligne.",
        "ctx_p1": "Digital Dreamsbox est implantée à Mittersheim, dans le Pays de Sarrebourg. On connaît les artisans, les commerçants, les PME de la zone de l'intérieur. Et on voit chaque jour que beaucoup d'entre eux travaillent bien mais n'ont aucune présence en ligne qui leur ressemble.",
        "ctx_p2": "On intervient sur place, sans frais de déplacement, pour construire cette présence : un site professionnel bien référencé, une fiche Google Business optimisée, une identité cohérente. Tout ce qu'il faut pour que vos clients vous trouvent avant la concurrence.",
        "pb4": "« Vous êtes vraiment implantés à Mittersheim ? »",
        "pb4a": "Oui. Digital Dreamsbox est basée au 16 rue d'Insviller, à Mittersheim (57930). On peut se déplacer sans frais dans toute la zone du Pays de Sarrebourg. Vous avez un interlocuteur local, pas une agence lointaine.",
        "faq": [
            ("Digital Dreamsbox est vraiment basée à Mittersheim ?",
             "Oui. Notre agence est installée au 16 rue d'Insviller, 57930 Mittersheim. On intervient sans frais de déplacement sur toute la zone du Pays de Sarrebourg : Sarrebourg, Mittersheim, Dieuze, Sarralbe et les communes alentour."),
            ("Je suis artisan dans le Pays de Sarrebourg, vous connaissez ma zone ?",
             "Oui. On est implantés ici depuis le départ. On connaît les entreprises locales, les contraintes des zones rurales et semi-rurales de Moselle, et on parle le même langage que nos clients."),
            ("Vous pouvez intervenir à domicile ou sur mon lieu de travail ?",
             "Oui. Pour les projets dans un rayon de 50 km autour de Mittersheim, on se déplace volontiers pour le cadrage, les présentations et les bilans. Au-delà, on travaille en distanciel sans surcoût."),
            ("Quelle différence avec une agence de Metz ou Nancy ?",
             "Une agence de Metz ne se déplace pas à Mittersheim pour une réunion. Nous si. Et on connaît la réalité économique locale, les enjeux des TPE et PME en zone rurale. Ce n'est pas un discours commercial, c'est notre quotidien."),
            ("Vous avez des références dans le Pays de Sarrebourg ?",
             "Oui. On présente nos cas clients sur rendez-vous : le contexte de départ, ce qu'on a mis en place, les résultats obtenus. On ne les liste pas publiquement par respect pour nos clients."),
            ("Quel délai pour commencer ?",
             "En général, on peut démarrer un premier échange dans la semaine. Le délai de production pour un site vitrine est de 2 à 3 semaines. On établit un planning écrit en début de projet."),
        ],
        "faq_intro": "Les questions qu'on entend dans le Pays de Sarrebourg. Une réponse vous manque ? On est juste à côté.",
        "contact_p": "On est à Mittersheim. Un échange de 30 minutes, sans engagement. On comprend votre activité, vous repartez avec une recommandation claire. On peut aussi se retrouver en face à face si vous le souhaitez.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-dieuze.html", "Dieuze"), ("agence-web-sarralbe.html", "Sarralbe"), ("agence-web-morhange.html", "Morhange")],
    },
    {
        "nom": "Sarre-Union",
        "slug": "sarre-union",
        "dept": "Bas-Rhin",
        "region_label": "Alsace Bossue",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Sarre-Union et de l'Alsace Bossue. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Sarre-Union et de l'Alsace Bossue.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Sarre-Union,<br class=\"brk-md\">\n      Drulingen, Ingwiller et toute l'Alsace Bossue.<br class=\"brk-md\">\n      Basés à Sarrebourg, on intervient sur place ou en distanciel.",
        "zones_label": "Sarre-Union & Alsace Bossue",
        "area_served": ["Sarre-Union", "Drulingen", "Ingwiller", "Bas-Rhin", "Grand Est"],
        "ctx_title": "Sarre-Union et l'Alsace Bossue. <em>Le problème :</em> une zone carrefour sans visibilité numérique locale.",
        "ctx_p1": "Sarre-Union et l'Alsace Bossue forment une zone économique à la frontière entre Lorraine et Alsace, avec un tissu d'artisans, d'agriculteurs et de PME bien installés. Mais cette zone reste peu visible sur Google : peu d'agences connaissent ses spécificités, et la plupart des prestataires numériques viennent de Strasbourg ou de Sarrebourg sans vraiment comprendre le marché local.",
        "ctx_p2": "On intervient à Sarre-Union depuis Sarrebourg (40 minutes) pour créer une présence numérique adaptée à ce double marché Lorraine-Alsace : site référencé sur les deux zones géographiques, fiche Google Business locale, identité qui inspire confiance.",
        "pb4": "« Ma clientèle est à cheval sur la Lorraine et l'Alsace. »",
        "pb4a": "C'est exactement la particularité de l'Alsace Bossue. On conçoit des sites et des stratégies SEO qui couvrent les deux marchés, sans doublon de budget. Une seule présence, deux zones capturées.",
        "faq": [
            ("Vous intervenez à Sarre-Union ?",
             "Oui. Sarre-Union est à 40 minutes de Sarrebourg. On se déplace pour le cadrage et les présentations importantes, ou on travaille entièrement en distanciel si vous préférez."),
            ("Vous pouvez cibler à la fois des clients en Lorraine et en Alsace ?",
             "Oui. La position de Sarre-Union entre Moselle et Bas-Rhin est une opportunité. On conçoit des sites référencés sur les deux zones géographiques et des campagnes Google Ads ciblées sur votre zone d'activité réelle."),
            ("Je suis dans le secteur agricole ou agroalimentaire, vous avez de l'expérience ?",
             "Oui. On a travaillé avec des producteurs locaux et des entreprises du secteur agroalimentaire régional. On sait comment valoriser une activité rurale et traditionnelle en ligne sans la dénaturer."),
            ("Vous couvrez aussi Drulingen et Ingwiller ?",
             "Oui. Notre rayon d'intervention couvre 100 km autour de Sarrebourg, ce qui englobe Sarre-Union, Drulingen, Ingwiller et toute l'Alsace Bossue."),
            ("Pourquoi choisir Digital Dreamsbox plutôt qu'une agence de Strasbourg ?",
             "Une agence de Strasbourg n'a pas de temps à consacrer à une PME de Sarre-Union. Nous si. On connaît la réalité économique de l'Alsace Bossue et on se déplace si nécessaire. Vous avez un seul interlocuteur du début à la fin."),
            ("Quel budget prévoir pour un site web ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend en Alsace Bossue. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes, sans engagement. On comprend votre activité à Sarre-Union, vous repartez avec une recommandation claire. Si on n'est pas la bonne agence pour vous, on le dit.",
        "autres_zones": [("index.html", "Sarrebourg"), ("agence-web-phalsbourg.html", "Phalsbourg"), ("agence-web-bitche.html", "Bitche"), ("agence-web-sarreguemines.html", "Sarreguemines")],
    },
    {
        "nom": "Sélestat",
        "slug": "selestat",
        "dept": "Bas-Rhin",
        "region_label": "Alsace centrale",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Sélestat et du centre Alsace. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Sélestat et du centre Alsace.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Sélestat,<br class=\"brk-md\">\n      Obernai, Colmar et tout le centre Alsace.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel ou sur rendez-vous.",
        "zones_label": "Sélestat & centre Alsace",
        "area_served": ["Sélestat", "Obernai", "Colmar", "Bas-Rhin", "Haut-Rhin", "Grand Est"],
        "ctx_title": "Sélestat, cœur de l'Alsace active. <em>Le problème :</em> des PME avec du potentiel mais une visibilité en ligne insuffisante.",
        "ctx_p1": "Sélestat est une ville commerçante et industrielle du centre Alsace avec un tissu économique dense : artisans du bâtiment, PME de services, commerces de centre-ville, prestataires B2B. Beaucoup ont un potentiel de clientèle local fort, mais leur présence numérique ne reflète pas la qualité de leur activité.",
        "ctx_p2": "On intervient à Sélestat en distanciel ou sur rendez-vous pour construire cette présence : un site web optimisé pour le SEO local alsacien, une identité de marque qui inspire confiance, une fiche Google Business qui ressort sur les recherches locales.",
        "pb4": "« J'ai de la concurrence locale forte, comment me démarquer en ligne ? »",
        "pb4a": "Dans un marché aussi actif que Sélestat, la différenciation numérique est décisive. Un site bien structuré, des avis gérés et une fiche GMB active peuvent vous positionner devant des concurrents pourtant plus anciens.",
        "faq": [
            ("Vous intervenez à Sélestat depuis Sarrebourg ?",
             "Oui. Pour Sélestat, on travaille principalement en distanciel, avec des déplacements sur rendez-vous pour les cadrages importants. La distance est d'environ 80 km, facilement compensée par un bon suivi à distance."),
            ("Vous avez de l'expérience sur le marché alsacien ?",
             "Oui. On travaille avec des clients en Alsace et on connaît les spécificités du marché régional : la clientèle germanophone, les enjeux du tourisme, la concurrence entre villes du Rhin."),
            ("Vous faites des sites bilingues français-allemand ?",
             "Oui. Pour les entreprises qui visent une clientèle germanophone, on conçoit des sites bilingues avec une architecture SEO adaptée à chaque langue et chaque marché."),
            ("Vous couvrez aussi Obernai et Colmar ?",
             "Oui. On intervient sur l'ensemble du centre Alsace, de Strasbourg à Colmar. Pour ces villes, on fonctionne en distanciel avec déplacements sur rendez-vous."),
            ("Pourquoi une agence de Sarrebourg pour Sélestat ?",
             "Parce qu'on combine la connaissance du Grand Est avec un tarif adapté aux PME, sans les structures de coûts des agences alsaciennes. Et parce qu'on travaille en distanciel aussi bien qu'en présentiel."),
            ("Quel budget prévoir pour une entreprise à Sélestat ?",
             "Chaque projet est chiffré sur devis. On établit un devis détaillé sous 48 h après un échange de cadrage de 30 minutes, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Sélestat. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio ou par téléphone, sans engagement. On comprend votre activité à Sélestat, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-obernai.html", "Obernai"), ("agence-web-molsheim.html", "Molsheim"), ("agence-web-saverne.html", "Saverne"), ("agence-web-phalsbourg.html", "Phalsbourg")],
    },
    {
        "nom": "Obernai",
        "slug": "obernai",
        "dept": "Bas-Rhin",
        "region_label": "Route des Vins d'Alsace",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans, vignerons et PME d'Obernai. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans, vignerons et PME d'Obernai et de la Route des Vins.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans, vignerons et PME d'Obernai,<br class=\"brk-md\">\n      Sélestat, Molsheim et toute la Route des Vins d'Alsace.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel ou sur rendez-vous.",
        "zones_label": "Obernai & Route des Vins",
        "area_served": ["Obernai", "Sélestat", "Molsheim", "Bas-Rhin", "Grand Est"],
        "ctx_title": "Obernai, entre viticulture et économie locale. <em>Le problème :</em> une image de marque trop souvent générique.",
        "ctx_p1": "Obernai et la Route des Vins concentrent des vignerons, des hôteliers, des artisans et des commerces qui méritent une image de marque à la hauteur de leur qualité. Pourtant, beaucoup se contentent d'un site daté ou d'une fiche Google incomplète qui ne reflète pas ce qu'ils proposent vraiment.",
        "ctx_p2": "On intervient à Obernai pour construire une présence numérique à la hauteur : identité visuelle soignée, site web qui valorise votre activité, fiche Google Business qui attire les clients touristiques et locaux. En distanciel ou sur rendez-vous.",
        "pb4": "« Je veux capter aussi les touristes de la Route des Vins. »",
        "pb4a": "La Route des Vins attire des millions de visiteurs par an. Un site bien positionné sur les requêtes touristiques locales et une fiche GMB complète sont vos meilleurs outils pour capter cette demande au bon moment.",
        "faq": [
            ("Vous intervenez à Obernai ?",
             "Oui. Pour Obernai, on travaille principalement en distanciel, avec des déplacements sur rendez-vous. La visioconférence permet de gérer l'essentiel des projets sans perte de qualité."),
            ("Vous avez de l'expérience avec les acteurs du tourisme et de la viticulture ?",
             "Oui. On a travaillé avec des établissements de tourisme et des producteurs locaux. On sait comment valoriser une adresse, raconter une histoire, et construire une présence qui donne envie de venir."),
            ("Vous faites des sites bilingues pour les touristes germanophones ?",
             "Oui. Pour les professionnels qui accueillent une clientèle d'Allemagne ou de Suisse, on conçoit des sites bilingues ou multilingues avec une architecture SEO adaptée à chaque langue."),
            ("Vous couvrez aussi les communes de la Route des Vins ?",
             "Oui. On intervient sur toute la Route des Vins d'Alsace, de Marlenheim à Thann, en distanciel ou sur rendez-vous selon les projets."),
            ("Pourquoi vous plutôt qu'une agence locale de Strasbourg ou Colmar ?",
             "Parce qu'on apporte un regard extérieur précieux pour vous différencier d'une concurrence locale homogène, avec des tarifs adaptés aux PME sans les structures de coûts des grandes agences."),
            ("Quel budget prévoir pour un projet à Obernai ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Obernai et sur la Route des Vins. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Obernai, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-selestat.html", "Sélestat"), ("agence-web-molsheim.html", "Molsheim"), ("agence-web-saverne.html", "Saverne"), ("agence-web-phalsbourg.html", "Phalsbourg")],
    },
    {
        "nom": "Molsheim",
        "slug": "molsheim",
        "dept": "Bas-Rhin",
        "region_label": "Alsace centrale",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Molsheim et du centre Bas-Rhin. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Molsheim et du centre Bas-Rhin.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Molsheim,<br class=\"brk-md\">\n      Obernai, Saverne et tout le centre Bas-Rhin.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel ou sur rendez-vous.",
        "zones_label": "Molsheim & centre Bas-Rhin",
        "area_served": ["Molsheim", "Obernai", "Saverne", "Bas-Rhin", "Grand Est"],
        "ctx_title": "Molsheim, bassin industriel et artisanal. <em>Le problème :</em> des entreprises performantes mais invisibles en ligne.",
        "ctx_p1": "Molsheim et son bassin concentrent des PME industrielles, des artisans du bâtiment et des prestataires de services qui opèrent dans un marché concurrentiel. Mais beaucoup n'ont pas encore de présence numérique solide, laissant la demande locale et régionale à des concurrents mieux positionnés sur Google.",
        "ctx_p2": "On intervient à Molsheim en distanciel ou sur rendez-vous pour construire une présence efficace : site web professionnel, fiche Google Business optimisée, identité cohérente qui inspire confiance.",
        "pb4": "« Mon secteur est industriel ou technique, le web peut vraiment m'aider ? »",
        "pb4a": "Oui, et plus qu'on ne le pense. Les acheteurs B2B recherchent leurs prestataires en ligne avant même de les appeler. Un site clair, crédible et bien référencé est souvent le premier filtre de sélection.",
        "faq": [
            ("Vous intervenez à Molsheim ?",
             "Oui. Pour Molsheim, on travaille principalement en distanciel, avec des déplacements sur rendez-vous pour les projets qui le justifient. À 70 km de Sarrebourg, c'est tout à fait accessible."),
            ("Vous travaillez avec des PME industrielles ou techniques ?",
             "Oui. On a accompagné des entreprises du secteur industriel, de la sous-traitance et des services B2B. On sait comment présenter une activité technique de façon claire et crédible sans jargon inutile."),
            ("Vous couvrez aussi Obernai et Saverne ?",
             "Oui. On intervient sur l'ensemble du centre Bas-Rhin. Pour toutes ces villes, on fonctionne en distanciel ou sur rendez-vous selon les besoins du projet."),
            ("Combien de temps pour refaire un site professionnel à Molsheim ?",
             "En moyenne 2 à 3 semaines pour un site vitrine complet, à partir du moment où le contenu est prêt. On établit un planning écrit en début de projet."),
            ("Pourquoi vous plutôt qu'une agence strasbourgeoise ?",
             "Parce qu'on est dimensionnés pour les PME, pas pour les grands comptes. Nos tarifs sont adaptés, nos délais sont tenus, et vous avez un seul interlocuteur du début à la fin."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage de 30 minutes. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Molsheim. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio ou par téléphone, sans engagement. On comprend votre activité à Molsheim, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-obernai.html", "Obernai"), ("agence-web-selestat.html", "Sélestat"), ("agence-web-saverne.html", "Saverne"), ("agence-web-phalsbourg.html", "Phalsbourg")],
    },
    {
        "nom": "Épinal",
        "slug": "epinal",
        "dept": "Vosges",
        "region_label": "Vosges",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME d'Épinal et des Vosges. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME d'Épinal et des Vosges.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME d'Épinal,<br class=\"brk-md\">\n      Remiremont, Saint-Dié-des-Vosges et tout le département des Vosges.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel.",
        "zones_label": "Épinal & Vosges",
        "area_served": ["Épinal", "Remiremont", "Saint-Dié-des-Vosges", "Vosges", "Grand Est"],
        "ctx_title": "Épinal, préfecture des Vosges. <em>Le problème :</em> un marché actif mais des entreprises peu visibles en ligne.",
        "ctx_p1": "Épinal est la préfecture des Vosges avec un tissu économique diversifié : artisans du bâtiment, PME industrielles héritières de l'industrie textile, commerces, services à la personne et professionnels de santé. Beaucoup de ces entreprises ont une clientèle locale fidèle, mais leur présence numérique ne leur permet pas de capter de nouveaux clients.",
        "ctx_p2": "On intervient à Épinal en 100 % distanciel pour créer une présence numérique qui génère des contacts : site web optimisé pour le SEO local vosgien, fiche Google Business active, identité de marque cohérente.",
        "pb4": "« J'ai besoin d'une agence qui travaille vite et efficacement à distance. »",
        "pb4a": "C'est exactement notre mode de fonctionnement pour les clients hors Moselle. On maîtrise le travail en distanciel : visioconférences courtes, livrables écrits clairs, délais tenus. Pas de réunions inutiles.",
        "faq": [
            ("Vous intervenez à Épinal ?",
             "Oui. Pour Épinal, on travaille exclusivement en distanciel : échanges par visioconférence, livrables envoyés en ligne, validations à distance. C'est un mode de fonctionnement qu'on maîtrise parfaitement."),
            ("Le distanciel fonctionne bien pour un projet de site web ?",
             "Oui, et c'est souvent plus efficace que des réunions en présentiel. On travaille avec des livrables écrits précis et des délais tenus. La majorité de nos clients travaillent déjà ainsi."),
            ("Vous connaissez le marché vosgien ?",
             "On intervient dans les Vosges et on a une bonne connaissance du tissu économique régional, notamment les héritages industriels et le secteur touristique lié à la montagne et aux lacs vosgiens."),
            ("Vous couvrez aussi Remiremont et Saint-Dié-des-Vosges ?",
             "Oui. On intervient dans l'ensemble du département des Vosges en distanciel. Épinal, Remiremont, Saint-Dié-des-Vosges, Gérardmer : on adapte notre intervention à votre zone."),
            ("Pourquoi pas une agence vosgienne ?",
             "Les agences locales d'Épinal ont souvent des délais longs et des tarifs élevés pour les PME. On offre un service comparable à tarif adapté, en distanciel, avec des délais clairs."),
            ("Quel budget prévoir pour un projet à Épinal ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage de 30 minutes en visio. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Épinal et dans les Vosges. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Épinal, vous repartez avec une recommandation claire. Tout se fait à distance, sans friction.",
        "autres_zones": [("agence-web-remiremont.html", "Remiremont"), ("agence-web-saint-die.html", "Saint-Dié-des-Vosges"), ("agence-web-luneville.html", "Lunéville"), ("index.html", "Sarrebourg")],
    },
    {
        "nom": "Saint-Dié-des-Vosges",
        "slug": "saint-die",
        "dept": "Vosges",
        "region_label": "Vosges",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Saint-Dié-des-Vosges. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Saint-Dié-des-Vosges et du massif vosgien.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Saint-Dié-des-Vosges,<br class=\"brk-md\">\n      Épinal, Sélestat et toute la vallée de la Meurthe.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel.",
        "zones_label": "Saint-Dié-des-Vosges & vallée de la Meurthe",
        "area_served": ["Saint-Dié-des-Vosges", "Épinal", "Sélestat", "Vosges", "Grand Est"],
        "ctx_title": "Saint-Dié-des-Vosges, entre forêt et économie locale. <em>Le problème :</em> une ville dynamique peu visible sur le web.",
        "ctx_p1": "Saint-Dié-des-Vosges et la vallée de la Meurthe ont un tissu économique bien réel : artisans, PME, professionnels du tourisme de montagne et de la filière bois. Mais beaucoup n'ont pas encore de présence numérique adaptée à la concurrence actuelle sur Google.",
        "ctx_p2": "On intervient à Saint-Dié-des-Vosges en distanciel pour créer cette présence : site web optimisé pour le SEO local, fiche Google Business qui attire les clients, identité cohérente. Des outils simples qui génèrent des contacts réguliers.",
        "pb4": "« Mon activité est liée au tourisme vosgien et à la montagne. »",
        "pb4a": "Le massif vosgien attire une clientèle touristique qui planifie ses séjours en ligne. Un site bien référencé sur les requêtes touristiques locales et une fiche GMB complète vous permettent de capter cette demande avant vos concurrents.",
        "faq": [
            ("Vous intervenez à Saint-Dié-des-Vosges ?",
             "Oui. Pour Saint-Dié-des-Vosges, on travaille en distanciel : échanges en visioconférence, livrables en ligne, validations à distance. C'est un mode de fonctionnement rodé qui permet de travailler efficacement."),
            ("Vous avez de l'expérience avec le tourisme de montagne ?",
             "Oui. On sait comment valoriser une activité liée à la nature, à la randonnée, aux sports d'hiver ou à l'artisanat local. On conçoit des sites qui donnent envie de réserver et des fiches GMB qui captent les visiteurs."),
            ("Vous couvrez aussi Gérardmer et Bruyères ?",
             "Oui. On intervient dans l'ensemble du département des Vosges en distanciel, y compris Gérardmer, Bruyères, Corcieux et les communes du massif."),
            ("Le distanciel est aussi efficace que le présentiel ?",
             "Oui. On a développé une méthode de travail à distance efficace : brief structuré, livrables clairs, délais tenus. La plupart de nos clients valident les projets sans se déplacer une seule fois."),
            ("Pourquoi vous plutôt qu'une agence locale ?",
             "Parce qu'on est dimensionnés pour les PME et les artisans, avec des tarifs adaptés et des délais clairs. Et parce qu'on a une expertise SEO locale qui fait souvent défaut aux agences généralistes."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Saint-Dié-des-Vosges. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Saint-Dié-des-Vosges, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-epinal.html", "Épinal"), ("agence-web-remiremont.html", "Remiremont"), ("agence-web-selestat.html", "Sélestat"), ("agence-web-luneville.html", "Lunéville")],
    },
    {
        "nom": "Remiremont",
        "slug": "remiremont",
        "dept": "Vosges",
        "region_label": "Vosges du Sud",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Remiremont et des Vosges du Sud. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Remiremont et des Vosges du Sud.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Remiremont,<br class=\"brk-md\">\n      Épinal, Plombières-les-Bains et tout le sud des Vosges.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel.",
        "zones_label": "Remiremont & Vosges du Sud",
        "area_served": ["Remiremont", "Épinal", "Plombières-les-Bains", "Vosges", "Grand Est"],
        "ctx_title": "Remiremont, entre tradition et économie locale. <em>Le problème :</em> des artisans et commerçants sans vitrine numérique.",
        "ctx_p1": "Remiremont et le sud des Vosges ont un tissu économique solide : artisans, commerçants, prestataires de services et acteurs du tourisme thermal et de montagne. Mais la plupart n'ont pas encore de présence numérique à la hauteur de leur activité, alors que leurs clients les cherchent de plus en plus sur Google.",
        "ctx_p2": "On intervient à Remiremont en distanciel pour créer cette présence : site web optimisé, fiche Google Business active, identité cohérente qui inspire confiance. Des leviers concrets pour générer des contacts sans attendre.",
        "pb4": "« Je veux capter les clients des stations thermales et de montagne. »",
        "pb4a": "Plombières-les-Bains, la Bresse, Gérardmer : le sud des Vosges attire une clientèle touristique et de bien-être. On conçoit des sites et des fiches GMB qui captent cette demande au bon moment, sur les bons mots-clés.",
        "faq": [
            ("Vous intervenez à Remiremont ?",
             "Oui. Pour Remiremont, on travaille exclusivement en distanciel : visioconférences, livrables en ligne, validations à distance. Un mode de fonctionnement efficace que nos clients apprécient."),
            ("Vous couvrez aussi Plombières-les-Bains et la Bresse ?",
             "Oui. On intervient dans tout le sud des Vosges en distanciel : Remiremont, Plombières-les-Bains, La Bresse, Gérardmer et les communes alentour."),
            ("Vous avez de l'expérience avec le tourisme de bien-être et thermal ?",
             "Oui. On a accompagné des établissements de tourisme et des professionnels du bien-être. On sait comment valoriser ce type d'activité en ligne et capter une clientèle en recherche de prestations qualitatives."),
            ("Le distanciel permet-il un travail de qualité ?",
             "Oui. On a développé une méthode structurée : brief détaillé, maquettes validées en ligne, livrables clairs à chaque étape. La distance ne diminue pas la qualité, elle force même plus de rigueur dans la communication."),
            ("Pourquoi choisir Digital Dreamsbox plutôt qu'une agence locale ?",
             "Parce qu'on est spécialisés sur les leviers qui génèrent des clients locaux : SEO local, GMB, site vitrine. Pas de prestation inutile, pas de forfait gonflé. Ce qu'il faut, au bon prix."),
            ("Quel budget prévoir pour un projet à Remiremont ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage en visio. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Remiremont. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Remiremont, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-epinal.html", "Épinal"), ("agence-web-saint-die.html", "Saint-Dié-des-Vosges"), ("agence-web-luneville.html", "Lunéville"), ("index.html", "Sarrebourg")],
    },
    {
        "nom": "Verdun",
        "slug": "verdun",
        "dept": "Meuse",
        "region_label": "Meuse",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Verdun et de la Meuse. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Verdun et de la Meuse.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Verdun,<br class=\"brk-md\">\n      Bar-le-Duc, Commercy et toute la Meuse.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel.",
        "zones_label": "Verdun & Meuse",
        "area_served": ["Verdun", "Bar-le-Duc", "Commercy", "Meuse", "Grand Est"],
        "ctx_title": "Verdun, ville historique et économie réelle. <em>Le problème :</em> des PME locales sans visibilité numérique.",
        "ctx_p1": "Verdun est connue dans le monde entier pour son histoire, mais la ville a aussi une économie active : artisans, commerçants, PME de services, acteurs du tourisme mémoriel. Beaucoup de ces entreprises n'ont pas encore de présence numérique adaptée à la concurrence actuelle sur Google.",
        "ctx_p2": "On intervient à Verdun en distanciel depuis Sarrebourg pour créer cette présence : site web référencé sur les requêtes locales meurtoises, fiche Google Business optimisée, identité de marque professionnelle.",
        "pb4": "« Le tourisme mémoriel attire des visiteurs de toute l'Europe. Comment capter cette demande ? »",
        "pb4a": "Verdun attire des centaines de milliers de visiteurs par an. Un site bien positionné sur les requêtes touristiques et une fiche GMB complète avec photos et horaires sont vos meilleurs outils pour capter cette clientèle internationale.",
        "faq": [
            ("Vous intervenez à Verdun ?",
             "Oui. Pour Verdun, on travaille en distanciel : échanges en visioconférence, livrables partagés en ligne, validations à distance. Un mode de travail efficace sans déplacement."),
            ("Vous avez de l'expérience avec le tourisme mémoriel ?",
             "Oui. On a accompagné des acteurs du tourisme culturel et mémoriel. On sait comment valoriser ce type d'activité en ligne et capter une clientèle internationale qui planifie ses visites bien à l'avance."),
            ("Vous faites des sites multilingues pour les touristes étrangers ?",
             "Oui. Pour les acteurs du tourisme à Verdun, on conçoit des sites bilingues ou multilingues (français, anglais, allemand) avec une architecture SEO adaptée à chaque marché."),
            ("Vous couvrez aussi Bar-le-Duc et la Meuse ?",
             "Oui. On intervient dans l'ensemble du département de la Meuse en distanciel : Verdun, Bar-le-Duc, Commercy, Saint-Mihiel et les communes alentour."),
            ("Pourquoi une agence de Sarrebourg pour Verdun ?",
             "Parce qu'on intervient dans tout le Grand Est et qu'on a l'habitude de travailler à distance. Le tarif est adapté aux PME, et vous avez un seul interlocuteur du début à la fin."),
            ("Quel budget prévoir ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage en visio. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Verdun. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Verdun, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-bar-le-duc.html", "Bar-le-Duc"), ("agence-web-luneville.html", "Lunéville"), ("agence-web-saint-die.html", "Saint-Dié-des-Vosges"), ("index.html", "Sarrebourg")],
    },
    {
        "nom": "Bar-le-Duc",
        "slug": "bar-le-duc",
        "dept": "Meuse",
        "region_label": "Meuse",
        "desc_meta": "Digital Dreamsbox crée des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de Bar-le-Duc et de la Meuse. Devis offert sous 48 h.",
        "og_desc": "Sites web, branding et Google Ads pour les artisans et PME de Bar-le-Duc et de la Meuse.",
        "hero_sub": "Sites web, branding et Google Ads pour les artisans et PME de Bar-le-Duc,<br class=\"brk-md\">\n      Verdun, Commercy et toute la Meuse.<br class=\"brk-md\">\n      Basés à Sarrebourg, intervention 100 % distanciel.",
        "zones_label": "Bar-le-Duc & Meuse",
        "area_served": ["Bar-le-Duc", "Verdun", "Commercy", "Meuse", "Grand Est"],
        "ctx_title": "Bar-le-Duc, préfecture de la Meuse. <em>Le problème :</em> un centre économique sous-représenté en ligne.",
        "ctx_p1": "Bar-le-Duc est la préfecture de la Meuse avec un tissu économique solide : artisans du bâtiment, PME de services, commerces de centre-ville et professionnels libéraux. Beaucoup ont une clientèle locale établie, mais leur présence numérique ne génère pas de nouveaux contacts.",
        "ctx_p2": "On intervient à Bar-le-Duc en distanciel pour construire une présence numérique qui travaille pour vous : site web optimisé pour les recherches locales meurtoises, fiche Google Business active, identité cohérente.",
        "pb4": "« Je veux développer ma clientèle dans la Meuse et au-delà. »",
        "pb4a": "Bar-le-Duc est un carrefour entre Paris, Metz et Nancy via les grands axes routiers. Un site bien référencé sur Bar-le-Duc et les communes alentour vous positionne sur un bassin plus large que votre seule commune.",
        "faq": [
            ("Vous intervenez à Bar-le-Duc ?",
             "Oui. Pour Bar-le-Duc, on travaille en distanciel : visioconférences, livrables en ligne, validations à distance. C'est un mode de fonctionnement fluide que nos clients apprécient."),
            ("Vous couvrez aussi Verdun et la Meuse ?",
             "Oui. On intervient dans tout le département de la Meuse en distanciel : Bar-le-Duc, Verdun, Commercy, Saint-Mihiel et les communes alentour."),
            ("Je suis artisan à Bar-le-Duc, par quoi commencer ?",
             "En général, on commence par la fiche Google Business : c'est le levier le plus rapide pour gagner en visibilité locale. Ensuite, selon votre activité, on complète avec un site web ou une campagne Google Ads ciblée sur Bar-le-Duc et les alentours."),
            ("Le distanciel vous convient pour gérer un projet de bout en bout ?",
             "Oui. On travaille avec des clients exclusivement en distanciel. Visioconférences courtes, livrables écrits, délais tenus : c'est un mode de collaboration efficace que nos clients apprécient."),
            ("Pourquoi pas une agence locale de Nancy ou Metz ?",
             "Parce qu'une agence de Nancy ou Metz n'a pas nécessairement de temps pour une PME de Bar-le-Duc. On se concentre sur les artisans et PME locaux et on leur donne toute notre attention."),
            ("Quel budget prévoir pour un projet à Bar-le-Duc ?",
             "Chaque projet est chiffré sur devis après un échange de cadrage en visio. On établit un devis détaillé sous 48 h, sans engagement."),
        ],
        "faq_intro": "Les questions qu'on entend à Bar-le-Duc. Une réponse vous manque ? Posez-la directement, on répond sous 24 h.",
        "contact_p": "Un échange de 30 minutes en visio, sans engagement. On comprend votre activité à Bar-le-Duc, vous repartez avec une recommandation claire.",
        "autres_zones": [("agence-web-verdun.html", "Verdun"), ("agence-web-luneville.html", "Lunéville"), ("agence-web-epinal.html", "Épinal"), ("index.html", "Sarrebourg")],
    },
]


def build_faq_jsonld(ville, faq_list):
    items = []
    for q, a in faq_list:
        items.append(f'''        {{
          "@type": "Question",
          "name": "{q}",
          "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}
        }}''')
    return ",\n".join(items)


def build_faq_html(faq_list):
    items = []
    for q, a in faq_list:
        items.append(f'''      <div class="faq-item">
        <button class="faq-q" aria-expanded="false">
          <span>{q}</span>
          <span class="ic"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>
        </button>
        <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
      </div>''')
    return "\n".join(items)


def build_autres_zones(autres_zones, nom):
    btns = [f'<a href="index.html" class="btn btn-ghost">Accueil</a>']
    for href, label in autres_zones:
        if label != nom:
            btns.append(f'<a href="{href}" class="btn btn-ghost">{label}</a>')
    return "\n      ".join(btns)


def build_footer_zones(autres_zones, nom, slug):
    items = [f'<li><a href="index.html">Sarrebourg</a></li>',
             f'<li><a href="agence-web-forbach.html">Forbach</a></li>',
             f'<li><a href="agence-web-sarreguemines.html">Sarreguemines</a></li>']
    current = f'agence-web-{slug}.html'
    for href, label in autres_zones:
        if href != "index.html" and href != "agence-web-forbach.html" and href != "agence-web-sarreguemines.html" and href != current:
            items.append(f'<li><a href="{href}">{label}</a></li>')
    return "\n          ".join(items[:5])


def generate_page(v):
    nom = v["nom"]
    slug = v["slug"]
    dept = v["dept"]
    region_label = v["region_label"]
    area_served_json = str(v["area_served"]).replace("'", '"')
    faq_jsonld = build_faq_jsonld(nom, v["faq"])
    faq_html = build_faq_html(v["faq"])
    autres_zones_html = build_autres_zones(v["autres_zones"], nom)
    footer_zones_html = build_footer_zones(v["autres_zones"], nom, slug)

    html = f'''<!doctype html>
<html lang="fr"><head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="theme-color" content="#0B1526">

  <title>Agence web à {nom} — Digital Dreamsbox | {dept}</title>
  <meta name="description" content="{v['desc_meta']}">
  <link rel="canonical" href="https://{CFG["domain"]}/agence-web-{slug}.html">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="Agence web à {nom} — Digital Dreamsbox">
  <meta property="og:description" content="{v['og_desc']}">
  <meta property="og:url" content="https://{CFG["domain"]}/agence-web-{slug}.html">
  <meta property="og:image" content="https://{CFG["domain"]}/{CFG["og_image"]}">
  <meta property="og:site_name" content="Digital Dreamsbox">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Agence web à {nom} — Digital Dreamsbox">
  <meta name="twitter:description" content="{v['og_desc']}">
  <meta name="twitter:image" content="https://{CFG["domain"]}/{CFG["og_image"]}">

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="favicon.ico" /><link rel="icon" type="image/png" href="favicon-light.png">
  <link rel="apple-touch-icon" href="favicon-light.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=Poppins:wght@400;500;600;700&amp;family=Phudu:wght@400;500;600;700&amp;family=Righteous&amp;family=Baloo+2:wght@400;500;600;700&amp;display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=Phudu:wght@400;500;600;700&family=Righteous&family=Baloo+2:wght@400;500;600;700&display=swap" rel="stylesheet"></noscript>

  <!-- Styles -->
  <link rel="stylesheet" href="styles.css">

  <!-- JSON-LD : WebPage + LocalBusiness + FAQPage -->
  <script type="application/ld+json">
  [
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Agence web à {nom} — Digital Dreamsbox",
      "url": "https://{CFG["domain"]}/agence-web-{slug}.html",
      "description": "Digital Dreamsbox intervient à {nom} pour créer des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de la zone.",
      "inLanguage": "fr",
      "breadcrumb": {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://{CFG["domain"]}/"}},
          {{"@type": "ListItem", "position": 2, "name": "Agence web à {nom}"}}
        ]
      }}
    }},
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Digital Dreamsbox",
      "url": "https://{CFG["domain"]}/",
      "telephone": "{CFG["phone"]}",
      "email": "{CFG["email"]}",
      "priceRange": "€€€",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "{CFG["address"]["street"]}",
        "addressLocality": "{CFG["address"]["city"]}",
        "addressRegion": "{CFG["address"]["region"]}",
        "postalCode": "{CFG["address"]["postal"]}",
        "addressCountry": "{CFG["address"]["country"]}"
      }},
      "areaServed": {area_served_json}
    }},
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
{faq_jsonld}
      ]
    }}
  ]
  </script>

  <!-- Google tag -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga_id"]}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{CFG["ga_id"]}');
    gtag('config', '{CFG["gads_id"]}');
  </script>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={CFG["gtm_id"]}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<div id="pt-overlay"></div>
<script>if(sessionStorage.getItem('pt')){{sessionStorage.removeItem('pt');var _o=document.getElementById('pt-overlay');_o.style.opacity='1';_o.style.pointerEvents='all';setTimeout(function(){{_o.style.transition='opacity 150ms ease-out';_o.style.opacity='0';_o.style.pointerEvents='none';}},60);}}</script>
<div id="bg-blobs"><div class="blob blob-1"></div><div class="blob blob-2"></div><div class="blob blob-3"></div></div>

<!-- HEADER -->
<header class="site-header" role="banner">
  <div class="shell-wide nav">
    <a href="index.html" class="brand" aria-label="Digital Dreamsbox — Accueil">
      <img src="mq02h9of-NVlogo-3d-d_d.png" alt="Logo Digital Dreamsbox" width="46" height="46">
      <span class="brand-text">
        <span class="b1">Digital</span>
        <span class="b2">Dreamsbox</span>
      </span>
    </a>

    <nav class="nav-links" role="navigation" aria-label="Navigation principale">
      <a href="pages/agence.html">Agence</a>
      <a href="pages/services.html">Services</a>
      <a href="pages/galerie.html">Galerie</a>
      <a href="pages/journal.html">Journal</a>
    </nav>

    <div class="nav-cta">
      <a href="tel:{CFG["phone"]}" class="btn btn-ghost nav-call" aria-label="Appeler Digital Dreamsbox">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"></path></svg>
        Appeler
      </a>
      <a href="pages/contact.html" class="btn btn-primary" data-magnet="">
        Nous contacter
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
    </div>

    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"></path></svg>
    </button>
  </div>
</header>

<main id="top">

<!-- HERO -->
<section class="hero" aria-labelledby="hero-title">
  <div class="shell hero-shell">
    <span class="eyebrow reveal">Agence · {nom}, {dept}</span>
    <h1 id="hero-title" class="hero-title reveal" style="--rd:60ms;">
      Votre agence web<br>
      à <span class="accent">{nom}.</span>
    </h1>
    <p class="hero-sub reveal" style="--rd:140ms;">
      {v['hero_sub']}
    </p>
    <div class="hero-ctas reveal" style="--rd:220ms;">
      <a href="pages/contact.html" class="btn btn-primary" data-magnet="">
        Demander un devis
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
      <a href="#methode" class="btn btn-ghost">
        Voir la méthode
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M19 12l-7 7-7-7"></path></svg>
      </a>
    </div>

    <div class="hero-meta reveal" style="--rd:320ms;">
      <div>
        <span class="k">Zone couverte</span>
        <span class="v">{v['zones_label']}</span>
      </div>
      <div>
        <span class="k">Rayon d'intervention</span>
        <span class="v">100 km · Grand Est</span>
      </div>
      <div>
        <span class="k">Délai moyen</span>
        <span class="v">2 à 3 semaines</span>
      </div>
    </div>
  </div>
</section>

<!-- CONTEXTE LOCAL -->
<section class="section-problem" aria-labelledby="context-title-{slug}">
  <div class="shell problem-grid">
    <div>
      <span class="eyebrow reveal">Le contexte</span>
      <h2 id="context-title-{slug}" class="problem-quote reveal" style="--rd:80ms;">
        {v['ctx_title']}
      </h2>
      <p class="body-md reveal" style="--rd:160ms; margin-top:24px; max-width:46ch;">{v['ctx_p1']}</p>
      <p class="body-md reveal" style="--rd:200ms; margin-top:16px; max-width:46ch;">{v['ctx_p2']}</p>
    </div>

    <div class="problem-stack">
      <article class="problem-card reveal from-r">
        <span class="num">01</span>
        <div>
          <h4>« Mes clients me trouvent par bouche à oreille seulement. »</h4>
          <p>C'est bien, jusqu'au jour où le réseau s'épuise. Un site optimisé pour la recherche locale vous amène des clients qui ne vous connaissent pas encore.</p>
        </div>
      </article>
      <article class="problem-card reveal from-r" style="--rd:80ms;">
        <span class="num">02</span>
        <div>
          <h4>« Les clients cherchent sur Google et tombent sur des agences de Metz ou Strasbourg. »</h4>
          <p>Si vous n'êtes pas visible localement, c'est votre concurrent qui capte la demande. On vous positionne sur les requêtes de votre zone.</p>
        </div>
      </article>
      <article class="problem-card reveal from-r" style="--rd:160ms;">
        <span class="num">03</span>
        <div>
          <h4>« J'ai un vieux site fait par un copain, il ne convertit personne. »</h4>
          <p>Un site sans SEO local, sans CTA clair et sans adaptation mobile ne sert à rien. On repart d'une base solide, pensée pour votre clientèle locale.</p>
        </div>
      </article>
      <article class="problem-card reveal from-r" style="--rd:240ms;">
        <span class="num">04</span>
        <div>
          <h4>{v['pb4']}</h4>
          <p>{v['pb4a']}</p>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="section-about" aria-labelledby="services-title-{slug}">
  <div class="shell">
    <div style="text-align:center; max-width:52ch; margin:0 auto 56px;">
      <span class="eyebrow reveal">Ce qu'on fait à {nom}</span>
      <h2 id="services-title-{slug}" class="h-section reveal" style="--rd:60ms;">Quatre leviers,<br>tirés ensemble.</h2>
      <p class="body-md reveal" style="--rd:140ms;">Image de marque, site, publicité et accompagnement. Ce n'est pas quatre métiers séparés : c'est un seul mouvement pour être trouvé, compris et choisi.</p>
    </div>

    <div class="about-facts">
      <div class="about-fact reveal">
        <div class="v" style="font-size:1.1rem; line-height:1.3;">Identité<br>de marque</div>
        <div class="k">Branding</div>
        <div class="d">Logo, palette, typographies, supports. Une image cohérente qui inspire confiance dès le premier regard.</div>
      </div>
      <div class="about-fact reveal" style="--rd:80ms;">
        <div class="v" style="font-size:1.1rem; line-height:1.3;">Site web<br>professionnel</div>
        <div class="k">Création web</div>
        <div class="d">Sites vitrines et e-commerce conçus pour le SEO local, la conversion et la lisibilité mobile.</div>
      </div>
      <div class="about-fact reveal" style="--rd:160ms;">
        <div class="v" style="font-size:1.1rem; line-height:1.3;">Google Ads<br>&amp; SEO local</div>
        <div class="k">Visibilité</div>
        <div class="d">Campagnes Google et référencement ciblés sur votre zone d'activité. Pas de trafic inutile, que des appels et des devis.</div>
      </div>
      <div class="about-fact reveal" style="--rd:240ms;">
        <div class="v" style="font-size:1.1rem; line-height:1.3;">Fiche Google<br>Business</div>
        <div class="k">Pack local</div>
        <div class="d">Optimisation de votre fiche GMB pour ressortir dans le pack local sur "votre métier + {nom}".</div>
      </div>
    </div>
  </div>
</section>

<!-- DIFFÉRENCIATION -->
<section style="padding:64px 0; border-top:1px solid var(--rule);">
  <div class="shell">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:start;">
      <div>
        <span class="eyebrow reveal">Pourquoi nous</span>
        <h2 class="h-section reveal" style="--rd:60ms;">Pas une agence 360.<br>Spécialisés, et fiers de l'être.</h2>
      </div>
      <p class="body-md reveal" style="--rd:120ms; padding-top:20px;">La plupart des agences de la région font de tout : sites web, flyers, marquage véhicule, sérigraphie. Elles sont obligées de diversifier pour survivre. Ce n'est pas notre modèle. On s'est concentrés sur ce qui génère vraiment des clients locaux : création web, visibilité Google, automatisations. Pas d'imprimerie, pas de 360 dilué. Une expertise concentrée sur les leviers qui convertissent.</p>
    </div>
  </div>
</section>

<!-- METHODE -->
<section class="section-process" id="methode" aria-labelledby="process-title-{slug}">
  <div class="shell">
    <div class="process-intro">
      <div>
        <span class="eyebrow reveal">La méthode</span>
        <h2 id="process-title-{slug}" class="h-section science reveal" style="--rd:60ms;">
          Quatre étapes,<br>zéro flou.
        </h2>
      </div>
      <p class="right reveal" style="--rd:140ms;">Vous savez à chaque instant où en est le projet, ce qui est attendu de vous, et ce qui sort. Aucune surprise à la livraison.</p>
    </div>

    <div class="process-controls">
      <div class="process-nav">
        <button type="button" data-proc-prev="" aria-label="Étape précédente">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <button type="button" data-proc-next="" aria-label="Étape suivante">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>
      </div>
    </div>
  </div>

  <div class="process-rail-wrap">
    <div class="process-rail" role="region" aria-label="Étapes du projet">
      <article class="process-card is-active">
        <div>
          <span class="step-num">01</span>
          <span class="duration"><span style="width:6px;height:6px;background:currentColor;border-radius:999px;display:inline-block;"></span>Semaine 1</span>
          <h3>Cadrage</h3>
        </div>
        <div>
          <p>On comprend votre activité, vos clients, votre zone, vos contraintes. On formalise ce qui vous différencie vraiment.</p>
          <ul>
            <li>Entretien de cadrage 90 min</li>
            <li>Analyse de la concurrence locale</li>
            <li>Document de positionnement écrit</li>
          </ul>
        </div>
      </article>
      <article class="process-card">
        <div>
          <span class="step-num">02</span>
          <span class="duration"><span style="width:6px;height:6px;background:currentColor;border-radius:999px;display:inline-block;"></span>Semaines 2–3</span>
          <h3>Stratégie</h3>
        </div>
        <div>
          <p>Plan d'attaque écrit : sur quoi on capitalise, ce qu'on déploie en premier, ce qu'on garde pour plus tard.</p>
          <ul>
            <li>Plan de visibilité 6 mois</li>
            <li>Recommandation branding ou site</li>
            <li>Brief créatif validé ensemble</li>
          </ul>
        </div>
      </article>
      <article class="process-card">
        <div>
          <span class="step-num">03</span>
          <span class="duration"><span style="width:6px;height:6px;background:currentColor;border-radius:999px;display:inline-block;"></span>Semaines 3–4</span>
          <h3>Production</h3>
        </div>
        <div>
          <p>Design, copywriting, développement. Itérations courtes, points hebdomadaires, livraisons en clair.</p>
          <ul>
            <li>2 directions créatives, 1 retenue</li>
            <li>Sprints d'1 semaine, points hebdo</li>
            <li>Maquettes &amp; prototypes cliquables</li>
          </ul>
        </div>
      </article>
      <article class="process-card">
        <div>
          <span class="step-num">04</span>
          <span class="duration"><span style="width:6px;height:6px;background:currentColor;border-radius:999px;display:inline-block;"></span>Semaine 5+</span>
          <h3>Activation</h3>
        </div>
        <div>
          <p>Mise en ligne, fiche Google, campagnes. Suivi des chiffres et ajustements pendant 90 jours.</p>
          <ul>
            <li>Mise en ligne &amp; recette</li>
            <li>Suivi des leads &amp; ajustements</li>
            <li>Tableau de bord mensuel</li>
          </ul>
        </div>
      </article>
    </div>
  </div>

  <div class="shell">
    <div class="process-progress" aria-hidden="true">
      <span class="pdot on"></span>
      <span class="pdot"></span>
      <span class="pdot"></span>
      <span class="pdot"></span>
    </div>
  </div>
</section>

<!-- GMB AUTOMATION -->
<section style="padding:64px 0; border-top:1px solid var(--rule);">
  <div class="shell">
    <div style="text-align:center; max-width:54ch; margin:0 auto 40px;">
      <span class="eyebrow reveal">Service exclusif</span>
      <h2 class="h-section reveal" style="--rd:60ms;">Votre fiche Google active<br>52 semaines par an.</h2>
      <p class="body-md reveal" style="--rd:120ms; margin-top:20px;">Publications, réponses aux avis, photos, mise à jour continue. Vous ne touchez à rien. Vos clients vous trouvent sur Google Maps pendant que vous faites votre métier. Dès 70€/mois.</p>
    </div>
    <div class="about-facts" style="margin-bottom:36px;">
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
        <div class="d">Des entreprises locales ne répondent jamais à leurs avis. C'est votre avance à prendre maintenant.</div>
      </div>
      <div class="about-fact reveal" style="--rd:240ms;">
        <div class="v">70%</div>
        <div class="k">Contactent en 24h</div>
        <div class="d">Des recherches locales débouchent sur un contact dans la journée.</div>
      </div>
    </div>
    <div style="text-align:center;">
      <a href="fiche-google-business-artisan.html" class="btn btn-solid reveal">
        Découvrir le service, dès 70€/mois
        <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
      </a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section-faq" id="faq" aria-labelledby="faq-title-{slug}">
  <div class="shell faq-grid">
    <aside class="faq-side">
      <span class="eyebrow reveal">FAQ</span>
      <h2 id="faq-title-{slug}" class="h-section reveal" style="--rd:60ms;">
        Questions<br>légitimes.
      </h2>
      <p class="body-md reveal" style="--rd:140ms;">{v['faq_intro']}</p>
      <div class="ctas reveal" style="--rd:220ms;">
        <a href="pages/contact.html" class="btn btn-solid">Poser une question</a>
        <a href="tel:+33688848145" class="btn btn-ghost">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2A19.86 19.86 0 0 1 2.08 4.18 2 2 0 0 1 4.07 2h3a2 2 0 0 1 2 1.72 12.5 12.5 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.5 12.5 0 0 0 2.81.7A2 2 0 0 1 22 16.92Z"></path></svg>
          Appeler
        </a>
      </div>
    </aside>

    <div class="faq-list reveal" style="--rd:120ms;">
{faq_html}
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="section-contact" id="contact" aria-labelledby="contact-title-{slug}">
  <div class="shell contact-grid">
    <div class="contact-side">
      <span class="eyebrow reveal">Étape suivante</span>
      <h2 id="contact-title-{slug}" class="reveal" style="--rd:60ms;">
        Parlons<br>de votre <span class="blue">projet.</span>
      </h2>
      <p class="ctxt reveal" style="--rd:140ms;">
        {v['contact_p']}
      </p>
      <div class="contact-actions reveal" style="--rd:220ms;">
        <a href="tel:+33688848145" class="btn btn-primary" data-magnet="">Appeler directement</a>
        <a href="#" class="btn btn-ghost" data-vcard="">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Ajouter au contact
        </a>
      </div>
    </div>

    <div class="contact-card reveal" style="--rd:200ms;">
      <h3>Demander un devis</h3>
      <p class="sub">Réponse écrite sous 24 h ouvrées.</p>
      <form id="contact-form" class="form" novalidate action="https://formspree.io/f/xaqzyzgk" method="POST">
        <div class="field">
          <label for="f-name">Nom &amp; prénom</label>
          <input id="f-name" name="name" type="text" required autocomplete="name">
        </div>
        <div class="field">
          <label for="f-company">Entreprise</label>
          <input id="f-company" name="company" type="text" autocomplete="organization">
        </div>
        <div class="field">
          <label for="f-email">Email</label>
          <input id="f-email" name="email" type="email" required autocomplete="email">
        </div>
        <div class="field">
          <label for="f-phone">Téléphone</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="field">
          <label for="f-need">Le sujet</label>
          <select id="f-need" name="need" required>
            <option value="">Choisir</option>
            <option>Site internet</option>
            <option>Branding / identité</option>
            <option>Google Ads / SEO</option>
            <option>Plusieurs / je ne sais pas encore</option>
          </select>
        </div>
        <div class="field">
          <label for="f-msg">Votre projet en quelques mots</label>
          <textarea id="f-msg" name="message" required></textarea>
        </div>
        <input type="hidden" name="source_page" value="agence-web-{slug}">
        <input type="hidden" name="_next" value="https://digitaldreamsbox.com/pages/merci.html">
        <div class="honeypot" aria-hidden="true">
          <label>Ne pas remplir<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
        </div>
        <div class="form-actions">
          <small>En envoyant, vous acceptez notre politique de confidentialité.</small>
          <button type="submit" class="btn btn-primary">
            Envoyer
            <svg class="arr" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"></path></svg>
          </button>
        </div>
        <div class="form-success" role="status">Message reçu. On revient vers vous sous 24 h ouvrées.</div>
      </form>
    </div>
  </div>
</section>

<!-- AUTRES ZONES -->
<section style="padding:48px 0; border-top:1px solid var(--rule);">
  <div class="shell" style="text-align:center;">
    <span class="eyebrow">Nos autres zones</span>
    <p style="color:var(--muted); margin:12px 0 28px; font-size:0.95rem;">On intervient dans toute la Moselle et le Grand Est.</p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
      {autres_zones_html}
    </div>
  </div>
</section>

</main>

<!-- FOOTER -->
<footer class="site-footer" role="contentinfo">
  <div class="shell">
    <div class="footer-top">
      <div>
        <div class="brand">
          <img src="mq02h9of-NVlogo-3d-d_d.png" alt="" width="46" height="46">
        </div>
        <p class="footer-blurb">Agence de marque &amp; design visuel.</p>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="pages/services.html#branding">Branding</a></li>
          <li><a href="pages/services.html#sites-web">Sites web</a></li>
          <li><a href="pages/services.html#google-ads">Google Ads</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Agence</h5>
        <ul>
          <li><a href="pages/agence.html">Qui sommes-nous</a></li>
          <li><a href="pages/journal.html">Journal</a></li>
          <li><a href="#faq">FAQ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Zones</h5>
        <ul>
          {footer_zones_html}
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="tel:{CFG["phone"]}">{CFG["phone_display"]}</a></li>
          <li><a href="mailto:{CFG["email"]}">{CFG["email"]}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year="">2026</span> Digital Dreamsbox. Tous droits réservés.</span>
      <span><a href="pages/mentions-legales.html">Mentions légales</a> &nbsp;·&nbsp; <a href="pages/confidentialite.html">Politique de confidentialité</a> &nbsp;·&nbsp; <a href="pages/cgv.html">CGV</a></span>
    </div>
  </div>
</footer>

<div class="cookies" role="dialog" aria-label="Cookies">
  <h4>Cookies &amp; mesure d'audience</h4>
  <p>Nous utilisons des cookies pour mesurer l'audience et améliorer le site. Aucun suivi avant votre consentement.</p>
  <div class="actions">
    <button class="reject" type="button">Refuser</button>
    <button class="accept" type="button">Accepter</button>
  </div>
</div>

<script src="script.js" defer></script>
</body></html>'''
    return html


def update_sitemap(slugs):
    sitemap_path = os.path.join(SITE_ROOT, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_urls = []
    for slug in slugs:
        url = f"https://{CFG['domain']}/agence-web-{slug}.html"
        if url not in content:
            new_urls.append(f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>')

    if new_urls:
        content = content.replace("</urlset>", "\n".join(new_urls) + "\n</urlset>")
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Sitemap mis à jour : {len(new_urls)} URL(s) ajoutée(s)")
    else:
        print("Sitemap déjà à jour")


def main():
    generated = []
    for v in VILLES:
        slug = v["slug"]
        filename = f"agence-web-{slug}.html"
        filepath = os.path.join(SITE_ROOT, filename)
        html = generate_page(v)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Généré : {filename}")
        generated.append(slug)

    update_sitemap(generated)
    print(f"\nTerminé : {len(generated)} page(s) générée(s)")


if __name__ == "__main__":
    main()
