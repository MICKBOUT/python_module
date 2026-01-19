from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.info = {
            "name": name,
            "cost": cost,
            "rarity": rarity
        }

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return self.info

    def is_playable(self, available_mana: int) -> bool:
        return self.info["cost"] <= available_mana
