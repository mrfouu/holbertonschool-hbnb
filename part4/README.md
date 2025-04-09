# 🏡 HBnB Evolution - Web Project

Bienvenue sur le projet **HBnB Evolution** !

Ce projet est un site web dynamique qui permet aux utilisateurs de :
- Se connecter avec leur compte.
- Consulter une liste d'annonces de logements.
- Filtrer les annonces par prix.
- Voir les détails d’une annonce avec ses équipements et avis.
- Ajouter un avis pour un logement (uniquement si connecté).

## 📁 Structure du projet

server/ ├── images/ │ └── logo.png ├── index.html ├── place.html ├── login.html ├── add_review.html ├── styles.css ├── scripts.js └── README.md

markdown
Copier
Modifier

## 🚀 Installation et Lancement

### Pré-requis

- **Python 3.x** avec Flask installé pour l’API Backend.
- Navigateur web moderne.
- (Optionnel) Extension VSCode : *Live Server* ou tout autre serveur local.

### Étapes pour lancer le front-end

1. Ouvre ton projet dans Visual Studio Code ou un autre éditeur.
2. Clique droit sur le fichier `index.html` et choisis **"Open with Live Server"** *(ou lance-le dans ton navigateur via un serveur local sur `localhost:8000`)*.
3. Connecte-toi via la page de connexion pour obtenir ton token utilisateur.
4. Navigue sur le site 🎉

### Étapes pour lancer l'API (Backend)

1. Assure-toi que ton serveur Flask tourne bien sur `http://localhost:5000`.
2. Vérifie que le CORS est bien configuré dans ton API pour autoriser `http://localhost:8000`.

Exemple pour le lancer :
```bash
python run.py
⚙️ Fonctionnalités
✅ Authentification JWT : Connexion utilisateur avec token sécurisé.

✅ Affichage dynamique des annonces : Données récupérées via API.

✅ Filtrage par prix : Filtre les annonces affichées en fonction du budget.

✅ Détail d’annonce : Vue complète d’un logement avec équipements et avis.

✅ Ajout d’avis : Formulaire d’avis disponible uniquement pour les utilisateurs connectés.

✅ Design responsive : Interface propre et fonctionnelle sur tous les appareils.

📦 API Backend
Les points d’API utilisés dans le projet :

POST /api/v1/auth/login → Connexion utilisateur.

GET /api/v1/places/ → Liste de toutes les annonces.

GET /api/v1/places/:id → Détail d’une annonce spécifique.

POST /api/v1/places/:id/reviews/ → Ajouter un avis (authentification requise).

🧩 Astuces
Les données sont affichées dynamiquement grâce au fichier scripts.js.

Si les annonces ne s’affichent pas, vérifie que l’API est bien en route et que le CORS est activé.

Le formulaire d’ajout d’avis n’est visible que si l’utilisateur est connecté.

Toutes les pages sont construites selon les bonnes pratiques HTML5 et CSS3.

📸 Aperçu du projet
🏠 Page d’accueil
Liste des annonces disponibles avec filtre par prix.

📄 Détail d’une annonce
Vue détaillée d’un logement avec ses équipements et avis existants.

✍️ Ajouter un avis
Formulaire d’avis affiché uniquement pour les utilisateurs connectés.

🔖 Validations
✅ W3C HTML Validator

✅ Fonctionnalités demandées dans le cahier des charges validées

🙌 Contribution
Projet réalisé dans le cadre de la formation Holberton School.

© 2025 HBnB Evolution — Tous droits réservés.