from enum import Enum

# Loome Color Enum'i
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Loome Size Enum'i
class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# Product klass
class Product:
    def __init__(self, name, color, size):
        # Salvestame toote omadused
        self.name = name
        self.color = color
        self.size = size

# ProductFilter klass
class ProductFilter:
    
    def filter_by_color(self, products, color):
        # Loome nimekirja sobivate toodete jaoks
        result = []
        
        # Läbime kõik tooted
        for p in products:
            # Kontrollime värvi
            if p.color == color:
                result.append(p)
        
        return result

    def filter_by_size(self, products, size):
        # Loome nimekirja sobivate toodete jaoks
        result = []
        
        # Läbime kõik tooted
        for p in products:
            # Kontrollime suurust
            if p.size == size:
                result.append(p)
        
        return result

    def filter_by_size_and_color(self, products, size, color):
        # Loome nimekirja sobivate toodete jaoks
        result = []
        
        # Läbime kõik tooted
        for p in products:
            # Kontrollime nii suurust kui värvi
            if p.size == size and p.color == color:
                result.append(p)
        
        return result


# Näidiskasutus
if __name__ == "__main__":
    products = [
        Product("Apple", Color.GREEN, Size.SMALL),
        Product("Tree", Color.GREEN, Size.LARGE),
        Product("House", Color.BLUE, Size.LARGE)
    ]

    pf = ProductFilter()

    print("Green products:")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(p.name)

    print("Large blue products:")
    for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
        print(p.name)