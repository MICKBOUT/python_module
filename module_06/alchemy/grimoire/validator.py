
from .spellbook import record_spell  # noqa: F401


def validate_ingredients(ingredients: str) -> str:
    valid_ingredient = {"fire", "water", "earth", "air"}
    ingredients_lst = ingredients.split(' ')

    if any(
        ingredient not in valid_ingredient for ingredient in ingredients_lst
    ):
        return f"{ingredients}, INVALID"
    return f"{ingredients} - VALID"
