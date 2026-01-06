class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str, height: int, age_days: int) -> None:
        """
        init the plant
        """
        self.name = name
        self.height_cm = height
        self.age_days = age_days
        self.last_grow = 0

    def grow(self, size: int) -> None:
        """
        grow the plant by the size specifide in parameter
        """
        self.height_cm += size
        self.last_grow = size

    def age(self, days: int) -> None:
        """
        age the plant by x days
        """
        self.age_days += days

    def get_info(self) -> int:
        """
        get info on the plant
        """
        return self.last_grow


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    print("=== Day 1 ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height_cm}cm, {plant.age_days} days old")

    for plant in plants:
        plant.age(6)
        plant.grow(6)

    print("=== Day 7 ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height_cm}cm, {plant.age_days} days old")
        print(f"Growth this week: +{plant.get_info()}cm")
