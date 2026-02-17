def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    if validate_ingredients(ingredients):
        ret = f"Spell recorded: {spell_name} "
        ret += f"({validate_ingredients(ingredients)})"
        return ret
    ret = f"Spell rejected: {spell_name} ({validate_ingredients(ingredients)})"
    return ret
