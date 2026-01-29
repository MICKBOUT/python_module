from functools import wraps
import time
from random import randint


def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Spell completed in {round(time.time() - start, 3)} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator_factory(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = kwargs["power"] if "power" in kwargs else args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator_factory


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int = -1) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer:")
    warped_fireball = spell_timer(fireball)
    print("Result:", warped_fireball())
    print()

    print("Testing MageGuild...")
    factory_minpower_10 = power_validator(10)
    fire_spell_minpower_10 = factory_minpower_10(lambda power: "FIREBALL !!!")
    print(fire_spell_minpower_10(power=5))
    print(fire_spell_minpower_10(power=15))
    print()

    print("Testin retry spell...")
    retryer = retry_spell(10)

    def random_succes(succes_rate: int) -> str:
        if randint(1, max(1, succes_rate)) == 1:
            return "Spell Cast at max power"
        raise
    random_succes_retryer = retryer(random_succes)
    print(random_succes_retryer(10))
    print()

    print("Testing MageGuild... ")
    guild = MageGuild()
    print(guild.cast_spell(" Lightning", 15))
    print(guild.cast_spell("Lightning", 9))


if __name__ == "__main__":
    main()
