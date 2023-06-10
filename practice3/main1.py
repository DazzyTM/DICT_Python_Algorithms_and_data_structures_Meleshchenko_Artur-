from list1 import List
from list_extra import CustomList
from without_dub import UniqueList
from sorted_date import SortedList


def test_list():
    some_list = List()
    some_list.append(1)
    some_list.append(2)
    some_list.append(3)
    print(some_list)
    print(len(some_list))
    print(some_list[0])
    some_list[0] = 0
    print(some_list)
    some_list.insert(1, 1)
    print(some_list)
    print(some_list.index(2))
    some_list.remove(2)
    print(some_list)


def test_custom_list():
    custom_list = CustomList()
    custom_list.append(1)
    custom_list.append(2)
    custom_list.append(3)
    print(custom_list)
    print(len(custom_list))
    print(custom_list[0])
    custom_list[0] = 0
    print(custom_list)
    custom_list.insert(1, 1)
    print(custom_list)
    print(custom_list.index(2))
    custom_list.remove(2)
    print(custom_list)
    custom_list.extend([4, 5, 6])
    print(custom_list)
    print(custom_list + custom_list)
    print(custom_list * 3)
    print(custom_list.min())
    print(custom_list.max())
    custom_list_copy = custom_list.deepcopy()
    print(custom_list_copy)


def test_unique_list():
    unique_list = UniqueList()
    unique_list.append(1)
    unique_list.append(2)
    unique_list.append(3)
    print(unique_list)
    try:
        unique_list.append(2)
    except ValueError as error:
        print(error)
    unique_list.insert(1, 4)
    print(unique_list)


def test_sorted_list():
    sorted_list = SortedList()
    sorted_list.append(3)
    sorted_list.append(1)
    sorted_list.append(2)
    print(sorted_list)
    try:
        sorted_list.insert(1, 4)
    except NotImplementedError as error:
        print(error)
    print(sorted_list.search(2))
    print(sorted_list.search(5))


if __name__ == "__main__":
    test_list()
    test_custom_list()
    test_unique_list()
    test_sorted_list()
