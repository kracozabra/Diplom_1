from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

# Данные для булочек
correct_bun_names = ['Bun', 'Big-Bada-Bun', 'Булочка с кунжутом']
correct_bun_prices = [0, 10, 123.45]

# Данные для игредиентов
correct_ingredient_names = ['Ketchup', '1000 островов', 'сыр']
correct_ingredient_prices = [0, 10, 123.45]
correct_ingredient_types = [ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING]

# Данные для бургеров
correct_bun = Bun('Bun', 10)
correct_ingredients = [
    Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Cutlet', 50),
    Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Ketchup', 20),
]
