import ex4


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    tournament = ex4.TournamentPlatform()
    dragon = ex4.TournamentCard("Fire Dragon", "dragon_001", 1200)
    wizard = ex4.TournamentCard("Ice Wizard", " wizard_001", 1150)
    tournament.register_card(dragon)
    tournament.register_card(wizard)

    print("Creating tournament match...")
    print("Match result:", tournament.create_match(dragon.player_id,
                                                   wizard.player_id))
    print()

    tournament.get_leaderboard()
    print()

    print("Platform Report:", tournament.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
