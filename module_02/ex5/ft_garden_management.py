class GardenError(Exception):
    """
    Error class that defines the behavior of its subclass.
    """
    default_message = "The garden has a problem"

    def __init__(self, custom_message: str = None):
        if custom_message is None:
            super().__init__(self.default_message)
        else:
            super().__init__(custom_message)


class TankError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    default_message = "The tank has not enough water to water the plant"


class WaterLevelError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    default_message = "The water level is not in the good range"


class SunLevelError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    default_message = "The Sun level is not in the good range"


class PlantError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    default_message = "Plant name cannot be empty!"


class GardenManager:
    """
    A class that manage a basic garden w/ basic functionality
    store the plants in self.plants and the tank level in self.water_tank
    the class raise custom error message whene someeting went wrong
    """
    def __init__(self):
        self.plants = []
        self.water_tank = 100

    def add_plant(self, plant: str, water_level: int = 8,
                  sun_level: int = 10) -> None:
        """
        add a plant in the arrey
        """
        if plant is None or (len(plant) == 0):
            raise PlantError()
        else:
            self.plants.append([plant, water_level, sun_level])

    def water_plant(self) -> None:
        """
        water the plant of the arrey if there is enough water in the tank
        else raise an error message
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise TankError()
                plant[1] += 5
                self.water_tank -= 5
                print(f"watering {plant[0]} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        """
        check if the plant has vitals in the range expected.
        raise an error otherwise
        """
        for name, water_level, sun_level in self.plants:
            try:
                if water_level < 1:
                    raise WaterLevelError(f"Water level too low: \
{water_level}, (min 1)")
                elif water_level > 10:
                    raise WaterLevelError(f"Water level too high: \
{water_level}, (max 10)")
                if sun_level < 2:
                    raise SunLevelError(f"sun level too low: \
{sun_level}, (min 2)")
                elif sun_level > 12:
                    raise SunLevelError(f"sun level too high: \
{sun_level}, (max 12)")
            except (WaterLevelError, SunLevelError) as e:
                print(f"Error: checking {name}: {e}")
            else:
                print(f"{name}: (water: {water_level}, sun: {sun_level})")


if __name__ == "__main__":

    print("=== Garden manager system ===")
    manager = GardenManager()

    print("\nAdding plants in garden")

    plant = "Carrot"
    try:
        manager.add_plant(plant, water_level=0)
    except PlantError as e:
        print(e)
    else:
        print(f"{plant} Added successfully")
    plant = "Potato"
    try:
        manager.add_plant(plant, water_level=10)
    except PlantError as e:
        print(e)
    else:
        print(f"{plant} Added successfully")
    plant = ""
    try:
        manager.add_plant(plant)
    except PlantError as e:
        print(e)
    else:
        print(f"{plant} Added successfully")

    print("\nWatering plants...")
    try:
        manager.water_plant()
    except GardenError as e:
        print("Caught GardenError:", e)

    print("\nChecking plant health")
    manager.check_plant_health()

    print("\nChecking error recovery")
    manager.water_tank = -1
    try:
        manager.water_plant()
    except GardenError as e:
        print("Caught GardenError:", e)
    manager.water_tank = 100
    print("System recovered and continuing...")
