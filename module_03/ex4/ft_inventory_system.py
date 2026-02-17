from sys import argv

usage = "usage: python3 ft_inventory_system.py <item:value> <item:value> ..."


def parsing_data(data: list[str]) -> bool:
    try:
        inventory = {}
        for d in data:
            nb_colon = d.count(":")
            if nb_colon == 0:
                raise Exception(f'colon (:) Not found in item "{d}"')
            elif nb_colon > 1:
                raise Exception(
                    f'More than 1 colon (:) found in "{d}"')

            item, nb = d.split(':')

            if len(item) == 0:
                raise ValueError("Key must not be empty")
            nb = int(nb)
            if nb <= 0:
                raise ValueError("Item count must be a positive int")

            if item in inventory:
                raise Exception("The item appears more than once in the list.")

            inventory.update({item: nb})
    except ValueError as e:
        print("Data invalid:", e)
    except Exception as e:
        print("Data invalid:", e)
    else:
        return inventory


def inventory_system_analysis(inventory: dict) -> int:
    print("=== Inventory System Analysis ===")
    items_count = sum(count for count in inventory.values())
    print("Total items in inventory:", items_count)
    print("Unique item types:", len(inventory))
    print()
    return items_count


def current_inventory(inventory: dict[str, int], items_count: int
                      ) -> list[str]:
    print("=== Current Inventory ===")
    sorted_item_lst = sorted(
        [item for item in inventory.keys()],
        key=lambda item: inventory.get(item),
        reverse=True
    )
    for item in sorted_item_lst:
        item_count = inventory[item]
        print(
            f"{item}: "
            f"{item_count} unit{'s' if item_count > 1 else ''} "
            f"({round(item_count / items_count * 100, 1)}%)"
        )
    print()
    return sorted_item_lst


def inventory_statistics(inventory: dict[str, int], sorted_item_lst: list
                         ) -> None:
    print("=== Inventory Statistics ===")
    if len(inventory) == 1:
        item = list(inventory.keys())[0]
        item_count = inventory[item]
        print(
            "Only one item in inventory, "
            "the most and least abundant are the same item.")
        print(
            "Only item:",
            item,
            f"({item_count} unit{'s' if item_count > 1 else ''})"
        )
        print()
        return None

    most_abundant = sorted_item_lst[0]
    most_abundant_count = inventory.get(most_abundant)
    print(
        "Most abundant:",
        most_abundant,
        f"({most_abundant_count} unit{'s' if most_abundant_count > 1 else ''})"
    )
    least_abundant = sorted_item_lst[-1]
    least_abundant_count = inventory.get(least_abundant)
    print(
        "Least abundant:",
        least_abundant,
        f"({least_abundant_count} "
        f"unit{'s' if least_abundant_count > 1 else ''})"
    )
    print()


def item_categories(inventory: dict[str, int]) -> None:
    print("=== Item Categories ===")
    abundant = {
        item: count
        for item, count in inventory.items()
        if 10 <= count
    }
    if abundant:
        print("Abundant:", abundant)

    moderate = {
        item: count
        for item, count in inventory.items()
        if 5 <= count < 10
    }
    if moderate:
        print("Moderate:", moderate)

    scarce = {
        item: count
        for item, count in inventory.items()
        if count < 5
    }
    if scarce:
        print("Scarce:", scarce)
    print()
    return scarce


def managment_suggestions(scarce: dict[str, int]):
    print("=== Management Suggestions ===")
    scarce_lst = list(key for key, count in scarce.items() if count == 1)
    if not scarce_lst:
        print("No Restock Needed")
    else:
        print("Restock needed:", scarce_lst)
    print()


def dictionary_properties_demo(inventory: dict[int, str]) -> None:
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory)}")
    print("Dictionary values:", str(list(inventory.values()))[1:-1])
    item = 'sword'
    print(f"Sample lookup - '{item}' in inventory:", item in inventory)


def manage_inventory(inventory: dict) -> None:
    items_count = inventory_system_analysis(inventory)
    sorted_item_lst = current_inventory(inventory, items_count)
    inventory_statistics(inventory, sorted_item_lst)
    scarce = item_categories(inventory)
    managment_suggestions(scarce)
    dictionary_properties_demo(inventory)


def main() -> None:
    if len(argv) == 1:
        print(usage)
        return None

    inventory = parsing_data(argv[1:])
    if inventory is None:
        print(usage)
        return None

    manage_inventory(inventory)


if __name__ == "__main__":
    main()
