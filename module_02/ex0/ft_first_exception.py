
def check_temperature(temp_str: str) -> int:
    """
    temperatire checker :
    Take a str in input and return the value in an int if the input is valide
    Otherwise, print an error and return nothing
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temp < 0:
        print(f"Error: {temp}°C too low (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp}°C too high (max 40°C)")
    else:
        print(f"{temp}°C is perfect")
        return temp
    return None


def test_temperature_input() -> None:
    """
    a checker to see if the fonction above crash
    """

    print("=== Temperature Checker ===")

    print("\nTest 1: no int")
    check_temperature("one")

    print("\nTest 2: too low")
    check_temperature("-20")

    print("\nTest 3: too high")
    check_temperature("50")

    print("\nTest 4: perfect temp")
    check_temperature("20")

    print(f"{'=' * 20}\nall test pass, nothing has crash !!!")


if __name__ == "__main__":
    test_temperature_input()
