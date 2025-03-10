```mermaid
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