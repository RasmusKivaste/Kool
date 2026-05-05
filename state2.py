class CombinationLock:
    def __init__(self, combination):
        self._combination = list(combination)
        self.status = "LOCKED"
        self._entered = []

    def enter_digit(self, digit):
        if self.status in ("OPEN", "ERROR"):
            return

        self._entered.append(digit)
        length = len(self._entered)

        if self._entered == self._combination[:length]:
            if length == len(self._combination):
                self.status = "OPEN"
            else:
                self.status = "".join(str(d) for d in self._entered)
        else:
            self.status = "ERROR"


if __name__ == "__main__":
    cl = CombinationLock([1, 2, 3, 4, 5])
    print(cl.status)

    for d in [1, 2, 3, 4, 5]:
        cl.enter_digit(d)
        print(cl.status)

    cl2 = CombinationLock([1, 2, 3, 4, 5])
    for d in [1, 2, 9]:
        cl2.enter_digit(d)
    print(cl2.status)
