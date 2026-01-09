def ft_count_harvest_recursive(
        current_day: None = None, end: None = None) -> None:
    if end is None:
        end = int(input("Days until harvest: "))
        ft_count_harvest_recursive(1, end)
    else:
        if current_day <= end:
            print(f"Day {current_day}")
            ft_count_harvest_recursive(current_day + 1, end)
        else:
            print("Harvest time!")
