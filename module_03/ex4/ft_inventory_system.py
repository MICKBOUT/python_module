alice = {
    "sword": ["weapon", "rare", 1, 500],
    "potion": ["consumable", "common", 5, 50],
    "shield": ["armor", "uncommon", 1, 200],
}

bob = {
    "magic_ring": ["armor", "rare", 1, 250],
}

player_dict = {
    "alice": alice,
    "bob": bob
}


def inventoryValue(inventory: dict) -> int:
    """
    return the value of the inventory of the player
    """
    inventory_value = 0
    for _, _, count, value in inventory.values():
        inventory_value += count * value
    return inventory_value


def inventoryCount(inventory: dict) -> int:
    """
    return the number of the item in the inventory of the player
    """
    inventory_count = 0
    for _, _, count, _ in inventory.values():
        inventory_count += count
    return inventory_count


def displayInventory(inventory: dict) -> None:
    """
    display the inventory of a player
    """
    category_count = dict()
    for name, (category, rarity, count, value) in inventory.items():
        category_count[category] = category_count.get(category, 0) + count
        print(f"{name} ({category}, {rarity}): \
{count}x @ {value} gold each = {count * value} gold")

    print(f"\nInventory value: {inventoryValue(inventory)} gold")
    print(f"Item count: {inventoryCount(inventory)} items")
    # s = "Categories: " +\
    #     ", ".join(f"{key}({value})" for key, value in category_count.items())
    str_categories_count = "Categories:"
    for key, value in category_count.items():
        str_categories_count += f" {key}({value}),"
    print(str_categories_count)


def transaction(donor: dict, receiver: dict, item: str, quantity: int) -> int:
    """
    take (quantity) items for (donor) and give it to (reciver)
    print the result of the transaction and
    return 1 if the transaction has occure or -1 otherwise
    """
    if donor[item][2] < quantity:
        print("Not enough item to give")
        return -1
    donor[item][2] -= quantity
    if item in receiver:
        receiver[item][2] += quantity
    else:
        receiver[item] = \
            donor[item][0], donor[item][1], quantity, donor[item][3]
    if donor[item] <= 0:
        donor.pop(item)
    print("Transaction successful!")
    return 1


def mostValuable(player_dict: dict) -> str:
    """
    return a str w/ the most valuable platyer in the given list
    or "No player found" if no player were found
    """
    most_valuable = (None, float("-inf"))
    for name, inventory in player_dict.items():
        inventory_value = inventoryValue(inventory)
        if inventory_value > most_valuable[1]:
            most_valuable = (name, inventory_value)
    if most_valuable[0] is None:
        return "No player found"
    else:
        return f"{most_valuable[0]} ({most_valuable[1]} gold)"


def mostItems(player_dict: dict) -> str:
    """
    reture the player w/ the bigest number of item
    or "No player found" if no player were found
    """
    most_item = (None, float("-inf"))
    for name, inventory in player_dict.items():
        inventory_value = inventoryCount(inventory)
        if inventory_value > most_item[1]:
            most_item = (name, inventory_value)
    if most_item[0] is None:
        return "No player found"
    else:
        return f"{most_item[0]} ({most_item[1]} items)"


def rareItems(player_dict: dict) -> str:
    """
    return a str containing all rare item present in any invenrory
    """
    rare_items = set()

    for inventory in player_dict.values():
        for name, (_, rarity, _, _) in inventory.items():
            if rarity == "rare":
                rare_items.add(name)
    return f"{rare_items}"[1:-1]


def PlayerInventoryTester():
    """
    a tester that print test for this subject
    """
    print("=== Player Inventory System ===\n")
    displayInventory(alice)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    transaction(alice, bob, "potion", 2)

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion'][2]}")
    print(f"Bob potions: {bob['potion'][2]}")

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {mostValuable(player_dict)}")
    print(f"Most items: {mostItems(player_dict)}")
    print(f"Rarest items: {rareItems(player_dict)}")


if __name__ == "__main__":
    PlayerInventoryTester()
