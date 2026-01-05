class GardenError(Exception):
    """
    Error class that defines the behavior of its subclass.
    """
    message = "The garden has a problem"

    def __init__(self):
        super().__init__(self.message)


class PlantError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    message = "The plant crave water"


class WaterError(GardenError):
    """
    Error class base on GardenError with a custom message
    """
    message = "The tank need more water"


def custom_error_tester():
    print("=== Testing custom Error: ===")
    plant_water_level = 3
    water_level = 0

    print("\nTesting GardenError:")
    try:
        raise GardenError()
    except GardenError as e:
        print(e)

    print("\nTesting PlantError:")
    try:
        if plant_water_level <= 5:
            raise PlantError()
    except PlantError as e:
        print(e)

    print("\nTesting WaterError:")
    try:
        if water_level < 10:
            raise WaterError()
    except WaterError as e:
        print(e)

    print("\nTesting All GardenError:")
    try:
        raise PlantError()
    except GardenError as e:
        print(e)
    try:
        raise WaterError()
    except GardenError as e:
        print(e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    custom_error_tester()
