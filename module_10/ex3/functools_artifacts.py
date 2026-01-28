from functools import reduce, partial, lru_cache, singledispatch
from operator import mul, add
from time import time


# Ancient Library Test Data
spell_powers = [40, 22, 49, 29, 31, 33]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [30, 35, 22]


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce((lambda x, y: add(x, y)), spells)
    elif operation == "multiply":
        return reduce((lambda x, y: mul(x, y)), spells)
    elif operation == "min":
        return reduce((lambda x, y: min(x, y)), spells)
    elif operation == "max":
        return reduce((lambda x, y: max(x, y)), spells)


def demo_enchantment(target: str, power: int, element: str, ) -> str:
    return f"Enchanting {target} with {element} lv {power}"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="lightning")
        }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher() -> callable:
    ...


@spell_dispatcher.register
def _(x: int):
    ...


def main() -> None:
    lst = [1, 2, 3, 4]
    print(f"Test reduce w/ {lst}:")
    for operator in operations:
        print(f"- {operator}: {spell_reducer(lst, operator)}")
    print()

    print("Test Partial function:")
    lv_50_enchant = partial_enchanter(demo_enchantment)
    print(" -", (lv_50_enchant["fire_enchant"])("Sword"))
    print(" -", (lv_50_enchant["ice_enchant"])("Bow"))
    print(" -", (lv_50_enchant["lightning_enchant"])("pickaxe"))

    t = time()
    for nb in fibonacci_tests:
        memoized_fibonacci(nb)
    print(time() - t)


if __name__ == "__main__":
    main()
