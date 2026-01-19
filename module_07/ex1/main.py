import ex1


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    deck = ex1.Deck()
    deck.add_card(ex1.CreatureCard("Fire Dragon", 5, 'Legendary', 7, 5))
    deck.add_card(ex1.ArtifactCard(
        "Mana Crystal", 2, 'Epic', 10, 'Permanent: +1 mana per turn'))
    deck.add_card(ex1.SpellCard(
        "Lightning Bolt", 3, "Rare", 'Deal 3 damage to target'))
    print("Deck stats:", deck.get_deck_stats())
    print()

    print("Drawing and playing cards:\n")
    deck.shuffle()
    while deck.deck:
        card_drew = deck.draw_card()
        print(f"Drew: {card_drew.info['name']} ({card_drew.info['type']})")
        game_state = {"card_wating": card_drew}
        print("Play result:", card_drew.play(game_state))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
