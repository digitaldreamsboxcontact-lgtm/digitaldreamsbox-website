#!/usr/bin/env python3
"""
Génère les pages SEO locales pour toutes les villes cibles de Digital Dreamsbox.
Exécuter depuis la racine du site : python3 scripts/generate_villes.py
"""

import os
from datetime import date

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()

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
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-T9M3KKHB');</script>
<!-- End Google Tag Manager -->

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
  <meta name="theme-color" content="#0B1526">

  <title>Agence web à {nom} — Digital Dreamsbox | {dept}</title>
  <meta name="description" content="{v['desc_meta']}">
  <link rel="canonical" href="https://digitaldreamsbox.com/agence-web-{slug}.html">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="Agence web à {nom} — Digital Dreamsbox">
  <meta property="og:description" content="{v['og_desc']}">
  <meta property="og:url" content="https://digitaldreamsbox.com/agence-web-{slug}.html">
  <meta property="og:image" content="https://digitaldreamsbox.com/assets/logo-full.jpg">
  <meta property="og:site_name" content="Digital Dreamsbox">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Agence web à {nom} — Digital Dreamsbox">
  <meta name="twitter:description" content="{v['og_desc']}">
  <meta name="twitter:image" content="https://digitaldreamsbox.com/assets/logo-full.jpg">

  <!-- Favicon -->
  <link rel="icon" type="image/x-icon" href="favicon.ico" /><link rel="icon" type="image/png" href="favicon-light.png">
  <link rel="apple-touch-icon" href="favicon-light.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@400;500;600;700&family=Phudu:wght@400;500;600;700&family=Righteous&family=Baloo+2:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="styles.css">

  <!-- JSON-LD : WebPage + LocalBusiness + FAQPage -->
  <script type="application/ld+json">
  [
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "Agence web à {nom} — Digital Dreamsbox",
      "url": "https://digitaldreamsbox.com/agence-web-{slug}.html",
      "description": "Digital Dreamsbox intervient à {nom} pour créer des sites web, identités visuelles et campagnes Google Ads pour les artisans et PME de la zone.",
      "inLanguage": "fr",
      "breadcrumb": {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://digitaldreamsbox.com/"}},
          {{"@type": "ListItem", "position": 2, "name": "Agence web à {nom}"}}
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
      "priceRange": "€€€",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Sarrebourg",
        "addressRegion": "Moselle",
        "postalCode": "57400",
        "addressCountry": "FR"
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
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T9M3KKHB" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
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
      <a href="tel:+33688848145" class="btn btn-ghost nav-call" aria-label="Appeler Digital Dreamsbox">
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
          <li><a href="tel:+33688848145">06 88 84 81 45</a></li>
          <li><a href="mailto:contact@digitaldreamsbox.com">contact@digitaldreamsbox.com</a></li>
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
        url = f"https://digitaldreamsbox.com/agence-web-{slug}.html"
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
