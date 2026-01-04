# def ft_different_errors():

def garden_operations(nb_str: str) -> int:
    """
    return 1 when the script is executed in its entirety
    """
    file_table = {100: "missing.txt"}
    try:
        nb = int(nb_str)
        index_file = 100 // nb
        file_name = file_table[index_file]
        with open(file_name, "r") as _:
            pass
    except (ValueError, ZeroDivisionError) as e:
        print(e)
    except KeyError:
        print(f"KeyError: '{index_file}' isn't in the dict")
    except FileNotFoundError:
        print(f"FileNotFoundError: '{file_name}' Not Found")
    return 1


def test_error_types() -> None:
    """
    Tester of the 4 error ask
    """
    print("=== Error test demo ===")
    number_of_successful_calls = 0

    print("\nTesting ValueError")
    number_of_successful_calls += 1 if garden_operations("a") == 1 else 0
    print("\nTesting ZeroDivisionError")
    number_of_successful_calls += 1 if garden_operations("0") == 1 else 0
    print("\nTesting FileNotFoundError")
    number_of_successful_calls += 1 if garden_operations("1") == 1 else 0
    print("\nTesting KeyError")
    number_of_successful_calls += 1 if garden_operations("2") == 1 else 0

    if number_of_successful_calls == 4:
        print("\nAll calls were successful !")
        print("All error types tested successfully !")


if __name__ == "__main__":
    test_error_types()
