from list_extra import CustomList

class UniqueList(CustomList):
    def append(self, value):
        if value in self.array.values():
            raise ValueError("Значение уже есть!")
        super().append(value)

    def insert(self, index, value):
        if value in self.array.values():
            raise ValueError("Значение уже есть!")
        super().insert(index, value)
