class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days


class Flower(Plant):
    """
    Class Flower inherits for class Plant with color atribut
    """
    def __init__(self, name: str, height: int, age_days: int,
                 color: str) -> None:
        """
        inti the class Flower
        """
        super().__init__(name, height, age_days)
        self.color = color

    def bloom(self) -> None:
        """
        print that the plant is blooming
        """
        print(f"{self.name} is blooming")

    def get_info(self):
        """
        print various info on the plant
        """
        print(f"{self.name} (Flower): {self.height}cm, {self.age_days} days, \
{self.color} color")


class Tree(Plant):
    """
    Class Tree inherits for class Plant with other atribut
    """
    def __init__(self, name: str, height: int, age_days: int,
                 trunk_diameter: int) -> None:
        """
        init the class
        """
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self, area: int) -> None:
        """
        print info on the shade area status
        """
        print(f"{self.name} provide {area} square meters of shade")

    def get_info(self):
        """
        print various info on the plant
        """
        print(f"{self.name} (Tree): {self.height}cm, {self.age_days} days \
{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Class Vegetable inherits for class Plant with other atribut
    """
    def __init__(self, name: str, height: int, age_days: int,
                 harvest_season: str, nutritional_value) -> None:
        """
        init the vegatable
        """
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self) -> None:
        """
        get nutritional info
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        """
        print various info with this vegatable
        """
        print(f"{self.name} (Vegetable): {self.height}cm, \
{self.age_days} days, {self.harvest_season} harvest")


if __name__ == "__main__":
    rose = Flower("Rose", 25, 25, "red")
    tuliple = Flower("tuliple", 36, 30, "Blue")

    oak = Tree("Oak", 500, 1900, 50)
    ash = Tree("Ash", 450, 1200, 75)

    carrot = Vegetable("Carrot", 10, 10, "Summer", "vitamine C")
    pumpkin = Vegetable("Pumpkin", 25, 50, "Fall", "vitamine C")

    rose.get_info()
    rose.bloom()
    print()
    oak.get_info()
    oak.produce_shade(70)
    print()
    carrot.get_info()
    carrot.nutritional()
