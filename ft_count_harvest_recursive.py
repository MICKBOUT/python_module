def ft_count_harvest_recursive(start=1, end=None):
    if end is None:
        end = int(input("Days until harvest: "))
    if start > end:
        print("Harvest time!")
    else:
        print(f"Day {start}")
        return ft_count_harvest_recursive(start + 1, end)
