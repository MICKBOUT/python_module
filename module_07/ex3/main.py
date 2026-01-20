import ex3


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    fantasy_factory = ex3.FantasyCardFactory()
    strategy = ex3.AggressiveStrategy()
    print("Factory: FantasyCardFactory")
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", fantasy_factory.get_supported_types())
    print()

    print("Simulating aggressive turn...")
    engine = ex3.GameEngine()
    engine.configure_engine(fantasy_factory, strategy)
    enemy = ex3.CreatureCard("Enemy Player", 3, 'Legendary', 5, 5)
    engine.battlefield.append(enemy)

    Actions = engine.simulate_turn()
    print("Actions:", Actions)

    print("Game Report:", engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

    if len(engine.battlefield) == 0:
        print("End of combat")


if __name__ == "__main__":
    main()
