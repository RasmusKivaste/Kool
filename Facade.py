import random

# Generator klass: loob juhuslikud numbrid vahemikus 1-9
class Generator:
  def generate(self, n):
    return [random.randint(1, 9) for _ in range(n)]


# Splitter klass: jagab 2D listi read, veerud ja diagonaalid
class Splitter:
  def split(self, matrix):
    n = len(matrix)
    result = []

    # read
    result.extend(matrix)

    # veerud
    for col in range(n):
      result.append([matrix[row][col] for row in range(n)])

    # peadiagonaal
    result.append([matrix[i][i] for i in range(n)])

    # kõrvaldiagonaal
    result.append([matrix[i][n - 1 - i] for i in range(n)])

    return result


# Verifier klass: kontrollib, kas kõik alamlistide summad on võrdsed
class Verifier:
  def verify(self, lists):
    if not lists:
      return False

    expected = sum(lists[0])
    for lst in lists[1:]:
      if sum(lst) != expected:
        return False
    return True


# Facade klass: MagicSquareGenerator
class MagicSquareGenerator:
  def __init__(self):
    self.generator = Generator()
    self.splitter = Splitter()
    self.verifier = Verifier()

  def generate(self, size):
    while True:
      # Loome size*size juhuslikku listi
      numbers = self.generator.generate(size * size)

      # Muudame selle 2D maatriksiks
      matrix = []
      for i in range(size):
        row = numbers[i*size:(i+1)*size]
        matrix.append(row)

      # Kasutame Splitterit, et saada read, veerud, diagonaalid
      parts = self.splitter.split(matrix)

      # Kasutame Verifierit
      if self.verifier.verify(parts):
        return matrix
      # Kui ei sobi → proovime uuesti


if __name__ == "__main__":
  msg = MagicSquareGenerator().generate(3)
  for row in msg:
    print(row)