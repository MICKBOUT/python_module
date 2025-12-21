class SecurePlant:
    """
    Class SecirePlant :
        Blueprint of a plant with secure methode to avoid corupted data.
    """
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        if age < 0:
            print("[REJECTED] Age: Security negative Value")
            self._age = 0
        else:
            self._age = age
        if height < 0:
            print("[REJECTED] Height: Security negative Value")
            self._height = 0
        else:
            self._height = height
        print(f"Plant created: {name}")

    def get_height(self) -> int:
        return self._height

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"[REJECTED] Invalid operation attempted: {height}cm")
            print("Security: Negative height rejected")
        else:
            self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"[REJECTED] Invalid operation attempted: {age} days")
            print("Security: Negative age rejected")
        else:
            self._age = age


if __name__ == "__main__":
    print("\n=== Secure Garden ===")
    rose = SecurePlant("Rose", 10, 15)

    print("----------")
    print(f"Original height :{rose.get_height()}cm")
    print("----------")
    print("Trying invalide height :")
    rose.set_height(-42)
    print("----------")
    print(f"After an invalide operation :{rose.get_height()}cm")
    print("----------")
    rose.set_height(20)
    print(f"After changing with the methode : {rose.get_height()}cm\n")

    print(f"Original age : {rose.get_age()} days")
    print("----------")
    print("Trying invalide age :")
    rose.set_age(-42)
    print("----------")
    print(f"After an invalide operation : {rose.get_age()} days")
    print("----------")
    rose.set_age(100)
    print(f"After changing with the methode : {rose.get_age()} days")

    print("\n\nPlant with negative age :")
    cactus = SecurePlant("Cactus", -10, 15)
    print(f"Age : {cactus.get_age()} days")

    print("\nPlant with negative height :")
    sunflower = SecurePlant("Sunflower", 80, -10)
    print(f"Height : {sunflower.get_height()}cm")
