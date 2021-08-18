class House():
    """Описание дома"""

    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """Сироить дом"""
        print("Дом на улице" + self.street + "Под номером" + str(self.number) + "построен.")

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year


House1 = House("Московская", 20)
House2 = House("Московская", 22)
House3 = House("Московская", 24)
House4 = House("Московская", 26)

print(House1.street)
print(House2.number)
print(House4.age)

House1.age_of_house(5)
print(House1.age)


class ProspectHouse(House):
    """Дома на проспректе"""

    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse("Ленина", 5)
print(PrHouse.prospect)
