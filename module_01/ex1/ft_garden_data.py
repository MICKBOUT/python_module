class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age_days} days old")
