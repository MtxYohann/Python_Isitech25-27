# Sujet de TP Fil Rouge - Formation Django

## TP : Système de Gestion de Bibliothèque avec Django

### Vue d'ensemble

Développer une application web complète de gestion de bibliothèque en utilisant le framework Django. L'accent est mis sur l'application de l'architecture MVT, la modélisation relationnelle avec l'ORM Django, et l'implémentation des bonnes pratiques de développement web.

### Contexte métier

Une bibliothèque municipale souhaite moderniser son système de gestion. Le système doit permettre aux bibliothécaires de cataloguer les ouvrages, suivre les emprunts en temps réel, gérer les retards avec pénalités, et fournir des statistiques d'utilisation. Les usagers doivent pouvoir consulter le catalogue et leur historique d'emprunts via une interface web intuitive.

---

## Phase 1 : Modélisation et Architecture

### Modèles de données à concevoir

#### Book (Livre)

Représente un ouvrage dans le catalogue de la bibliothèque.

Attributs requis :
- Identifiant unique automatique
- Titre de l'ouvrage
- Code ISBN au format ISBN-13
- Année de publication
- Relation vers l'auteur
- Nombre d'exemplaires disponibles
- Nombre total d'exemplaires possédés
- Description textuelle
- Catégorie littéraire
- Langue de publication
- Nombre de pages
- Maison d'édition
- Image de couverture
- Date d'ajout au catalogue

Contraintes métier :
- Le nombre d'exemplaires disponibles ne peut jamais dépasser le total
- L'ISBN doit être unique dans le système
- Un livre ne peut être supprimé s'il existe des emprunts actifs
- La méthode __str__ doit retourner le titre
- Validation de l'année de publication entre 1450 et année courante

#### Author (Auteur)

Représente un écrivain ou contributeur.

Attributs requis :
- Identifiant unique automatique
- Prénom
- Nom de famille
- Date de naissance
- Nationalité
- Biographie
- Date de décès
- Site web ou URL de référence
- Photo de l'auteur

Contraintes métier :
- Le nom complet doit être unique
- Un auteur peut avoir écrit plusieurs livres
- Un auteur ne peut être supprimé si des livres lui sont associés
- La méthode __str__ doit retourner le nom complet
- Le related_name pour la relation inverse doit être "books"

#### Loan (Emprunt)

Représente un prêt de livre à un usager.

Attributs requis :
- Identifiant unique automatique
- Relation vers le livre emprunté
- Nom complet de l'emprunteur
- Email de contact de l'emprunteur
- Numéro de carte de bibliothèque
- Date et heure de l'emprunt
- Date limite de retour
- Date et heure de retour effectif
- Statut de l'emprunt
- Commentaires du bibliothécaire

Contraintes métier :
- Un usager ne peut emprunter plus de 5 livres simultanément
- La durée standard d'emprunt est de 14 jours
- La date limite de retour est calculée automatiquement
- Un livre retourné en retard génère une pénalité calculée
- Un livre ne peut être emprunté que s'il reste des exemplaires disponibles
- Utiliser des choix Django pour les statuts
- Le related_name pour la relation inverse doit être configuré

#### Category (Catégorie)

Représente une catégorie littéraire.

Attributs requis :
- Identifiant unique automatique
- Nom de la catégorie
- Description
- Image représentative

Contraintes métier :
- Le nom doit être unique
- Une catégorie peut contenir plusieurs livres
- Définir un ordering par défaut alphabétique

---

## Phase 2 : Configuration du Projet Django

### Structure à créer

Organisation du projet :
- Un projet Django nommé "library_project"
- Une application "library" pour la gestion principale
- Configuration de la base de données SQLite
- Configuration des fichiers statiques et médias
- Configuration des templates
- Mise en place d'un fichier settings_local.py pour les configurations sensibles

### Configuration de base

Éléments à configurer :
- INSTALLED_APPS avec toutes les applications nécessaires
- Configuration de la base de données
- Configuration des chemins STATIC et MEDIA
- Configuration TEMPLATES avec les chemins appropriés
- Configuration de la langue et du fuseau horaire en français
- Configuration des messages Django
- Paramètres de sécurité de base

### Migrations

Processus à suivre :
- Création des migrations initiales
- Application des migrations
- Vérification de la structure de base de données générée
- Documentation des commandes utilisées

