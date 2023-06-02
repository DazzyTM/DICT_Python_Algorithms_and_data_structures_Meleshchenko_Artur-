import random
from typing import List

class Parrot:
    def __init__(self, name: str, breed: str, areal: str, size: int, color: str):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.size = size
        self.color = color

    def determine_size_category(self) -> str:
        if self.size > 80:
            return "великий"
        elif self.size > 50:
            return "великий"
        elif self.size > 30:
            return "середній"
        else:
            return "невеликий"

    def determine_areal_category(self) -> str:
        areal_categories = {
            "Північна та Південна Америка": "американському",
            "Європа та Азія": "євроазіатському",
            "Африка": "африканському",
            "Австралія": "австралійському"
        }
        return areal_categories.get(self.areal, "невідомому")

    def generate_message(self) -> str:
        size_category = self.determine_size_category()
        areal_category = self.determine_areal_category()
        message = f"Папуга {self.name} має забарвлення {self.color}, {size_category} розмір довжиною {self.size} см " \
                  f"і належить до породи {self.breed}, які літають у {areal_category} регіоні."
        return message


class Generator:
    @staticmethod
    def generate_parrot() -> Parrot:
        names = ["Шері", "Кіко", "Поллі", "Макс", "Ріо", "Коко", "Луї", "Олівія", "Марлін", "Джек"]
        breeds = ["ара", "амазонка", "корелла", "какаду", "неразлучник"]
        areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        colors = ["червоний", "синій", "зелений", "жовтий", "фіолетовий"]

        # Згенерувати випадкові значення для кожного атрибута папуги
        name = random.choice(names)
        breed = random.choice(breeds)
        areal = random.choice(areals)
        size = random.randint(10, 100)
        color = random.choice(colors)

        # Створити об'єкт папуги з випадковими атрибутами
        parrot = Parrot(name, breed, areal, size, color)
        return parrot


# Створити випадкову папугу
random_parrot = Generator.generate_parrot()

# Створити повідомлення для випадкової папуги
message = random_parrot.generate_message()
print(message)


def generate_parrots(num_parrots: int) -> List[Parrot]:
    parrots = []
    for _ in range(num_parrots):
        parrot = Generator.generate_parrot()
        parrots.append(parrot)
    return parrots


# Згенерувати список з 1000 випадкових папуг
parrots_list_1000 = generate_parrots(1000)

# Згенерувати список з 10000 випадкових папуг
parrots_list_10000 = generate_parrots(10000)
