from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity | str,
        durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.info["type"] = "Artifact"
        self.info["effect"] = effect
        self.info["durability"] = durability

    def play(self, game_state: dict) -> dict:
        play_result = {
            "card_played": game_state["card_wating"].info["name"],
            "mana_used": game_state["card_wating"].info["cost"],
            "effect": game_state["card_wating"].info["effect"],
        }
        return play_result

    def activate_ability(self) -> dict:
        ability = {'activate ability': self.info["effect"]}
        return ability
