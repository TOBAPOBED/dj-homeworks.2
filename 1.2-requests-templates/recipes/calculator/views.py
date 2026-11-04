from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def show_recipe(request, recipe_name):
    # Получаем рецепт из DATA
    recipe = DATA.get(recipe_name)
    
    # Если рецепт не найден — возвращаем 404
    if recipe is None:
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound('Рецепт не найден')
    
    # Получаем параметр servings из URL (?servings=4)
    servings_str = request.GET.get('servings')
    
    # Если параметр есть — конвертируем в число, иначе 1 порция
    if servings_str is not None:
        servings = int(servings_str)
    else:
        servings = 1
    
    # Умножаем все ингредиенты на количество порций
    recipe_with_servings = {}
    for ingredient, amount in recipe.items():
        recipe_with_servings[ingredient] = amount * servings
    
    # Формируем контекст
    context = {
        'recipe': recipe_with_servings
    }
    
    # Возвращаем шаблон
    return render(request, 'calculator/index.html', context)