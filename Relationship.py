from enum import Enum

# Person klass
class Person:
    def __init__(self, name):
        # Salvestame inimese nime
        self.name = name


# Relationship Enum
class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


# Relationships klass
class Relationships:
    def __init__(self):
        # Siia salvestame kõik seosed (tuple kujul)
        self.relations = []

    def add_parent_and_child(self, parent, child):
        # Lisame kaks seost:
        # parent -> child
        self.relations.append((parent, Relationship.PARENT, child))
        # child -> parent
        self.relations.append((child, Relationship.CHILD, parent))


# Research klass
class Research:
    def __init__(self, relationships):
        # Läbime OTSE relationships.relations nimekirja
        for r in relationships.relations:
            person1, relation, person2 = r

            # Leiame Johni lapsed
            if person1.name == "John" and relation == Relationship.PARENT:
                print(f"John has a child called {person2.name}")


# Näidiskasutus
if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)