---

## Phase 3 : Interface d'Administration Django

### Configuration de l'admin

Personnalisation à implémenter :

#### Admin Book
- Affichage en liste : titre, auteur, ISBN, catégorie, exemplaires disponibles
- Filtres latéraux par catégorie, auteur, année
- Barre de recherche sur titre, ISBN, auteur
- Actions personnalisées pour marquer des livres comme indisponibles
- Configuration des champs en lecture seule
- Organisation des champs par sections
- Inlines pour visualiser les emprunts actifs

#### Admin Author
- Affichage en liste : nom complet, nationalité, date de naissance
- Filtres par nationalité
- Recherche par nom
- Inlines pour visualiser les livres de l'auteur

#### Admin Loan
- Affichage en liste : livre, emprunteur, date d'emprunt, statut
- Filtres par statut, période d'emprunt
- Recherche par nom d'emprunteur, email, numéro de carte
- Action pour marquer comme retourné
- Calcul automatique des pénalités affichées

#### Admin Category
- Configuration simple avec recherche
- Comptage du nombre de livres par catégorie

Fonctionnalités avancées :
- Personnalisation du titre et header de l'admin
- Messages de confirmation personnalisés
- Validation des données avant sauvegarde
- Gestion des erreurs avec messages explicites

---

## Phase 4 : Système de Routage (URLconf)

### URLs du projet

Structure à implémenter :
- Configuration du fichier urls.py racine
- Inclusion des URLs de l'application library
- Configuration de l'accès à l'admin Django
- Configuration pour servir les fichiers médias en développement
- URL de la page d'accueil
- Utilisation des namespaces pour éviter les conflits

### URLs de l'application

Routes à créer :

#### Livres
- Liste de tous les livres avec pagination
- Détail d'un livre spécifique
- Recherche de livres
- Liste des livres par catégorie
- Liste des livres par auteur

#### Auteurs
- Liste de tous les auteurs
- Détail d'un auteur avec ses livres
- Recherche d'auteurs

#### Emprunts
- Liste des emprunts actifs
- Liste des emprunts en retard
- Historique des emprunts d'un usager
- Formulaire de création d'emprunt
- Formulaire de retour de livre

#### Pages statiques
- Page d'accueil
- Page "À propos"
- Page de contact

Contraintes :
- Utilisation de path() pour les URLs simples
- Utilisation de converters appropriés
- Nommage cohérent de toutes les routes
- Organisation logique par fonctionnalité

---

## Phase 5 : Vues et Templates

### Vues basées sur des fonctions

Vues à implémenter :

#### Vues de liste
- Liste paginée des livres avec recherche
- Liste des auteurs
- Liste des emprunts par statut
- Gestion de la pagination
- Gestion des filtres via GET parameters

#### Vues de détail
- Détail d'un livre avec informations complètes
- Détail d'un auteur avec liste de ses ouvrages
- Affichage conditionnel selon la disponibilité

#### Vues de formulaires
- Création d'un nouvel emprunt
- Retour d'un livre
- Recherche avancée de livres
- Validation des données
- Gestion des erreurs de formulaire

### Vues basées sur des classes

Utilisation des Generic Views :
- ListView pour les listes
- DetailView pour les détails
- CreateView pour la création
- UpdateView pour la modification
- Personnalisation via get_queryset()
- Personnalisation via get_context_data()
- Gestion des redirections après actions

### Templates

Structure des templates :

#### Template de base
- Layout principal avec header, footer, navigation
- Blocs pour le contenu principal
- Blocs pour les scripts et styles supplémentaires
- Inclusion de Bootstrap ou framework CSS
- Messages Django pour les notifications

#### Templates de liste
- Affichage en grille ou tableau
- Pagination avec numéros de pages
- Filtres et tri
- Messages si liste vide

#### Templates de détail
- Affichage structuré des informations
- Images de couverture pour les livres
- Boutons d'action contextuels
- Breadcrumb pour la navigation

#### Templates de formulaires
- Structure cohérente pour tous les formulaires
- Affichage des erreurs de validation
- Messages de succès/échec
- Protection CSRF
- Labels et placeholders explicites

### Filtres et tags personnalisés

