import ex0


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    card_deck = ex0.CreatureCard("Fire Dragon", 5, ex0.Rarity.LEGENDARY, 7, 5)
    print("CreatureCard Info:")
    print(card_deck.get_card_info())
    print(ex0.CreatureCard("Fire Dragon", 5, "Legendary", 7, 5).get_card_info()
          )
    print()

    mana = 6
    print(f"Playing Fire Dragon with {mana} mana available:")
    print("Playable:", card_deck.is_playable(mana))
    game_state = {"card_wating": card_deck}
    print("Play result:", card_deck.play(game_state))

    card_enemy = ex0.CreatureCard("Goblin Warrior", 3, 'Legendary', 5, 5)
    print(f"{card_deck.info['name']} attacks {card_enemy.info['name']}:")
    print(card_deck.attack_target(card_enemy))
    print()

    mana = 3
    print(f"Testing insufficient mana ({mana} available):")
    print("Playable:", card_deck.is_playable(mana))
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
