import sys
from math import sqrt


def index(data: str, ell: str) -> int:
    """
    return the index of the first occurence of the ell
    srearch in the data
    """
    index = 0
    for i in data:
        if ell == i:
            return index
        index += 1
    raise Exception(f"{ell} not found in {data}")


def distance(end_pos, starting_pos: tuple = (0, 0, 0)):
    """
    calculate the distance between two poitns
    """
    x1, y1, z1 = starting_pos
    x2, y2, z2 = end_pos

    dist = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Distance between {starting_pos} and {end_pos}: {dist}")


def parcing_sting(data: str) -> tuple:
    """
    parce a string and return the tuple of the x, y, z
    if an error ocurre, raise the error
    """
    try:
        first_comma = index(data, ',')
        second_comma = index(data[first_comma + 1:], ',') + first_comma + 1

        x = int(data[:first_comma])
        y = int(data[first_comma + 1:second_comma])
        z = int(data[second_comma + 1:])

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
        pos = parcing_sting(string)
    except Exception as e:
        print(f"Error details - Type: {type(e).__name__}, Args: ({e})")
    else:
        distance(pos)


def tester_coordinate_system():
    """
    a tester fonction that show example of how the code work
    """
    print("=== Game Coordinate System ===\n")

    pos = tuple((10, 20, 5))
    print(f"Position created: {pos}")
    distance(pos)

    valide_string = "3,4,0"
    print(f'\nParcing coordinates: "{valide_string}"')
    manage_string(valide_string)

    invalide_string = "abc,def,ghi"
    print(f'\nParcing invalid coordinates: "{invalide_string}"')
    manage_string(invalide_string)


if __name__ == "__main__":
    tester_coordinate_system()

    for user_string in sys.argv[1:]:
        print(f'\nParcing user string: "{user_string}"')
        manage_string(user_string)
