from functools import reduce
from operator import mul, add

# Ancient Library Test Data
spell_powers = [40, 22, 49, 29, 31, 33]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [13, 16, 16]


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce((lambda x, y: add(x, y)), spells)
    elif operation == "multiply":
        return reduce((lambda x, y: mul(x, y)), spells)
    elif operation == "min":
        return reduce((lambda x, y: min(x, y)), spells)
    elif operation == "max":
        return reduce((lambda x, y: max(x, y)), spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    ...


def memoized_fibonacci(n: int) -> int:
    ...


def spell_dispatcher() -> callable:
    ...


def main() -> None:
    lst = [1, 2, 3, 4]
    print(f"Test reduce w/ {lst}:")
    for operator in ["add", "multiply", "min", "max"]:
        print(f"- {operator}: {spell_reducer(lst, operator)}")


if __name__ == "__main__":
    main()
