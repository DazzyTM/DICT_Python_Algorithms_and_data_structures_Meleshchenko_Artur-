import pytest
from class_parrot import Parrot
from practice4 import ParrotListBasic, ParrotListExtended


class TestParrotListBasic:
    def setup_method(self):
        self.parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        self.parrot2 = Parrot("Parrot2", "Breed2", "Color2", 2, 5)
        self.parrot3 = Parrot("Parrot3", "Breed3", "Color3", 3, 6)

    def test_append_and_getitem(self):
        parrot_list = ParrotListBasic()
        parrot_list.append(self.parrot1)
        parrot_list.append(self.parrot2)
        parrot_list.append(self.parrot3)
        assert parrot_list[0] == self.parrot1
        assert parrot_list[1] == self.parrot2
        assert parrot_list[2] == self.parrot3
        with pytest.raises(IndexError):
            assert parrot_list[3]

    def test_len(self):
        parrot_list = ParrotListBasic()
        parrot_list.append(self.parrot1)
        parrot_list.append(self.parrot2)
        parrot_list.append(self.parrot3)
        assert len(parrot_list) == 3

    def test_setitem(self):
        parrot_list = ParrotListBasic()
        parrot_list.append(self.parrot1)
        parrot_list.append(self.parrot2)
        parrot_list.append(self.parrot3)
        parrot_list[1] = self.parrot3
        assert parrot_list[1] == self.parrot3
        with pytest.raises(IndexError):
            parrot_list[3] = self.parrot1

    def test_index(self):
        parrot_list = ParrotListBasic()
        parrot_list.append(self.parrot1)
        parrot_list.append(self.parrot2)
        assert parrot_list.index(self.parrot2) == 1
        with pytest.raises(ValueError):
            parrot_list.index(self.parrot3)

    def test_remove(self):
        parrot_list = ParrotListBasic()
        parrot_list.append(self.parrot1)
        parrot_list.append(self.parrot2)
        parrot_list.append(self.parrot3)
        parrot_list.remove(self.parrot2)
        assert self.parrot2 not in parrot_list
        with pytest.raises(ValueError):
            parrot_list.remove(self.parrot2)


class TestParrotListExtended:
    def setup_method(self):
        self.parrot_list = ParrotListExtended()
        self.parrot1 = Parrot("Parrot1", "Breed1", "Color1", 1, 4)
        self.parrot2 = Parrot("Parrot2", "Breed2", "Color2", 2, 3)
        self.parrot3 = Parrot("Parrot3", "Breed3", "Color3", 3, 2)

    def test_clear(self):
        self.parrot_list.append(self.parrot1)
        self.parrot_list.append(self.parrot2)
        self.parrot_list.clear()
        assert len(self.parrot_list) == 0
        assert self.parrot_list.head is None
        assert self.parrot_list.tail is None

    def test_extend(self):
        self.parrot_list.append(self.parrot1)
        self.parrot_list.append(self.parrot2)
        self.parrot_list.extend([self.parrot3])
        assert len(self.parrot_list) == 4
        assert self.parrot_list[1] == self.parrot1
        assert self.parrot_list[2] == self.parrot2
        assert self.parrot_list[3] == self.parrot3
