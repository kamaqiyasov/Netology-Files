import os

def get_recipes_by_files(text):
    cook_book = {}    
    for dishes in text.split('\n\n'):
        lines = dishes.split('\n')
        cook_book[lines[0]] = []
        if not lines[1].isdigit():
            return False
        for i in range(0, int(lines[1])):
            ingridient = lines[i + 2].split(' | ')
            cook_book[lines[0]].append({
                'ingredient_name': ingridient[0],
                'quantity': ingridient[1],
                'measure': ingridient[2]  
            })

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    ingredients = {}
    for dish in dishes:
        if not dish in cook_book:
            return False
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in ingredients:
                ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': ingredients[ingr['ingredient_name']]['quantity'] * int(ingr['quantity'])}
            else:
                ingredients[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}
    return ingredients
    
with open(os.path.join(os.getcwd(), 'recipes.txt'), 'r', encoding='utf-8') as f:
    text = f.read()
  
# cook_book = get_recipes_by_files(text)
# get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_book)