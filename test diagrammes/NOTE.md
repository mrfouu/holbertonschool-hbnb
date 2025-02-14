### **Document Technique - Couche Logique Métier**

---

#### **Introduction**

Ce document présente une description détaillée du diagramme de classes pour la couche logique métier du projet **HBnB**. Ce diagramme illustre les principales entités du système, leurs attributs, leurs méthodes, et leurs relations.  
L’objectif de cette section est d’expliquer en détail la structure de la couche logique métier, en mettant en avant les choix de conception et leur intégration dans l’architecture globale.

---

### **Diagramme de Classes**

#### **Diagramme**

Le diagramme ci-dessous représente les classes principales, leurs attributs, leurs méthodes, ainsi que leurs relations :
```
classDiagram
	class User {
        - string first_name
        - string last_name
        - string email
        - string password
        - boolean is_admin
        + register() void
        + update_profile() void
        + delete() void
    }
    class Place {
        - string title
        - string description
        - float price
        - float latitude
        - float longitude
        - User owner
        - List<Amenity> amenities
        + create() void
        + update() void
        + delete() void
        + list() void
    }
    class Amenity {
        - string name
        - string description
        + create() void
        + update() void
        + delete() void
        + list() void
    }
    class Review {
        - int rating
        - string comment
        - User user
        + create() void
        + update() void
        + delete() void
        + list_by_place() void
    }
    
    User --* Place : "User can have multiple places"
    Place --* Amenity : "Place can have multiple amenities"
    Place --* Review : "Place can have multiple reviews"
    Review --* User : "Review is associated with one user"
```



---

### **Explications Détailées**

#### **Classe User**

- **Attributs** :
    
    - `first_name`, `last_name` : Informations personnelles de l’utilisateur.
    - `email` : Utilisé comme identifiant unique pour l’authentification.
    - `password` : Stocké sous forme hachée pour garantir la sécurité.
    - `is_admin` : Booléen indiquant si l’utilisateur possède des privilèges administratifs.
- **Méthodes** :
    
    - `register()` : Permet à un utilisateur de s’inscrire.
    - `update_profile()` : Met à jour les informations personnelles de l’utilisateur.
    - `delete()` : Supprime le compte utilisateur.
- **Relations** :
    
    - Association avec `Place` : Un utilisateur peut posséder plusieurs lieux.

---

#### **Classe Place**

- **Attributs** :
    
    - `title`, `description` : Informations descriptives sur le lieu.
    - `price` : Prix de la location du lieu.
    - `latitude`, `longitude` : Coordonnées géographiques pour la localisation.
    - `owner` : Référence à l’utilisateur propriétaire du lieu.
    - `amenities` : Liste des commodités associées au lieu.
- **Méthodes** :
    
    - `create()`, `update()`, `delete()` : Opérations CRUD pour la gestion des lieux.
    - `list()` : Liste les lieux disponibles.
- **Relations** :
    
    - Association avec `Amenity` : Un lieu peut offrir plusieurs commodités.
    - Association avec `Review` : Un lieu peut recevoir plusieurs avis.

---

#### **Classe Amenity**

- **Attributs** :
    
    - `name` : Nom de la commodité (ex. WiFi, piscine).
    - `description` : Détail sur la commodité.
- **Méthodes** :
    
    - `create()`, `update()`, `delete()` : Opérations CRUD pour gérer les commodités.
    - `list()` : Liste les commodités disponibles.
- **Relations** :
    
    - Association avec `Place` : Une commodité est liée à un ou plusieurs lieux.

---

#### **Classe Review**

- **Attributs** :
    
    - `rating` : Note donnée au lieu (ex. de 1 à 5).
    - `comment` : Avis écrit par l’utilisateur.
    - `user` : Référence à l’utilisateur ayant laissé l’avis.
- **Méthodes** :
    
    - `create()`, `update()`, `delete()` : Opérations CRUD pour gérer les avis.
    - `list_by_place()` : Liste les avis associés à un lieu.
- **Relations** :
    
    - Association avec `Place` : Un avis est lié à un lieu unique.
    - Association avec `User` : Un avis est écrit par un utilisateur unique.

---

### **Décisions de Conception**

1. **Séparation des responsabilités** :  
    Chaque classe est responsable de la gestion de ses propres données et de ses opérations associées (principe SRP).
    
2. **Relations entre classes** :
    
    - Les associations permettent de représenter les relations réelles entre les entités (ex. un lieu a des avis et des commodités).
    - Une agrégation a été choisie entre `Place` et `Amenity` pour indiquer une relation logique sans dépendance forte.
3. **Sécurité** :  
    Les informations sensibles telles que `password` sont gérées avec soin (ex. hachage).
    

---

### **Conclusion**

Ce diagramme de classes fournit une base solide pour implémenter la logique métier du projet HBnB. Il garantit une structure claire, extensible et en accord avec les bonnes pratiques de conception.  
Les relations bien définies facilitent la navigation entre les entités.

by: Bryan Weinegaessel