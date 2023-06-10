import copy


class CustomList:
    def __init__(self):
        self.size = 0
        self.array = {}

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr([self.array[i] for i in range(self.size)])

    def __getitem__(self, index):
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне допустимого диапазона")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне допустимого диапазона")
        self.array[index] = value

    def __iter__(self):
        return iter(self.array)

    def __next__(self):
        raise NotImplementedError

    def __delitem__(self, index):
        del self.array[index]

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return self.array == other.array
        if isinstance(other, list):
            return list(self.array.values()) == other
        return False

    def append(self, value):
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне допустимого диапазона")
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.size += 1

    def index(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        raise ValueError("Значение не найдено")

    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j+1]
                del self.array[self.size - 1]
                self.size -= 1
                return
        raise ValueError("Значение не найдено")

    def clear(self):
        self.array.clear()
        self.size = 0

    def copy(self):
        copied_list = CustomList()
        copied_list.extend(self)
        return copied_list

    def extend(self, other):
        if hasattr(other, "__iter__"):
            for item in other:
                self.append(item)
        else:
            raise TypeError("Недопустимый тип расширения. Ожидайте повторения.")

    def reverse(self):
        for first_var in range(self.size // 2):
            second_var = self.size - first_var - 1
            self.array[first_var], self.array[second_var] \
                = self.array[second_var], self.array[first_var]

    def count(self, value):
        count = 0
        for i in range(self.size):
            if self.array[i] == value:
                count += 1
        return count

    def __add__(self, other):
        if hasattr(other, "__iter__"):
            new_list = CustomList()
            new_list.extend(self)
            new_list.extend(other)
            return new_list
        raise TypeError("Недопустимый тип расширения. Ожидайте CustomList.")

    def __mul__(self, other):
        if isinstance(other, int):
            new_list = CustomList()
            for _ in range(other):
                new_list.extend(self)
            return new_list
        raise TypeError("Недопустимый тип для умножения. Ожидайте целое число")

    def min(self):
        if self.size == 0:
            raise ValueError("Список пуст")
        min_value = self.array[0]
        for i in range(1, self.size):
            if self.array[i] < min_value:
                min_value = self.array[i]
        return min_value

    def max(self):
        if self.size == 0:
            raise ValueError("Список пуст")
        max_value = self.array[0]
        for i in range(1, self.size):
            if self.array[i] > max_value:
                max_value = self.array[i]
        return max_value

    def deepcopy(self):
        copied_list = CustomList()
        copied_list.size = self.size
        copied_list.array = copy.deepcopy(self.array)
        return copied_list
