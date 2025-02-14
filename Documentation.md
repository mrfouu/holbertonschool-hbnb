This document provides an overview of the layered architecture employed in the HBnH project, highlighting the separation of concerns across different layers and the key entities involved. This document will delve into the specifics of each layer, the entities they manage, and the design decisions that underpin the architecture.

## Package Diagram

This diagram illustrates a layered architecture for the HBnB project, utilizing interfaces and design patterns to separate concerns across three main layers:

### The 3 layers

- PresentationLayer (User Interface)
Interacts with the business logic through the `ServiceAPI` interface, abstracting the implementation details from the user.
- BusinessLogicLayer (Business Logic)
Contains core business entities: `User`, `Place`, `Review`, `Amenity`.
- PersistenceLayer (Data Persistence)
Manages data access and storage via `DatabaseAccess` and `Repository`.

### Entities

- **User**: Represents a platform user.
- **Place**: Represents a lodging or property.
- **Review**: Represents user reviews for places.
- **Amenity**: Represents available amenities in a place.

````mermaid 
classDiagram
class PresentationLayer {

    +ServiceAPI


}
class BusinessLogicLayer {
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    +DatabaseAccess
    +Repository

}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
````