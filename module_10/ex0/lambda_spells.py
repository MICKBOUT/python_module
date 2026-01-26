# Lambda Sanctum Test Data
artifacts = [
    {'name': 'Earth Shield', 'power': 105, 'type': 'armor'},
    {'name': 'Water Chalice', 'power': 117, 'type': 'weapon'},
    {'name': 'Shadow Blade', 'power': 86, 'type': 'armor'},
    {'name': 'Lightning Rod', 'power': 70, 'type': 'weapon'}
]
mages = [
    {'name': 'Morgan', 'power': 74, 'element': 'light'},
    {'name': 'River', 'power': 77, 'element': 'earth'},
    {'name': 'Phoenix', 'power': 56, 'element': 'water'},
    {'name': 'Luna', 'power': 54, 'element': 'shadow'},
    {'name': 'Sage', 'power': 87, 'element': 'shadow'}
]
spells = ['heal', 'freeze', 'fireball', 'earthquake']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
            artifacts,
            key=lambda artifact: artifact['power'],
            reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
            lambda mage: mage["power"] >= min_power,
            mages)
            )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: str('* ') + spell + str(' *'),
        spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])["name"],
        'min_power': min(mages, key=lambda mage: mage['power'])["name"],
        'avg_power': sum(map(lambda mage: mage['power'], mages)) / len(mages)
    }


def main() -> None:
    print("artefact sorted by power in reverse order:")
    print(artifact_sorter(artifacts))
    print()

    print("Dict of mage w/ only w/ more than 'x' power")
    print(power_filter(mages, 12))
    print()

    print("Spell formated")
    print(spell_transformer(spells))
    print()

    print("Dict of stats on mage")
    print(mage_stats(mages))
    print()


if __name__ == "__main__":
    main()
