from random import randint


def main():
    for i in range(1, 11):
        test_arr = create_random_lst()
        sorted_arr = quicksort(test_arr)
        print(f"Тест №{i}. Несорт.:{test_arr}\nСорт.:{sorted_arr}")


def create_random_lst() -> list[int]:
    return [randint(-100, 100) for _ in range(randint(1, 20))]


def insertion_sort(lst: list[int]) -> list[int]:
    length = len(lst)

    if length <= 1:
        return lst

    for i in range(1, length):
        key = lst[i]  # Запоминает текущий элемент для того, тоюы потом правильно вставить элементы
        j = i - 1
        while j >= 0 and key < lst[j]:  # Двигаем элементы большие ключа на 1 элемент
            lst[j + 1] = lst[j]  # Двишаем элемент вперед
            j -= 1
        lst[j + 1] = key
    return lst


def list_create(lst: list[int]) -> tuple[list[int], list[int], list[int]]:
    main_element = lst[-1]  # Выбираем опорный элемент
    list_m = []  # Больше опорного
    list_l = []  # Меньше опорного
    list_e = []  # Равные опорному
    for element in lst:
        if element > main_element:
            list_m.append(element)
        elif element < main_element:
            list_l.append(element)
        else:
            list_e.append(element)
    return list_m, list_l, list_e


def quicksort(lst: list[int]) -> list[int]:
    list_m, list_l, list_e = list_create(lst)
    # Если длина меньше 10, # то сортируем вствкой

    list_m = quicksort(list_m) if len(list_m) >= 10 else insertion_sort(list_m)

    list_l = quicksort(list_l) if len(list_l) >= 10 else insertion_sort(list_l)

    return list_l + list_e + list_m


if __name__ == "__main__":
    main()
