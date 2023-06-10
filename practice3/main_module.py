class Parrot:
    """All methods which are specific to parrots"""
    name: str  # parrot name
    breed: str  # parrot breed
    color: str  # parrot color
    size: int  # parrot size in centimeters
    areal: str  # parrot geographic region

    def __init__(self, name: str, breed: str, color: str, size: int, areal: str) -> None:
        """Constructor of the class to set up all basic variables"""
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.areal = areal
    def get_info(self) -> str:
        """String representation of the object"""
        return f"Parrot({self.name}, {self.breed}, {self.color}, {self.size}, {self.areal})"

    def __repr__(self) -> str:
        """String representation of the object"""
        return f"Parrot({self.name}, {self.breed}, {self.color}, {self.size}, {self.areal})"

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
        message = f"Папуга {self.name} породи {self.breed}, що мешкає у {areal_category} регіоні, має {size_category} розмір, " \
                  f"довжиною {self.size} см, та має забарвлення {self.color}."
        return message
