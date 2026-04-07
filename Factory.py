# Antud klass
class Person:
  def __init__(self, id, name):
    self.id = id
    self.name = name


# Factory klass
class PersonFactory:
  def __init__(self):
    # Loendur ID-de jaoks (algab 0-st)
    self.current_id = 0

  def create_person(self, name):
    # Loome uue Person objekti
    person = Person(self.current_id, name)

    # Suurendame ID-d järgmise inimese jaoks
    self.current_id += 1

    return person


# Näidiskasutus
if __name__ == "__main__":
  factory = PersonFactory()
  p1 = factory.create_person("Anna")
  p2 = factory.create_person("Mark")
  print(p1.id, p1.name)
  print(p2.id, p2.name)