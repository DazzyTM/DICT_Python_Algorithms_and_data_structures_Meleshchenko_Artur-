from list_extra import CustomList

class SortedList(CustomList):
    def append(self, value):
        index = 0
        while index < self.size and self.array[index] < value:
            index += 1
        super().insert(index, value)

    def insert(self, index, value):
        raise NotImplementedError("Операция не поддерживается в отсортированном массиве!")

    def search(self, value):
        left = 0
        right = self.size - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == value:
                return mid
            if self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1
