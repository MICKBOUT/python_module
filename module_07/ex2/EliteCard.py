from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int,
        combat_type: str = "melee"
    ):
        super().__init__(name, cost, rarity)
        self.info["type"] = "Elite"
        self.info["combat_type"] = combat_type
        if attack <= 0:
            raise Exception("attack can't be initialize as a negative value")
        self.info["attack"] = attack
        if health <= 0:
            raise Exception("health can't be initialize as a negative value")
        self.info["health"] = health

    def play(self, game_state: dict[str]) -> dict:
        play_result = {
            "card_played": game_state["card_wating"].info["name"],
            "mana_used": game_state["card_wating"].info["cost"],
            "effect": 'Creature summoned to battlefield',
        }
        return play_result

    def attack(self, target) -> dict:
        attack_res = {
            "attacker": self.info["name"],
            "target": target.info["name"],
            "damage": self.info["attack"],
            "combat_type": self.info["combat_type"]
        }
        target.info["health"] -= self.info["attack"]
        return attack_res

    def defend(self, incoming_damage) -> dict:
        defend_res = {
            "defender": self.info["name"],
            "damage_taken": incoming_damage // 2,
            "damage_blocked": (incoming_damage // 2) + (incoming_damage % 2),
        }
        self.info["health"] -= defend_res["damage_taken"]
        defend_res["still_alive"] = self.info["health"] > 0
        return defend_res

    def get_combat_stats(self) -> dict:
        return {"combat_available": self.info["health"] > 0}

    def cast_spell(self, spell_name: str, targets: List[Card]) -> dict:
        spell_res = {
            "caster": self.info["name"],
            "spell": spell_name,
            "targets": [target.info["name"] for target in targets],
            "mana_used": len(targets) * 2,
        }
        return spell_res

    def channel_mana(self, amount: int) -> dict:
        channel_res = {
            'channeled': amount // 2,
            'total_mana': amount
        }
        return channel_res

    def get_magic_stats(self) -> dict:
        return {"magic_available": self.info["health"] > 0}
