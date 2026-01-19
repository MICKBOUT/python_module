from ex0.Card import Card
from random import shuffle as deck_shuffle


class Deck:
    def __init__(self):
        self.deck: list = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        base_len = len(self.deck)
        self.deck = [
            card for card in self.deck if card.info["name"] == card_name]
        return base_len > len(self.deck)

    def shuffle(self) -> None:
        deck_shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop()

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        avg = 0
        avg_count = 0
        for card in self.deck:
            card_type = card.info["type"]
            if card_type == "Artifact":
                artifacts += 1
            else:
                avg += card.info["cost"]
                avg_count += 1
                if card_type == "Creature":
                    creatures += 1
                elif card_type == "Spell":
                    spells += 1

        deck_info = {
            "total_cards": len(self.deck),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "cost": (avg / avg_count) if avg_count > 0 else 0,
        }
        return deck_info
