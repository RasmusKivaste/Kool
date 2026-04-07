class CodeBuilder:
  def __init__(self, class_name):
    # Salvestame klassi nime
    self.class_name = class_name
    # Siia salvestame väljad (nimi, väärtus)
    self.fields = []

  def add_field(self, name, value):
    # Lisame uue välja
    self.fields.append((name, value))
    # Tagastame self, et saaks aheldada
    return self

  def __str__(self):
    # Kui välju pole, tagastame lihtsa klassi
    if not self.fields:
      return f"class {self.class_name}:\n  pass"

    # Hakkame klassi stringi ehitama
    lines = []
    lines.append(f"class {self.class_name}:")
    lines.append("")  # tühi rida

    # Konstruktor
    lines.append("  def __init__(self):")
    lines.append("")  # tühi rida

    # Lisame kõik väljad
    for name, value in self.fields:
      lines.append(f"    self.{name} = {value}")

    return "\n".join(lines)


# Näidiskasutus
if __name__ == "__main__":
  cb = CodeBuilder('Person')\
    .add_field('name', '""')\
    .add_field('age', '0')
  print(cb)