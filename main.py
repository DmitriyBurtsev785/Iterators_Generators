
# Задание 1


class FlatIterator:
    def __init__(self, current_list):
        self.current_list = current_list # складываем сюда список
        self.cursor = -1 # определяем переменную для прохода по основному списку
        self.list_len = len(self.current_list) # кол-во проходов по основному циклу

    def __iter__(self):
        self.cursor += 1 # начинаем итерацию, увеличиваем переменную для обхода основного списка на 1
        self.nested_cursor = 0 # создаём переменную для обхода внутреннего списка
        return self # возвращаем ссылку на объект класса

    def __next__(self):
        if self.nested_cursor == len(self.current_list[self.cursor]): # если вложенный список дошёл до конца,
          iter(self) #  то, вызываем метод iter(), переходим к следующему вложенному списку
        if self.cursor == self.list_len: # если основной список дошёл до конца,
          raise StopIteration # останавливаем наш итератор
        self.nested_cursor += 1 # о мере итерации увеличиваем на 1 переменную для подсчёта кол-ва итераций по внутренним спискам
        return self.current_list[self.cursor][self.nested_cursor - 1] # возвращаем текущий элемент списка


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

flat_list = [item for item in FlatIterator(list_of_lists)]
print(flat_list)






# Задание 2


import types

list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


def flat_generator(list_of_lists: list):
    for i in list_of_lists:
        for y in i:
            yield y


flat_list = [item for item in flat_generator(list_of_lists)]
print(flat_list)

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()