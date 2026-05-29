from typing import Dict, List


def find_most_expensive_weapons(inventory: Dict[str, int], blueprints: Dict[str, Dict]) -> List[str]:
    """
    Находит все оружия, которые можно изготовить из данного инвентаря,
    и которые имеют максимальную стоимость среди возможных.

    :param inventory: Словарь материалов и их количества (например, {"wood": 5, "metal": 3}).
    :param blueprints: Словарь чертежей оружия (например, {"sword": {"materials": {"wood": 2}, "price": 10}}).
    :return: Список названий оружий с максимальной ценой, которые можно создать.
    """
    most_expensive_weapons = []
    max_price = 0

    for weapon_name, weapon_info in blueprints.items():
        materials = weapon_info["materials"]
        price = weapon_info["price"]
        can_craft = True

        for material, required_amount in materials.items():
            if inventory.get(material, 0) < required_amount:
                can_craft = False
                break

        if can_craft:
            if price > max_price:
                max_price = price
                most_expensive_weapons = [weapon_name]
            elif price == max_price:
                most_expensive_weapons.append(weapon_name)

    return most_expensive_weapons
