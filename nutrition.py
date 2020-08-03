class NutritionalContent(object):
    def __init__(self,
                 calories: int,
                 fat: float,
                 saturated_fat: float,
                 trans_fat: float,
                 protein: float,
                 carbohydrate: float,
                 cholesterol: float,
                 sodium: float):
        self.calories = calories
        self.fat = fat
        self.saturated_fat = saturated_fat
        self.trans_fat = trans_fat
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.cholesterol = cholesterol
        self.sodium = sodium
        
    def get_quantity(self) -> dict:
        pass

    def get_nutritional_value(self) -> dict:
        pass


class Supplement(object):
    def __init__(self,
                 name: str,
                 amount: int,
                 daily_value: float):
        self.name = name
        self.amount = amount
        self.daily_value = daily_value


class Vitamin(Supplement):
    def __init__(self, name: str,
                 amount: int,
                 daily_value: float):
        super().__init__(name, amount, daily_value)


class Mineral(Supplement):
    def __init__(self, name: str,
                 amount: int,
                 daily_value: float):
        super().__init__(name, amount, daily_value)