À créer :
- Filtre pour calculer les jours de retard
- Filtre pour formater l'ISBN
- Tag pour afficher le statut d'un emprunt avec badge coloré
- Tag pour calculer la pénalité de retard
- Tag d'inclusion pour composants réutilisables

---

## Phase 6 : Gestion des Formulaires

### Formulaires Django

Formulaires à implémenter :

#### LoanForm (Emprunt)
- Sélection du livre depuis liste filtrée de livres disponibles
- Champs pour l'emprunteur
- Validation de l'email
- Validation du numéro de carte
- Vérification de disponibilité du livre
- Vérification de la limite de 5 emprunts par usager
- Calcul automatique de la date limite
- Messages d'erreur personnalisés

#### BookSearchForm (Recherche)
- Recherche par titre
- Recherche par auteur
- Filtrage par catégorie
- Filtrage par disponibilité
- Plage d'années de publication
- Utilisation de widgets appropriés

#### ContactForm (Contact)
- Nom, email, sujet, message
- Validation des champs
- Envoi d'email simulé

### Validation

Validations à implémenter :
- Validators personnalisés pour ISBN
- Validation de la cohérence des dates
- Validation métier dans la méthode clean()
- Messages d'erreur en français et explicites

---

## Phase 7 : Règles Métier et Signaux

### Méthodes des modèles

Logique métier à implémenter :

#### Dans Book
- Méthode pour vérifier la disponibilité
- Méthode pour décrémenter les exemplaires disponibles
- Méthode pour incrémenter les exemplaires disponibles
- Méthode pour obtenir les emprunts actifs
- Méthode pour calculer le taux d'occupation

#### Dans Loan
- Méthode pour calculer les jours de retard
- Méthode pour calculer la pénalité
- Méthode pour marquer comme retourné
- Propriété is_overdue pour vérifier le retard
- Méthode pour prolonger l'emprunt

### Signaux Django

Signaux à utiliser :

#### Signal pre_save sur Loan
- Validation de la disponibilité avant création
- Calcul de la date limite de retour
- Vérification de la limite de 5 emprunts

#### Signal post_save sur Loan
- Décrémentation des exemplaires disponibles à la création
- Incrémentation des exemplaires disponibles au retour
- Mise à jour des statistiques

#### Signal post_delete sur Loan
- Libération des exemplaires si suppression

---

## Phase 8 : Fonctionnalités Avancées

### Statistiques

Pages de statistiques à créer :
- Tableau de bord général
- Nombre total de livres, auteurs, emprunts
- Livres les plus empruntés
- Auteurs les plus populaires
- Taux d'occupation de la bibliothèque
- Graphiques de visualisation
- Emprunts par mois sur l'année
- Livres jamais empruntés

### Recherche avancée

Fonctionnalités de recherche :
- Recherche textuelle multi-champs
- Filtres combinables
- Recherche insensible à la casse
- Recherche par mots-clés dans la description
- Tri des résultats par pertinence

### Exports

Fonctionnalités d'export :
- Export de la liste des livres en CSV
- Export des statistiques d'emprunts
- Génération de rapport mensuel
- Export avec encodage UTF-8

### Pagination

Implémentation :
- Pagination sur toutes les listes
- Configuration du nombre d'éléments par page
- Navigation entre pages
- Affichage du nombre total de résultats

---

## Phase 9 : Gestion des Fichiers Statiques et Médias

### Fichiers statiques

Organisation :
- Dossier static dans l'application
- Sous-dossiers pour CSS, JS, images
- Utilisation du tag static dans les templates
- Configuration de STATIC_URL et STATIC_ROOT

### Fichiers médias

Gestion des uploads :
- Configuration de MEDIA_URL et MEDIA_ROOT
- Upload d'images de couverture pour les livres
- Upload de photos pour les auteurs
- Validation du type et de la taille des fichiers
- Affichage conditionnel des images

---

## Phase 10 : Qualité et Bonnes Pratiques

### Structure du code

Organisation recommandée :
- Séparation claire des responsabilités
- Logique métier dans les modèles
- Logique de présentation dans les vues
- Aucune logique dans les templates
- Utilisation de managers personnalisés si nécessaire

### Documentation

Éléments à documenter :
- Docstrings pour toutes les fonctions et classes
- Commentaires pour la logique complexe
- README avec instructions d'installation
- Documentation des choix d'architecture
- Liste des dépendances

