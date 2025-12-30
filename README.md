# 📚 Bibliothèque Numérique - Gestion de Bibliothèque

## 📖 Description du Projet

Bienvenue dans ce projet de **gestion de bibliothèque numérique** ! Développé avec Django, cette application web permet aux utilisateurs de naviguer facilement dans une collection de livres, d'auteurs et de catégories. Vous pouvez consulter les détails de chaque livre, vérifier le stock disponible, et créer des emprunts en toute simplicité. Le système veille à ce que les emprunts respectent le stock disponible, empêchant ainsi les erreurs. Idéal pour une petite bibliothèque ou un projet éducatif !

## 🛠️ Technologies Utilisées

Voici les technologies clés utilisées dans ce projet :

- **🐍 Python** : Langage principal (version 3.12).
- **🌐 Django** : Framework web robuste pour le backend (version 6.0).
- **💾 SQLite** : Base de données légère et intégrée à Django.
- **🎨 HTML/CSS** : Templates front-end avec le moteur de Django.

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
   - Méthodes `clean()` pour valider (ex. : pas d'emprunt si stock ≤ 0).
   - Méthodes `__str__()` pour un affichage propre.

2. **📝 Formulaires (forms.py)** :
   - `LoanForm` basé sur le modèle `Loan`.
   - Champs : nom complet, email, numéro de carte de l'emprunteur.

3. **👀 Vues de Base (views.py)** :
   - `book_list` : Liste complète des livres.
   - `book_detail` : Détails d'un livre spécifique.
   - `author_list` : Liste des auteurs.
   - `author_detail` : Détails d'un auteur.

4. **🔄 Vue d'Emprunt (loan_create)** :
   - Formulaire POST pour créer un emprunt.
   - Validation du stock disponible.
   - Mise à jour automatique du stock après emprunt.
   - Redirection vers la page du livre.

5. **🎭 Templates HTML** :
   - `book_list.html` : Liste avec liens.
   - `book_detail.html` : Détails + stock.
   - `author_list.html` / `author_detail.html` : Pour les auteurs.
   - `loan_form.html` : Formulaire d'emprunt.

6. **🛤️ URLs et Routage** :
   - Configuration dans `urls.py` (ex. : `/library/books/<id>/`).

7. **⚠️ Validation et Gestion d'Erreurs** :
   - Gestion des erreurs (livre introuvable, stock insuffisant).
   - Utilisation de `get_object_or_404`.

## Suite à venir