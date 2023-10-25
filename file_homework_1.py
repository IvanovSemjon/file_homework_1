from pprint import pprint


file_path = 'recipes.txt'


def read_cooking_book():
    """Читает текстовый файл и возвращает словарь."""
    cook_book = {}
    ingridients = []
    try:
        with open(file_path, encoding='utf-8') as f_obj:
            contents = f_obj.read().split('\n')
            for content in contents:
                ingridients.append(content) # создаём спиисок для дальнейшей работы

            for i, c in enumerate(ingridients): # Ищем строку только с цифровым значением и берем наменование на строку выше
                if c.isdigit ():
                    cook_book[contents[i-1]] = []

                    for ingr in ingridients[i+1:i+int(c)+1]: # определяем строки с ингридиентами через сплит и добавляем их
                        if len(ingr.split('|')) == 3:
                            ing = ingr.split('|')[0]
                            qua = int(ingr.split('|')[1])
                            mea = ingr.split('|')[2]

                            cook_book[contents[i-1]].append({
                                                            'ingredient_name':ing,
                                                            'quantity':qua,
                                                            'measure':mea,
                                                            })
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Убедитесь что файл на месте и повторите ввод.")
    
    return cook_book








pprint(read_cooking_book())




