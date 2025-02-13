classDiagram
    class User {
        - UUID id
        - string name
        - string email
        - string password
        - datetime created_at
        - datetime updated_at
        + authenticate() bool
        + update_profile() void
        + delete_account() void
        + get_places() List<Place>
        + get_reviews() List<Review>
        + get_bookings() List<Booking>
        + get_addresses() List<Address>
    }

    class Place {
        - UUID id
        - string name
        - string description
        - datetime created_at
        - datetime updated_at
        + add_amenity() void
        + remove_amenity() void
        + get_amenities() List<Amenity>
        + get_reviews() List<Review>
        + get_bookings() List<Booking>
        + get_user() User
        + get_address() Address
    }

    class Review {
        - UUID id
        - string text
        - int rating
        - datetime created_at
        - datetime updated_at
        + update_review() void
        + delete_review() void
        + get_place() Place
        + get_user() User
    }

    class Amenity {
        - UUID id
        - string name
        - datetime created_at
        - datetime updated_at
        + get_places() List<Place>
    }

    class Booking {
        - UUID id
        - datetime start_date
        - datetime end_date
        - int price
        - datetime created_at
        - datetime updated_at
        + update_booking() void
        + delete_booking() void
        + get_place() Place
        + get_user() User
    }

    class Address {
        - UUID id
        - string street
        - string city
        - string state
        - string zip
        - datetime created_at
        - datetime updated_at
        + get_place() Place
    }

    User --* Place : "User can have multiple places"
    Place --* Amenity : "Place can have multiple amenities"
    User --* Review : "User can have multiple reviews"
    Place --* Review : "Place can have multiple reviews"
    Amenity --* Place : "Amenity can be associated with multiple places"
    User --* Booking : "User can have multiple bookings"
    Place --* Booking : "Place can have multiple bookings"
    Address --* Place : "Address can be associated with one place"