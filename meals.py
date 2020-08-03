class Meal(object):
    def __init__(self,
                 _id: int,
                 name: str,
                 description: str,
                 servings: int,
                 prep_time: int,
                 cooking_time: int,
                 total_time: int,
                 ingredients: list,
                 preparation_steps: list,
                 thumbnails: list):
        self._id = _id
        self.name = name
        self.description = description
        self.servings = servings
        self.prep_time = prep_time
        self.cooking_time = cooking_time
        self.total_time = total_time
        self.ingredients = ingredients
        self.preparation_steps = preparation_steps
        self.thumbnails = thumbnails

    def get_ingredients(self) -> list:
        return self.ingredients

    def get_nutritional_facts(self) -> dict:
        pass

    def get_similar_meals(self) -> list:
        pass
    
    
class MealCalculator(object):
    def __init__(self, meals: list, meal_count: int):
        self.meals = meals
        self.meal_count = meal_count
        
    def validate_meals(self) -> bool:
        pass

    def calculate_nutrition_facts(self) -> dict:
        pass

    def calculate_ingredients_list(self) -> list:
        """
        Get all
        :return:
        """
        pass

    def calculate_costs(self, Meal) -> dict:
        """
        Calculate rough cost of all ingredients in meal, return each price for ingredient as
        key, value, return total cost at end
        :return:
        """
        pass
