class CombinationLock:
  def __init__(self, combination):
    # Õige kombinatsioon salvestatakse
    self.combination = combination
    # Algolek
    self.status = 'LOCKED'
    # Seni sisestatud numbrid
    self.entered = []

  def enter_digit(self, digit):
    # Kui juba ERROR või OPEN, ei tee midagi
    if self.status in ('OPEN', 'ERROR'):
      return

    # Lisame uue numbri sisestatud listi
    self.entered.append(digit)

    # Kontrollime, kas sisestatud jada algab õigesti
    for i, val in enumerate(self.entered):
      if i >= len(self.combination) or val != self.combination[i]:
        self.status = 'ERROR'
        return

    # Kui sisestatud jada on täielik ja õige
    if len(self.entered) == len(self.combination):
      self.status = 'OPEN'
    else:
      # Muul juhul näitame seni sisestatud numbreid
      self.status = ''.join(str(d) for d in self.entered)


# Näidiskasutus õige kombinatsiooniga
if __name__ == "__main__":
  cl = CombinationLock([1, 2, 3, 4, 5])
  print(cl.status)  # LOCKED

  cl.enter_digit(1)
  print(cl.status)  # 1

  cl.enter_digit(2)
  print(cl.status)  # 12

  cl.enter_digit(3)
  print(cl.status)  # 123

  cl.enter_digit(4)
  print(cl.status)  # 1234

  cl.enter_digit(5)
  print(cl.status)  # OPEN

  # Vale kombinatsioon
  cl2 = CombinationLock([1, 2, 3, 4, 5])
  cl2.enter_digit(1)
  cl2.enter_digit(2)
  cl2.enter_digit(9)
  print(cl2.status)  # ERROR
