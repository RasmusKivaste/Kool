# Baasklass Machine
class Machine:
    def print(self, document):
        # Vaikimisi pole implementeeritud
        raise NotImplementedError("Printimine pole toetatud!")

    def fax(self, document):
        # Vaikimisi pole implementeeritud
        raise NotImplementedError("Faksimine pole toetatud!")

    def scan(self, document):
        # Vaikimisi pole implementeeritud
        raise NotImplementedError("Skaneerimine pole toetatud!")


# Multifunktsionaalne printer
class MultiFunctionPrinter(Machine):
    def print(self, document):
        # Lihtne printimise simulatsioon
        print(f"Prindin: {document}")

    def fax(self, document):
        # Lihtne faksimise simulatsioon
        print(f"Saadan faksi: {document}")

    def scan(self, document):
        # Lihtne skaneerimise simulatsioon
        print(f"Skaneerin: {document}")


# Vanamoodne printer
class OldFashionedPrinter(Machine):
    def print(self, document):
        # Ainuke päriselt toetatud funktsioon
        print(f"Prindin: {document}")

    def fax(self, document):
        # Ei tee midagi (nõutud ülesandes)
        pass

    def scan(self, document):
        # Ei ole toetatud → viskame vea
        raise NotImplementedError("Printer ei saa skaneerida!")


# Testkasutus
if __name__ == "__main__":
    printer = OldFashionedPrinter()
    printer.print("Hello world")      # töötab
    printer.fax("Test document")     # ei tee midagi
    # See viskab vea
    printer.scan("Important document")