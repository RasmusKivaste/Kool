def is_singleton(factory):
  # Kutsume factory funktsiooni kaks korda
  obj1 = factory()
  obj2 = factory()

  # Kontrollime, kas tegemist on täpselt sama objektiga
  return obj1 is obj2


if __name__ == "__main__":
  class Demo:
    pass

  def factory_singleton():
    if not hasattr(factory_singleton, "_instance"):
      factory_singleton._instance = Demo()
    return factory_singleton._instance

  def factory_transient():
    return Demo()

  print(is_singleton(factory_singleton))  # True
  print(is_singleton(factory_transient))  # False