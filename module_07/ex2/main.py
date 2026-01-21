import ex2


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    elite_card = ex2.EliteCard("Arcane Warrior", 10, ex2.Rarity.LEGENDARY,
                               5, 10)
    print("Attack result:",
          elite_card.attack(ex2.EliteCard("Enemy", 3, ex2.Rarity.COMMON,
                                          5, 10)))
    print("Defense result:", elite_card.defend(5))
    print()

    print("Magic phase")
    Enemy1 = ex2.EliteCard("Enemy1", 3, ex2.Rarity.COMMON, 5, 10)
    Enemy2 = ex2.EliteCard("Enemy2", 3, ex2.Rarity.COMMON, 5, 10)
    print("spell cast:", elite_card.cast_spell("Fireball", [Enemy1, Enemy2]))
    print("Mana channel:", elite_card.channel_mana(7))


if __name__ == "__main__":
    main()