### Conventions Django

Conventions à respecter :
- Nommage des URLs en snake_case
- Nommage des vues explicite et cohérent
- Organisation des templates par application
- Utilisation des raccourcis Django
- Gestion appropriée des erreurs 404 et 500

### Tests

Tests à implémenter :
- Tests unitaires des modèles
- Tests des méthodes de calcul
- Tests des validations
- Tests des vues principales
- Tests des formulaires
- Utilisation de fixtures pour les données de test

---

## Livrables Attendus

### Code source

Éléments requis :
- Projet Django complet et fonctionnel
- Structure d'application organisée
- Migrations à jour
- Fichiers requirements.txt avec toutes les dépendances
- Fichier .gitignore approprié pour Django

### Base de données

Fourniture :
- Base de données avec données de démonstration
- Script de peuplement si applicable
- Documentation du schéma de base de données

### Documentation

Documents à fournir :
- README complet avec instructions d'installation
- Guide d'utilisation de l'interface admin
- Documentation des URLs disponibles
- Captures d'écran des principales pages
- Schéma de la base de données

### Interface

Exigences :
- Interface admin Django complètement fonctionnelle
- Interface publique responsive
- Navigation intuitive
- Messages utilisateur clairs
- Gestion des erreurs avec pages appropriées

---

## Critères d'Évaluation

### Architecture MVT

Respect du pattern :
- Séparation claire Modèles / Vues / Templates
- Utilisation appropriée de l'ORM Django
- URLconf bien structuré
- Pas de logique métier dans les templates

### Modèles de données

Qualité de la modélisation :
- Relations correctement définies
- Contraintes métier respectées
- Méthodes de modèles pertinentes
- Utilisation appropriée des champs Django
- Gestion des cascades et related_name

### Interface d'administration

Personnalisation :
- Admin complet et fonctionnel
- Personnalisation adaptée au métier
- Filtres et recherches pertinents
- Actions personnalisées utiles
- Inlines configurés judicieusement

### Vues et Templates

Implémentation :
- Vues fonctionnelles et optimisées
- Templates bien structurés avec héritage
- Réutilisation via includes et tags
- Gestion appropriée des formulaires
- Messages de feedback utilisateur

### Gestion des formulaires

Qualité :
- Validation complète des données
- Messages d'erreur explicites
- Protection CSRF active
- Formulaires ergonomiques
- Gestion des cas d'erreur

### Règles métier

Respect des contraintes :
- Limite de 5 emprunts respectée
- Calcul correct des pénalités
- Gestion atomique de la disponibilité
- Validation de toutes les contraintes métier
- Utilisation appropriée des signaux

### Code et conventions

Bonnes pratiques :
- Code propre et lisible
- Conventions PEP 8 respectées
- Conventions Django respectées
- Nommage explicite et cohérent
- Commentaires et docstrings appropriés

### Fonctionnalités

Complétude :
- Toutes les fonctionnalités de base implémentées
- Recherche fonctionnelle
- Statistiques pertinentes
- Pagination opérationnelle
- Gestion des fichiers médias

### Qualité générale

Aspects transversaux :
- Application stable sans erreurs
- Performance acceptable
- Interface utilisateur cohérente
- Documentation complète
- Tests de base présents

---

## Conseils de Développement

### Approche itérative

Méthodologie recommandée :
- Commencer par les modèles et valider avec makemigrations/migrate
- Configurer l'admin en premier pour tester les modèles
- Créer les URLs et vues de base
- Développer les templates progressivement
- Ajouter les fonctionnalités avancées ensuite

### Utilisation du shell Django

Commandes utiles :
- python manage.py shell pour tester les modèles
- Créer des données de test manuellement
- Tester les méthodes des modèles interactivement
- Déboguer les requêtes ORM

### Debug

Techniques de débogage :
- DEBUG = True en développement
- Utilisation de print() et de Django debug toolbar
- Consultation des logs Django
- Vérification des requêtes SQL générées

### Documentation Django

Ressources à consulter :
- Documentation officielle Django pour les modèles
- Documentation sur l'ORM et les QuerySets
- Documentation sur les vues génériques
- Documentation sur le système de templates
- Tutoriel officiel Django comme référence