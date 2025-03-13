INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES
    ('36c9050e-ddd3-4c3b-9731-9f487208bbc1', Admin, HBnB, admin@hbnb.io, '$2a$12$M6b8rmKikihpo5eEkRmcROZI.MMDEFgmfyLL70ULaHDk9r7LvugjO', TRUE),

INSERT INTO amenities (id, name)
VALUES
('', 'Wifi')
('', 'Swimming Pool')
('', 'Air conditioning');

INSERT INTO places (id, title, description, price, latitude, longitude, owner_id)
VALUES
();

INSERT INTO places_amenity (place_id, amenity_id)
VALUES
();


INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES
();
