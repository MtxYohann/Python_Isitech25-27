# 📚 Bibliothèque Numérique - Gestion de Bibliothèque

## 📖 Description du Projet

Bienvenue dans ce projet de **gestion de bibliothèque numérique** ! Développé avec Django, cette application web complète permet aux utilisateurs de naviguer facilement dans une collection de livres, d'auteurs et de catégories. Vous pouvez consulter les détails de chaque livre, vérifier le stock disponible, créer et retourner des emprunts, rechercher des livres ou auteurs, et gérer les emprunts actifs ou en retard. Le système inclut une interface d'administration puissante, une UI moderne avec Bootstrap, et des fonctionnalités avancées comme la pagination, les filtres, et les badges de statut. Idéal pour une petite bibliothèque ou un projet éducatif !

## 🛠️ Technologies Utilisées

Voici les technologies clés utilisées dans ce projet :

- **🐍 Python** : Langage principal (version 3.12).
- **🌐 Django** : Framework web robuste pour le backend (version 6.0).
- **💾 SQLite** : Base de données légère et intégrée à Django.
- **🎨 Bootstrap** : Framework CSS pour une interface utilisateur responsive et moderne (version 5.3).
- **🔧 Git** : Gestion de version pour le développement collaboratif.

### 🚀 Installation et Configuration

Suivez ces étapes pour installer et lancer le projet sur votre machine :

1. **Prérequis** :
   - Installez Python 3.12 depuis [python.org](https://www.python.org/).
   - Installez Git depuis [git-scm.com](https://git-scm.com/).

2. **Clonage du Repository** :
   ```bash
   git clone <https://github.com/MtxYohann/Python_Isitech25-27>
   cd python-avancé
   ```

3. **Création de l'Environnement Virtuel** :
   ```bash
   python -m venv mon-env
   mon-env\Scripts\activate  # Sur Windows
   ```

4. **Installation des Dépendances** :
   ```bash
   pip install django
   ```

5. **Configuration de la Base de Données** :
   - Allez dans le dossier du projet : `cd mon-env\myproject`.
   - Appliquez les migrations :
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

6. **Création d'un Superutilisateur (Optionnel)** :
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancement du Serveur** :
   ```bash
   python manage.py runserver
   ```
   - Ouvrez votre navigateur à `http://127.0.0.1:8000/`.

8. **Tests** :
   - Créez des données via l'admin Django (`/admin/`) ou directement en base pour tester.

## ✨ Fonctionnalités Implémentées (dans l'Ordre de Développement)

Voici les fonctionnalités développées, étape par étape :

1. **📊 Modèles de Données (models.py)** :
   - Modèles : `Book`, `Author`, `Category`, `Loan`.
   - Champs détaillés pour les livres (titre, ISBN, auteur, catégorie, stock dispo/max).
   - Relations `ForeignKey` pour lier les entités.
   - Méthodes `clean()` pour valider (ex. : pas d'emprunt si stock ≤ 0, calcul des pénalités).
   - Méthodes `__str__()` pour un affichage propre.

2. **📝 Formulaires (forms.py)** :
   - `LoanForm` basé sur le modèle `Loan`.
   - Champs : nom complet, email, numéro de carte de l'emprunteur.

3. **👀 Vues de Base (views.py)** :
   - `book_list` : Liste complète des livres avec pagination.
   - `book_detail` : Détails d'un livre spécifique.
   - `author_list` : Liste des auteurs.
   - `author_detail` : Détails d'un auteur.
   - Vues class-based pour les listes (BookListView, etc.).

4. **🔄 Gestion des Emprunts** :
   - `loan_create` : Formulaire POST pour créer un emprunt.
   - Validation du stock disponible et possibilité d'emprunts multiples.
   - Mise à jour automatique du stock après emprunt.
   - `loan_return` : Retour d'un emprunt avec confirmation.
   - Gestion des statuts : emprunté, retourné, en retard.

5. **🎭 Templates HTML et UI** :
   - Templates étendant `base.html` pour une UI cohérente.
   - `book_list.html` : Liste avec recherche, pagination et cartes Bootstrap.
   - `book_detail.html` : Détails + boutons conditionnels pour emprunter.
   - `author_list.html` / `author_detail.html` : Pour les auteurs.
   - `loan_form.html`, `loan_list_active.html`, `loan_list_overdue.html`, etc. : Gestion complète des emprunts.
   - Pages : recherche d'auteurs, livres par catégorie/auteur, à propos, contact.

6. **🛤️ URLs et Routage** :
   - Configuration dans `urls.py` avec namespace 'library' (ex. : `/library/books/<id>/`).

7. **⚠️ Validation et Gestion d'Erreurs** :
   - Gestion des erreurs (livre introuvable, stock insuffisant).
   - Utilisation de `get_object_or_404` et messages d'erreur.

8. **🔧 Interface d'Administration** :
   - Personnalisation de l'admin Django avec inlines, actions, fieldsets.
   - Validations et filtres avancés pour les emprunts et livres.

9. **🏷️ Tags et Filtres Personnalisés (templatetags/library_tags.py)** :
   - `format_isbn` : Formatage des ISBN.
   - `loan_status_badge` : Badges colorés pour le statut des emprunts.
   - `calculate_penalty` : Calcul des pénalités.

10. **🔍 Recherche et Filtrage** :
    - Recherche de livres et auteurs.
    - Filtrage par catégorie et auteur.
    - Pagination sur les listes.

## 🚀 Utilisation

- **Page d'accueil** : `/library/books/` - Liste des livres avec recherche.
- **Détails livre** : `/library/books/<id>/` - Voir et emprunter un livre.
- **Auteurs** : `/library/authors/` - Liste et recherche d'auteurs.
- **Emprunts** : `/library/loans/` - Voir les emprunts actifs, en retard, historique.
- **Admin** : `/admin/` - Interface d'administration (nécessite superutilisateur).

## 🔮 Améliorations Futures

- Authentification utilisateur pour un suivi personnel des emprunts.
- API REST pour intégration mobile.
- Notifications par email pour les retours en retard.
- Statistiques et rapports pour l'admin.