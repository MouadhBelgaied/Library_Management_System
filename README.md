<p align="center">
  <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="Django" width="200"/>
</p>

# Library Management System - MVP

MVP d’un système de gestion de librairie avec Django et SQLite. Permet login/logout, CRUD de livres et catégories, recherche et statistiques. Interface responsive en HTML, CSS, JavaScript et Bootstrap.

## Architecture Django

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*XohhamnRotq53fQaY5HQfA.png" alt="Architecture Django MVT" width="700"/>
</p>

Cette image illustre l’architecture **MVT (Model-View-Template)** de Django :
- **Modèle (Model)** : Gestion de la base de données
- **Vue (View)** : Logique de traitement des requêtes et réponses
- **Template** : Affichage des données à l’utilisateur

## Fonctionnalités

- Authentification utilisateur : Login / Logout
- CRUD Livre : Ajouter, Afficher, modifier et supprimer des livres
- CRUD Catégorie : Ajouter, Afficher, modifier et supprimer des catégories
- Recherche : Rechercher des livres par titre ou catégorie
- Statistiques :
  - Nombre total de livres
  - Nombre de livres par catégorie
  - Total des profits
  - Profits générés par les ventes et les locations

## Technologies Utilisées

- Backend : Django
- Base de données : SQLite
- Frontend : HTML, CSS, JavaScript, Bootstrap
