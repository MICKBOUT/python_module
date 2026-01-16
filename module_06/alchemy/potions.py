from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"{create_fire()} and "
            f"{create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"{create_earth()} and "
            f"{create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with "
            f"{create_air()} and "
            f"{create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: "
            f"{create_fire()}, "
            f"{create_water()}, "
            f"{create_earth()} and "
            f"{create_air()}")
