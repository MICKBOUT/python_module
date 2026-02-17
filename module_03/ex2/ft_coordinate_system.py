import sys
from math import sqrt


def distance(end_pos, starting_pos: tuple = (0, 0, 0)) -> None:
    """
    calculate the distance between two poitns
    """
    x1, y1, z1 = starting_pos
    x2, y2, z2 = end_pos

    dist = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Distance between {starting_pos} and {end_pos}: {dist}")


def parsing_sting(data: str) -> tuple:
    """
    parse a string and return the tuple of the x, y, z
    if an error ocurre, raise the error
    """
    try:
        values = data.split(",")
        x, y, z = list(map(int, values))  # Unpacking exemple
        pos = tuple((x, y, z))

        print(f"Parsed position:: {pos}")
    except Exception as e:
        print("Error parsing coordinates", e)
        raise e
    return pos


def manage_string(string: str) -> None:
    """
    procec the string and handle if an error ocure
    """
    try:
        pos = parsing_sting(string)
    except Exception as e:
        print(f"Error details - Type: {type(e).__name__}, Args: ({e})")
    else:
        distance(pos)


def tester_coordinate_system() -> None:
    """
    a tester fonction that show example of how the code work
    """
    print("=== Game Coordinate System ===\n")

    pos = tuple((10, 20, 5))
    print(f"Position created: {pos}")
    distance(pos)

    valide_string = "3,4,0"
    print(f'\nParsing coordinates: "{valide_string}"')
    manage_string(valide_string)

    invalide_string = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalide_string}"')
    manage_string(invalide_string)
    print()

    print("Unpacking demonstration:")
    player = (3, 4, 0)
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]}")
    x, y, z = player
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    tester_coordinate_system()

    for user_string in sys.argv[1:]:
        print(f'\nParsing user string: "{user_string}"')
        manage_string(user_string)
