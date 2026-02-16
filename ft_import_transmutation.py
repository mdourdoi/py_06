if __name__ == "__main__":
    print()
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    import alchemy.elements
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print()

    print("Method 2 - Specific function import:")
    from alchemy.elements import create_fire
    print("create_fire():", create_fire())
    print()

    print("Method 3 - Aliased imports:")
    from alchemy.potions import healing_potion as heal
    print("heal():", heal())
    print()

    print("Method 4 - Multiple imports:")
    from alchemy.elements import create_fire, create_water
    from alchemy.potions import strength_potion
    print("create_fire():", create_fire())
    print("create_water():", create_water())
    print("strength_potion():", strength_potion())
    print()

    print("All import transmutation methods mastered!")
