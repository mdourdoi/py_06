def validate_ingredients(ingredients: str) -> str:
    if ("fire" in ingredients or
        "water" in ingredients or
        "earth" in ingredients or
            "air" in ingredients):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

# Circular dependancy could happen here if we imported spellbook
# Would cause : validator--calls-->spellbook--calls-->validator etc...
