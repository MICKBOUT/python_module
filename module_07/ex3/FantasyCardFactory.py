from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    card_dict = {
        "creatures": [
            ("Fire Dragon", 5, 'Legendary', 7, 5),
            ("Goblin Warrior", 2, 'Legendary', 5, 5)],
        "spells": [
            ("fireball", 5, "Rare", '5 damage'),
            ("Lightning", 3, "Rare", '3 damage'),
            ("ice", 2, "Rare", '2 damage')],
        "artifact": [
            ("Rings", 2, 'Rare', 10, 'Permanent: +1 mana per turn'),
            ("Staffs", 2, 'Legendary', 10, 'Permanent: +1 mana per turn'),
            ("Mana Crystal", 2, 'Epic', 10, 'Permanent: +1 mana per turn')],
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        for card in FantasyCardFactory.card_dict["creatures"]:
            if card[0] == name_or_power:
                return CreatureCard(*card)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        for card in FantasyCardFactory.card_dict["spells"]:
            if card[0] == name_or_power:
                return SpellCard(*card)
        raise Exception("Card not found")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        for card in FantasyCardFactory.card_dict["artifact"]:
            if card[0] == name_or_power:
                return ArtifactCard(*card)
        raise Exception("Card not found")

    def create_themed_deck(self, size: int) -> dict:
        if size <= 0:
            raise Exception("You need to have at least one card")
        deck = {key: [] for key in self.get_supported_types()}
        for i in range(size):
            if i % 2 == 0:
                new_card = random.choice(
                    FantasyCardFactory.card_dict["creatures"])
                deck["creatures"].append(self.create_creature(new_card[0]))
            else:
                type_card = random.randint(0, 2)
                if type_card == 0:
                    new_card = random.choice(
                        FantasyCardFactory.card_dict["creatures"])
                    deck["creatures"].append(self.create_creature(new_card[0]))
                elif type_card == 1:
                    new_card = random.choice(
                        FantasyCardFactory.card_dict["spells"])
                    deck["spells"].append(self.create_spell(new_card[0]))
                else:
                    new_card = random.choice(
                        FantasyCardFactory.card_dict["artifact"])
                    deck["artifact"].append(self.create_artifact(new_card[0]))
        return deck

    def get_supported_types(self) -> dict:
        return {key: [elem[0] for elem in value]
                for key, value in FantasyCardFactory.card_dict.items()}
