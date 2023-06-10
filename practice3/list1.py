class List:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return repr(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def append(self, value):
        self.array.append(value)

    def insert(self, index, value):
        self.array.insert(index, value)

    def index(self, value):
        return self.array.index(value)

    def remove(self, value):
        self.array.remove(value)
