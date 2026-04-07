class Diary:
    def __init__(self):
        # Loome tühja nimekirja sissekannete jaoks
        self.entries = []
        # Loendur sissekannete nummerdamiseks
        self.counter = 0

    def add_entry(self, text):
        # Suurendame loendurit
        self.counter += 1
        # Lisame sissekande kujul "nr: tekst"
        entry = f"{self.counter}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        # Kontrollime, kas indeks on kehtiv
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
        else:
            print("Vigane indeks!")

    def save(self, filename):
        # Salvestame kõik sissekanded faili
        with open(filename, "w", encoding="utf-8") as f:
            for entry in self.entries:
                f.write(entry + "\n")

    def load(self, filename):
        # Laeme sissekanded failist
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.entries = [line.strip() for line in f]
                # Uuendame loendurit vastavalt sissekannete arvule
                self.counter = len(self.entries)
        except FileNotFoundError:
            print("Faili ei leitud!")

    def print_statistics(self):
        # Arvutame sissekannete arvu
        count = len(self.entries)
        print(f"Sissekannete arv: {count}")

        # Kui sissekandeid pole, väldime nulliga jagamist
        if count == 0:
            print("Keskmine tähemärkide arv: 0")
            return

        # Arvutame keskmise tähemärkide arvu
        total_chars = sum(len(entry) for entry in self.entries)
        average = total_chars / count
        print(f"Keskmine tähemärkide arv: {average:.2f}")

    def __str__(self):
        # Tagastame kõik sissekanded reavahetustega
        return "\n".join(self.entries)


# Näidiskasutus
d = Diary()
d.add_entry("Täna oli ilus ilm.")
d.add_entry("Õppisin programmeerimist.")
d.save("diary.txt")

d.print_statistics()

# Võid ka printida kogu päeviku
print(d)