class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str,
                 starting_height: int = 0, starting_age: int = 0):
        self.name = name
        self.starting_height = starting_height
        self.height_cm = starting_height
        self.starting_age = starting_age
        self.age_days = starting_age
        self.grow_this_week = 0
        print(f"Created: {name} ({starting_height}cm, {starting_age} days)")

    def grow(self, size: int) -> None:
        self.height_cm += size
        self.grow_this_week = size

    def age(self, days: int) -> None:
        self.age_days += days

    def get_info(self) -> int:
        return self.grow_this_week


if __name__ == "__main__":
    plantes = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Tulip", 18, 20),
        Plant("Bamboo", 70, 150),
    ]
    nb = 0
    for i in plantes:
        nb += 1
    print(f"Total plants created: {nb}")
