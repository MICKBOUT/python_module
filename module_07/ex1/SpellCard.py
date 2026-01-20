from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.info["type"] = "Spell"
        self.info["effect_type"] = effect_type

    def play(self, game_state: dict) -> dict:
        play_result = {
            "card_played": game_state["card_wating"].info["name"],
            "mana_used": game_state["card_wating"].info["cost"],
            "effect": game_state["card_wating"].info["effect_type"],
        }
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        targets.info["effect"] = None
