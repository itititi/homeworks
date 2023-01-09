import os.path
import os
from pprint import pprint


# Задание 1

def reading_cookbook(filename: str) -> dict:
    with open(filename, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            cook_name = line.strip()
            cook_book[cook_name] = []
            for i in range(int(f.readline())):
                result = f.readline().split(' | ')
                cook_book[cook_name].append({'ingredient_name': result[0],
                                             'quantity': int(result[1]),
                                             'measure': result[2].strip()})
            f.readline()
    return cook_book


pprint(reading_cookbook('cookbook.txt'))


# Задание 2

def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book: dict) -> dict:
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for good in cook_book[dish]:
                if good['ingredient_name'] in result:
                    result[good['ingredient_name']]['quantity'] += good['quantity'] * person_count
                else:
                    result[good['ingredient_name']] = {'measure': good['measure'],
                                                       'quantity': (good['quantity'] * person_count)}

        else:
            print(f'Блюда {dish} нет в книге рецептов =(')
    return result


pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3, cook_book=reading_cookbook('cookbook.txt')))


# Задание 3

def string_count(file: str) -> int:
    with open(file, 'r', encoding="UTF-8") as f:
        return sum(1 for _ in f)


def group_text(file: str, base_path, location):
    result = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        result.append([string_count(os.path.join(base_path, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(result):
        opening_files = open(file_for_writing, 'a', encoding="UTF-8")
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r', encoding="UTF-8") as f:
            counting = 1
            for line in f:
                opening_files.write(f'line in № {counting} in file {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


file_for_writing = os.path.abspath('result.txt')
group_text(file_for_writing, base_path=os.getcwd(), location=os.path.abspath(''))
