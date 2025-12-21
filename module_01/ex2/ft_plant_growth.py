class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.grow_this_week = 0

    def grow(self, size: int) -> None:
        self.height += size
        self.grow_this_week = size

    def age(self, days: int) -> None:
        self.age_days += days

    def get_info(self) -> int:
        return self.grow_this_week


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120),
]

if __name__ == "__main__":
    print("=== Day 1 ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age_days} days old")

    for plant in plants:
        plant.age(6)
        plant.grow(6)

    print("=== Day 7 ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age_days} days old")
        print(f"Growth this week: +{plant.get_info()}cm")
