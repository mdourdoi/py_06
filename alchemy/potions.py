def healing_potion() -> str:
    from .elements import create_fire, create_water

    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    from .elements import create_fire, create_earth

    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water

    ret = f"Invisibility potion brewed with {create_air()} "
    ret += f"and {create_water()}"
    return ret


def wisdom_potion() -> str:
    from .elements import create_fire, create_earth, create_water, create_air

    ret = "Wisdom potion brewed with all elements:"
    ret += f" {create_earth()} - {create_fire()} "
    ret += f"- {create_air()} - {create_water()}"
    return ret
