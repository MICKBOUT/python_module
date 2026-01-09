import sys


def command_quest_tester() -> None:
    """
    Basic tests to show how to print arg
    """
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv}")

    if len(sys.argv) > 1:
        print(f"Arguments recived: {len(sys.argv) - 1}")

    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest_tester()
