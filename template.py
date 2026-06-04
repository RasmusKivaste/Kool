from abc import ABC


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the index of winning creature
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        c2_alive = self.hit(c1, c2)   # c1 ründab c2
        c1_alive = self.hit(c2, c1)   # c2 ründab c1

        if c1_alive == c2_alive:
            return -1

        if c1_alive:
            return c1_index

        return c2_index

    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack

        if defender.health <= 0:
            return False

        defender.health += attacker.attack
        return True


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health > 0

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health


creatures = [Creature(1, 2), Creature(1, 3)]

game = TemporaryDamageCardGame(creatures)
print(game.combat(0, 1))

creatures = [Creature(1, 2), Creature(1, 3)]

game = PermanentDamageCardGame(creatures)
print(game.combat(0, 1))
print(game.combat(0, 1))