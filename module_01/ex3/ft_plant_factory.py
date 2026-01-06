class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str,
                 starting_height: int = 0, starting_age: int = 0):
        """
        init the class
        """
        self.name = name
        self.starting_height = starting_height
        self.height_cm = starting_height
        self.starting_age = starting_age
        self.age_days = starting_age
        self.grow_this_week = 0
        print(f"Created: {name} ({starting_height}cm, {starting_age} days)")

    def grow(self, size: int) -> None:
        """
        grow the plant by size cm
        """
        self.height_cm += size
        self.grow_this_week = size

    def age(self, days: int) -> None:
        """
        add days to the age of the plant
        """
        self.age_days += days

    def get_info(self) -> int:
        """
        get the last grow of the plant
        """
        return self.grow_this_week


class factory:
    """
    a factory that create plant
    """
    def create_plant(data):
        """
        a factory that create plant
        """
        name, height, age = data
        return Plant(name, height, age)


if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Sunflower", 80, 45),
        ("Cactus", 15, 120),
        ("Tulip", 18, 20),
        ("Bamboo", 70, 150),
    ]

    plants = [factory.create_plant(data) for data in plants_data]

    print(f"Total plants created: {5}")
