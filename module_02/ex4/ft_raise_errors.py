def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """
    a function that check_plant_health(plant_name, water_level, sunlight_hours)
    that:
    • Checks if the plant name is valid (not empty)
    • Checks if water level is reasonable (between 1 and 10)
    • Checks if sunlight hours are reasonable (between 2 and 12)
    • Raises appropriate errors with helpful messages when something is wrong
    • Returns a success message if everything is okay
    """
    if plant_name is None or len(plant_name) == 0:
        raise ValueError("Name missing")
    if not (1 <= water_level <= 10):
        raise ValueError("water_level is not in the good range")
    if not (2 <= sunlight_hours <= 12):
        raise ValueError("sunlight_hours are not in the good range")
    print("Success message")


def test_plant_checks():
    """
    Create a test_plant_checks() function that demonstrates:
    • Testing with good values (should work fine)
    • Testing with bad plant name (should raise ValueError)
    • Testing with bad water level (should raise ValueError)
    • Testing with bad sunlight hours (should raise ValueError)
    • Catching and handling each error appropriately
    """
    print("=== Custom Error Tester ===")
    print("\nTest w/ good values :")
    try:
        check_plant_health("plant", 5, 5)
    except ValueError as e:
        print("Error:", e)

    print("\nTest w/ missing name")
    try:
        check_plant_health("", 0, 0)
    except ValueError as e:
        print("Error:", e)

    print("\nTest w/ bad water level")
    try:
        check_plant_health("plant", -1, 5)
    except ValueError as e:
        print("Error:", e)

    print("\nTest w/ bad sunlight hours")
    try:
        check_plant_health("plant", 5, -1)
    except ValueError as e:
        print("Error:", e)

    print("\nAll tests Completed !!!")


if __name__ == "__main__":
    test_plant_checks()
