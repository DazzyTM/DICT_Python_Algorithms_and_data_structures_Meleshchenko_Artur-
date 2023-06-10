import random
from main_module import Parrot


class Generator:
    @staticmethod
    def generate_parrot() -> Parrot:
        name_list = ["Шері", "Кіко", "Поллі", "Макс", "Ріо", "Коко", "Луї", "Олівія", "Марлін", "Джек"]
        breed_list = ["ара", "амазонка", "корелла", "какаду", "неразлучник"]
        color_list = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        areal_list = ["червоний", "синій", "зелений", "жовтий", "фіолетовий"]


        # Згенерувати випадкові значення для кожного атрибута папуги
        name = random.choice(name_list)
        breed = random.choice(breed_list)
        areal = random.choice(areal_list)
        size = random.randint(10, 100)
        color = random.choice(color_list)

        # Створити об'єкт папуги з випадковими атрибутами
        parrot = Parrot(name, breed, areal, size, color)
        return parrot

    def generate_1000(self) -> list:

      plist = list()
      for i in range(1000):
        plist.append(self.generate_parrot())
      return plist


    def generate_10_000(self) -> list:
      plist = [self.generate_parrot() for _ in range(10000)]
      return plist


# Створити випадкову папугу
random_parrot = Generator.generate_parrot()

# Вивід повідомлення про випадкового папугу
message = random_parrot.generate_message()
print(message)


def abstract_object():
    return None
