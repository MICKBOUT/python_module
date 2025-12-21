def ft_count_harvest_recursive() -> None:
    def ft_harvest_count(current_day: int, end: int):
        if current_day > end:
            print("Harvest time!")
        else:
            print(f"Day {current_day}")
            ft_harvest_count(current_day + 1, end)

    until_harvest = int(input("Days until harvest: "))
    ft_harvest_count(1, until_harvest)
