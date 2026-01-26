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
    ...


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
    
    for i in (5, 6):
        print("cast ")
    print()



if __name__ == "__main__":
    main()
