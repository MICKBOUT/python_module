from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from random import random, randint


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name: str, player_id: str, rating: int):
        super().__init__(name, None, "Tournament")
        self.player_id = player_id
        self.base_rating = rating
        self.win = 0
        self.losse = 0

    def play(self, game_state: dict) -> dict:
        ...

    def attack(self, target) -> dict:
        atk = {
            "target": target.info["name"],
            "dmg send": randint(0, 20)
        }
        return atk

    def get_tournament_stats(self) -> dict:
        ...

    def defend(self, incoming_damage: int) -> dict:
        return {"dmg_taken": incoming_damage * random()}

    def get_combat_stats(self) -> str:
        return f"win rate: {self.win / (self.win + self.losse)}"

    def calculate_rating(self) -> int:
        return self.base_rating + ((self.win - self.losse) * 16)

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def update_losses(self, losses: int) -> None:
        self.losse += losses

    def get_rank_info(self) -> dict:
        rank_info = {
            "win": self.win,
            "losse": self.losse,
            "rating": self.calculate_rating()
        }
        return rank_info
