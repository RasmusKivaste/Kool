# Antud klass
class Square:
  def __init__(self, side=0):
    self.side = side

# Antud funktsioon, mis ootab objekt, millel on width ja height
def calculate_area(rc):
  return rc.width * rc.height

# Adapter klass
class SquareToRectangleAdapter:
  def __init__(self, square):
    self.square = square

  @property
  def width(self):
    # width on sama mis square.side
    return self.square.side

  @property
  def height(self):
    # height on sama mis square.side
    return self.square.side


# Näidiskasutus
if __name__ == "__main__":
  sq = Square(5)
  adapter = SquareToRectangleAdapter(sq)
  print(calculate_area(adapter))  # Tulemus: 25