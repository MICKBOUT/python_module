from typing import Any

# Memory Depths Test Data
initial_powers = [55, 70, 39]
power_additions = [7, 20, 19, 5, 14]
enchantment_types = ['Shocking', 'Earthen', 'Radiant']
items_to_enchant = ['Armor', 'Wand', 'Amulet', 'Shield']


def mage_counter() -> callable:
    count = 0

    def counting() -> int:
        nonlocal count
        count += 1
        return count
    return counting


def spell_accumulator(initial_power: int) -> callable:
    accumulate_power = initial_power

    def accumulating(power_add) -> int:
        nonlocal accumulate_power
        accumulate_power += power_add
        return accumulate_power
    return accumulating


def enchantment_factory(enchantment_type: str) -> callable:
    def enchanting(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanting


def memory_vault() -> dict[str, callable]:
    memory = {}

    def storing(key: str, values: Any) -> None:
        memory[key] = values

    def recalling(key: str) -> Any:
        return memory[key] if key in memory else "Memory not found"

    dico = {
        'store': storing,
        'recall': recalling
    }
    return dico


def main() -> None:
    print("Test mage counter:")
    counter = mage_counter()
    for i in range(3):
        print(f"{i} call: {counter()}")
    print()

    print("Test accumulator:")
    initial_power = initial_powers[0]
    accumulator = spell_accumulator(initial_power)
    print(f"Starting at {initial_power}")
    for i in range(3):
        print(f"Call {i + 1} (+{power_additions[i]}): "
              f"Power = {accumulator(power_additions[i])}")
    print()

    print("Test enchanting:")
    for i in range(min(len(enchantment_types), len(items_to_enchant))):
        enchantment, item = enchantment_types[i], items_to_enchant[i]
        enchanter = enchantment_factory(enchantment)
        print(f"Enchantment: {enchantment}, Item: {item}, "
              f"result: {enchanter(item)}")
    print()

    print("Test memory")
    custom_memory = memory_vault()
    print("recall on empty dict:", custom_memory["recall"]("somewhere"))
    custom_memory["store"]("somewhere", "something")
    print("recall on dict w/ somthing inside:",
          custom_memory["recall"]("somewhere"))


if __name__ == "__main__":
    main()
