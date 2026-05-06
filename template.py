from __future__ import annotations

from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players: int) -> None:
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self) -> None:
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def have_winner(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def take_turn(self) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def winning_player(self) -> int:
        raise NotImplementedError


class Chess(Game):
    def __init__(self) -> None:
        super().__init__(2)
        self.max_turns = 10
        self.turn = 1

    def start(self) -> None:
        print(f"Starting a game of chess with {self.number_of_players} players.")

    @property
    def have_winner(self) -> bool:
        return self.turn == self.max_turns

    def take_turn(self) -> None:
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self) -> int:
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()

