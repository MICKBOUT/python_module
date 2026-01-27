# Higher Realm Test Data
# Use these in your test functions:
test_values = [23, 7, 22]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(ell: str) -> str:
        return f"{spell1(ell)}, {spell2(ell)}"
    return combined


def thunder() -> int:
    """ return 10, the dmg of the thunder """
    return 10


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier() -> int:
        return base_spell() * multiplier
    return amplifier


def mod_2_condition(power: int) -> bool:
    """
    Return if the string only contain number,
    False otherwise.
    """
    return power % 2 == 0


def powerfull_spell(power) -> str:
    return f"{power * 2} dmg done"


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(power: int) -> str:
        if condition(power):
            return spell(power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def chaine(power: int) -> None:
        for index, spell in enumerate(spells):
            print(f"{index + 1} - {spell(power)}")
    return chaine


def main() -> None:

    print("Testing spell combiner...")
    new_spell = spell_combiner(
        lambda target: f"Fireball hit {target}",
        lambda target: f"Heals {target}"
    )
    print("Combined spell result:", new_spell(test_targets[0]))
    print()

    print("Testing power amplifier...")
    mega_thunder = power_amplifier(thunder, 3)
    print("Original:", thunder(), "Amplified:", mega_thunder())
    print()

    print("Testing conditional caster:")
    conditional_spell = conditional_caster(mod_2_condition, powerfull_spell)
    print("Cast invalide:", conditional_spell(5))
    print("Cast valide:", conditional_spell(6))
    print()

    print("Spell chaine")
    first_spell = conditional_caster(
        lambda power: power % 2 == 0,
        lambda power: f"{power * 2} dmg done"
    )
    second_spell = conditional_caster(
        lambda power: power % 3 == 0,
        lambda power: f"{power * 3} dmg done"
    )
    third_spell = conditional_caster(
        lambda power: power % 4 == 0,
        lambda power: f"{power * 4} dmg done"
    )
    print("Testing spell chaine:")
    spell_chaine = spell_sequence([first_spell, second_spell, third_spell])
    print("Cast spell chaine:")
    spell_chaine(6)


if __name__ == "__main__":
    main()
