from enum import Enum
from abc import ABCMeta


class Quantity(Enum):
    def __init__(self,
                 amount: float,
                 short_name: str):
        self.amount = amount
        self.short_name = short_name

    @staticmethod
    def convert(input_quantity, from_quantity, to_quantity, output_quantity, short_name: str = 0):
        if not issubclass(from_quantity.__class__, to_quantity.__class__.__bases__):
            raise TypeError("Could not convert from {} to {}. Invalid conversion.".format(
                            from_quantity.__class__.__name__, to_quantity.__class__.__name))
        if from_quantity == to_quantity:
            return
        # read the enum value for the quantity so we can convert correctly (ie. 3 teaspoon is 1 tablespoons)
        if from_quantity > to_quantity:
            return output_quantity(input_quantity.amount * (from_quantity / to_quantity),
                                   short_name=output_quantity.__class__.short_names[short_name])
        else:  # cast as float to make sure we don't truncate since from quantity might not fit whole into to quantity 
            return output_quantity(input_quantity.amount * (float(from_quantity) / float(to_quantity)),
                                   short_name=output_quantity.__class__.short_names[short_name])


class Spoon(Quantity, metaclass=ABCMeta):
    short_names = ['spoon', 'sp']

    def __init__(self,
                 amount: float,
                 short_name: str = short_names[0]):
        super().__init__(amount, short_name)


class Tablespoon(Spoon):
    short_names = ['tbsp', 'tablespoon', 'tbs']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Teaspoon(Spoon):
    short_names = ['tsp', 'teaspoon', 'teas']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Cup(object):
    short_names = ['cup', 'cp', 'Cup']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Piece(object):
    short_names = ['pc', 'piece', 'p']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Gram(Quantity):
    short_names = ['g', 'gram', 'G']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Milligram(Gram):
    short_names = ['mg', 'milligram']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Kilogram(Gram):
    short_names = ['kg', 'kilogram', 'Kg', 'kilo']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Ounce(object):
    short_names = ['oz', 'ounce', 'Oz']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)


class Pound(object):
    short_names = ['lb', 'pound', 'Lb']

    def __init__(self,
                 amount: float,
                 short_name: str):
        super().__init__(amount, short_name)

