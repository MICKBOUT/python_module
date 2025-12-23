def ft_len(ell):
    """
    MY version of strlen bc the original is not allowd:
    """
    i = 0
    for _ in ell:
        i += 1
    return i


class Plant:
    """
    Blueprint of a plant with attibutes Name, height and age
    """
    def __init__(self, name: str, starting_height: int) -> None:
        self.name = name
        self.height = starting_height
        self.starting_height = starting_height
        self.grown = 0
        self.type = "Plant"

    def get_data(self) -> None:
        print(f"{self.name}, {self.height}cm")

    def grow(self, size: int) -> None:
        self.grown += size
        self.height += size


class FloweringPlant(Plant):
    """
    Class FloweringPlant creat from plant
    """
    def __init__(self, name: str, starting_height: int, color: str):
        super().__init__(name, starting_height)
        self.color = color
        self.type = "FloweringPlant"

    def get_data(self):
        print(f"{self.name}, {self.height}cm, {self.color} (Blooming)")


class PrizeFlower(FloweringPlant):
    """
    Class FloweringPlant creat from FloweringPlant
    """
    def __init__(self, name: str, starting_height: int, color: str,
                 prizePoints: int):
        super().__init__(name, starting_height, color)
        self.prizePoints = prizePoints
        self.type = "PrizeFlower"

    def get_data(self):
        print(f"{self.name}, {self.height}cm, {self.color} (Blooming), \
{self.prizePoints} Prize points")


class Garden:
    """
    class garden : create a garden with basic atribut
    """
    totalPlant = 0

    @staticmethod
    def border(size: int) -> str:
        return '=' * size

    @classmethod
    def add_total_plant_count(cls) -> None:
        cls.totalPlant += 1

    @classmethod
    def get_total_plant_count(cls) -> int:
        return cls.totalPlant

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        Garden.add_total_plant_count()
        print(f"{plant.name} added to {self.name}'s garden")

    def get_plant(self) -> None:
        print(f"=============== {self.name}'s Garden ===============")
        print("Plants in this garden :")
        for plant in self.plants:
            plant.get_data()
        print(f"Plants added: {ft_len(self.plants)}")
        print(f"Total Growth: +{self.get_grow()}cm")
        typePlant = 0
        typeFloweringPlant = 0
        typePrizeFlower = 0
        for plant in self.plants:
            if plant.type == "Plant":
                typePlant += 1
            elif plant.type == "FloweringPlant":
                typeFloweringPlant += 1
            elif plant.type == "PrizeFlower":
                typePrizeFlower += 1
        print(f"Plant Type: {typePlant} Regular, \
{typeFloweringPlant} flowering, {typePrizeFlower} Prize flowers")
        print(Garden.border((ft_len(self.name) + 41)))

    def grow_all_plants(self, size: int) -> None:
        print(f"{self.name} grow all Plants by {size}cm")
        for plant in self.plants:
            plant.grow(size)

    def get_grow(self) -> int:
        growth = 0
        for plant in self.plants:
            growth += plant.grown
        return growth

    def get_score(self) -> int:
        score = 0
        for plant in self.plants:
            if plant.type == "PrizeFlower":
                score += plant.prizePoints
            score += plant.height
        return score

    def height_validation(self) -> bool:
        for plant in self.plants:
            if plant.starting_height + plant.grown != plant.height:
                return False
        return True


class GardenManager:
    """
    Class Garden Manager : Manage multiplue garden
    """
    class GardenStats:
        """
        call Garden Stats : help track all stats related to the garden
        """

        def __init__(self, manager) -> None:
            self.manager = manager

        def count_plants_network(self) -> int:
            nb = 0
            for garden in self.manager.network:
                nb += ft_len(garden.plants)
            return nb

        def count_growth_network(self) -> int:
            growth = 0
            for garden in self.manager.network:
                growth += garden.get_grow()
            return growth

        def height_validation(self) -> bool:
            for garden in self.manager.network:
                if not garden.height_validation():
                    return False
            return True

        def garden_score(self) -> None:
            print("Garden Scores :")
            for garden in self.manager.network:
                print(f"- {garden.name}: {garden.get_score()}")

        def total_garden(self) -> int:
            return ft_len(self.manager.network)

    network = []

    @classmethod
    def create_garden_network(cls, garden: Garden) -> None:
        cls.network.append(garden)

    def __init__(self):
        self.stats = GardenManager.GardenStats(self)


if __name__ == "__main__":
    aliceGarden = Garden("Alice")
    bobGarden = Garden("Bob")
    mboutteGarden = Garden("Mboutte")

    oak = Plant("Oak", 150)
    rose = FloweringPlant("Rose", 20, "Red")
    oak.grow(15)
    rose.grow(5)

    aliceGarden.add_plant(oak)
    aliceGarden.add_plant(rose)
    aliceGarden.add_plant(PrizeFlower("Sunflower", 23, "yellow", 7))
    bobGarden.add_plant(Plant("Carrot", 10))
    mboutteGarden.add_plant(Plant("Tomato", 15))
    aliceGarden.grow_all_plants(2)

    aliceGarden.get_plant()

    manager = GardenManager()

    GardenManager.create_garden_network(aliceGarden)
    GardenManager.create_garden_network(bobGarden)

    print(f"Plants in this network : \
{manager.stats.count_plants_network()}")
    print(f"Cm grown in this network: \
{manager.stats.count_growth_network()}")
    print(f"Height validation test: {manager.stats.height_validation()}")
    print(f"Total Garden managed : {manager.stats.total_garden()}")
    manager.stats.garden_score()
