def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validate = validate_ingredients(ingredients)
    if validate[-7:] == "- VALID":
        return f"Spell recorded: {spell_name} {validate}"
    return f"Spell rejected: {spell_name} {validate}"
