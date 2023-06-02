class Parrot:
    def __init__(self, name, breed, areal, size, color):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.size = int(size)
        self.color = color

    def determine_size(self):
        if self.size > 80:
            return "великий"
        elif self.size > 50:
            return "великий"
        elif self.size > 30:
            return "середній"
        else:
            return "невеликий"

    def determine_areal(self):
        areal_categories = {
            "Північна та Південна Америка": "американському",
            "Європа та Азія": "євроазіатському",
            "Африка": "африканському",
            "Австралія": "австралійському"
        }
        return areal_categories.get(self.areal, "невідомому")

    def generate_message(self):
        size_category = self.determine_size()
        areal_category = self.determine_areal()
        message = f"Папуга {self.name} має забарвлення {self.color}, {size_category} розмір довжиною {self.size} см " \
                  f"і відноситься до породи {self.breed}, які літають у {areal_category} регіоні."
        return message


# Запрос данных у пользователя
name = input("Введіть ім'я папуги: ")
breed = input("Введіть породу папуги: ")
areal = input("Введіть регіон папуги (Північна та Південна Америка, Європа та Азія, Африка, Австралія): ")
size = input("Введіть розмір папуги (см): ")
color = input("Введіть забарвлення папуги: ")

# Створення об'єкту класу Parrot
parrot = Parrot(name, breed, areal, size, color)

# Вивід повідомлення про папугу
message = parrot.generate_message()
print(message)
