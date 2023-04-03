import math
import numpy


def test_greeting(name, age):

    output = f'Привет, {name}! Тебе {age} лет.'

    assert output == 'Привет, Анна! Тебе 25 лет.'
    print(output)


test_greeting('Анна', 25)


def test_rectangle(length, width):

    perimetr = 2 * (length + width)

    assert perimetr == 60
    print(f'Периметр прямоугольника = {perimetr}')

    area = length * width

    assert area == 200
    print(f'Площадь прямоугольника = {area}')


test_rectangle(10, 20)


def test_circle(radius):

    area = math.pi * radius ** 2

    assert area == 1661.9025137490005
    print(f'Площадь круга = {area}')

    length = 2 * math.pi * radius

    assert length == 144.51326206513048
    print(f'Длина круга = {length}')


test_circle(23)


def test_random_list(my_list: list):

    assert len(my_list) == 10
    print(f'Список из случайных чисел = {my_list}')

    my_list.sort()

    assert my_list[0] < my_list[-1]
    print(f'Отсортированный по возрастанию список: {my_list}')


test_random_list(numpy.random.randint(1, 100, 10))


def test_unique_elements(list_to_change: list):

    unique_list = list(set(list_to_change))

    assert isinstance(list_to_change, list)
    assert len(unique_list) == 10
    assert unique_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Список без повторяющихся значений: {unique_list}')


test_unique_elements([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10])


def test_dicts(first_list: list, second_list: list):

    dict_from_lists = dict(zip(first_list, second_list))

    assert isinstance(dict_from_lists, dict)
    assert len(dict_from_lists) == 5
    print(f'Словарь из двух списков: {dict_from_lists}')


test_dicts(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])














