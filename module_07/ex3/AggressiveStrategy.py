from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        played = hand[:2]
        target = self.prioritize_targets(battlefield)[0]
        hand = hand[2:]
        actions = {
            "cards_played": [card.info["name"] for card in played],
            "mana_used": sum(card.info["cost"] for card in played),
            "targets_attacked": [target.info["name"]],
        }

        damage_dealt = 0
        for card in played:
            if card.info["type"] == "Creature":
                damage_dealt += card.info["attack"]
            elif card.info["type"] == "Spell":
                dmg_str = card.info["effect_type"]
                dmg = int(dmg_str[:dmg_str.index(' ')])
                damage_dealt += dmg
        actions["damage_dealt"] = damage_dealt

        target.info["health"] -= actions["damage_dealt"]
        if target.info["health"] <= 0:
            battlefield.remove(target)
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """
        play low cost card first
        """
        return sorted(available_targets, key=lambda x: x.info["cost"],
                      reverse=True)
