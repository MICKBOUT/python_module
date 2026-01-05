def water_plants(plant_list: list):
    """
    • Opens a "watering system" (just print a message)
    • Goes through each plant in the list
    • Waters each plant (print a message)
    • Always closes the watering system in a finally block
    • Handles errors if a plant name is invalid
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            plant[1]
            print(f"Watering {plant}")
    except Exception:
        print(Exception(f"Cannot water '{plant}'"))
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Testing Watering ===")
    print("\ntestinf w/o error")
    water_plants(["carrot", "tomato"])

    print("\nTestinf w/ error")
    water_plants(["carrot",  None, "tomato"])
