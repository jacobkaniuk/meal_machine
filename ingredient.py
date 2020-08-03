from quantity import Quantity
from enum import Enum


class IngredientType(Enum):
    FRUIT       = 1
    VEGETABLE   = 2
    SPICE       = 3
    MEAT        = 4
    FISH        = 5
    DAIRY       = 6
    LIQUID      = 7
    MISC        = 8


class Ingredient(object):
    def __init__(self,
                 _id: int,
                 name: str,
                 quantity: float,
                 quantity_unit: Quantity,
                 serving_size: int,
                 ingredient_type: IngredientType):
        self._id = _id
        self.name = name
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.serving_size = serving_size
        self.ingredient_type = ingredient_type
