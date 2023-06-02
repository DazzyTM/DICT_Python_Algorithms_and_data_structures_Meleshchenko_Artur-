class Parrot:
    def __repr__(self) -> str:
        return f"Parrot(name={self.name}, breed={self.breed}, areal={self.areal}, size={self.size}, color={self.color})"

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
        message = f"Папуга {self.name} породи {self.breed}, що мешкає у {areal_category} регіоні, має розмір {size_category}, " \
                  f"довжиною {self.size} см, та має забарвлення {self.color}."
        return message


# Запрос данных у пользователя
name = input("Введіть ім'я папуги: ")
breed = input("Введіть породу папуги: ")
areal = input("Введіть регіон папуги (Північна та Південна Америка, Європа та Азія, Африка, Австралія): ")
size = int(input("Введіть розмір папуги (см): "))
color = input("Введіть забарвлення папуги: ")

# Створення об'єкту класу Parrot
parrot = Parrot(name, breed, areal, size, color)

# Вивід повідомлення про папугу
message = parrot.generate_message()
print(message)

# Вихідні дані не коректні
parrot1 = Parrot("Кеша", "Ара", "Північна та Південна Америка", "70см", "зелений")

# Порода невідома
parrot2 = Parrot("Папу", "невідома порода", "Австралія", 25, "жовто-синє")
