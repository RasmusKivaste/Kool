# Rectangle klass
class Rectangle:
    def __init__(self, width, height):
        # Kasutame "peidetud" atribuute (_width, _height)
        self._width = width
        self._height = height

    # width getter
    @property
    def width(self):
        return self._width

    # width setter
    @width.setter
    def width(self, value):
        self._width = value

    # height getter
    @property
    def height(self):
        return self._height

    # height setter
    @height.setter
    def height(self, value):
        self._height = value

    # Pindala arvutus
    @property
    def area(self):
        return self._width * self._height

    # Tekstiline esitus
    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"


# Square klass (pärib Rectangle'ist)
class Square(Rectangle):
    def __init__(self, size):
        # Mõlemad väärtused on samad
        super().__init__(size, size)

    # Kui muudetakse width, muudetakse ka height
    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value

    # Kui muudetakse height, muudetakse ka width
    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value


# Testfunktsioon (ei muuda!)
def use_shape(shape):
    width = shape.width
    shape.height = 10
    expected = width * 10

    print(f"Expected area: {expected}")
    print(f"Actual area: {shape.area}")
    print()


# Näidiskasutus
if __name__ == "__main__":
    r = Rectangle(2, 3)
    use_shape(r)

    s = Square(5)
    use_shape(s)