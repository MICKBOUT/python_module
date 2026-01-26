from importlib.metadata import version, PackageNotFoundError


def bitcoin_graph() -> None:
    import requests
    import time
    import pandas
    import numpy
    import matplotlib.pyplot

    # get the timestemp
    end = int(time.time())
    start = end - 2592000
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": start,
        "to": end
    }

    # call to api
    response = requests.get(url, params=params)
    data = response.json()

    # datra frame
    data_frame = pandas.DataFrame(data["prices"],
                                  columns=["timestamp", "price"])

    data_frame["timestamp"] = pandas.to_datetime(data_frame["timestamp"],
                                                 unit="ms")

    data_frame = data_frame.set_index("timestamp")

    prices_np = data_frame["price"].to_numpy()

    print("Mean price:", numpy.mean(prices_np))
    print("Price volatility (std):", numpy.std(prices_np))

    data_frame["smooth"] = data_frame["price"].rolling(window=20,
                                                       center=True).mean()

    # create the graph
    matplotlib.pyplot.figure(figsize=(16, 9))

    matplotlib.pyplot.plot(data_frame.index, data_frame["price"],
                           label="Raw Price")
    matplotlib.pyplot.plot(data_frame.index, data_frame["smooth"],
                           label="Smoothed Price")

    matplotlib.pyplot.title("Bitcoin Price Over the Last 30 Days")
    matplotlib.pyplot.xlabel("Date")
    matplotlib.pyplot.ylabel("Price (USD)")
    matplotlib.pyplot.grid(True)
    matplotlib.pyplot.legend()

    matplotlib.pyplot.show()


def error_deps(missing: list, bad_version: list) -> None:
    if missing:
        print("Missing modules:")
        for module in missing:
            print(f" - {module}")
        print("")
    if bad_version:
        print("Wrong versions:")
        for m, inst, req in bad_version:
            print(f" - {m}: installed {inst}, required {req}")
    print()
    print("To run the programe:")
    print("python3 -m venv 'venv_name'")
    print("run source ./'venv_name'/bin/activate")
    print()

    print("If you want use poetry:")
    print("pip install poetry")
    print("poetry install")
    print()

    print("If you want use pip:")
    print("pip install -r requirements.txt")
    print("")


def find_deps(file: str = "requirements.txt") -> dict:
    # find the depos w/ a with open cond
    deps = {}
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "==" in line:
                package, ver = line.split("==", 1)
                deps[package] = ver
            else:
                deps[line] = None
    return deps


def main():
    deps = find_deps()
    missing = []
    bad_version = []

    # check module
    print("cheking module")
    for module, required in deps.items():
        try:
            installed = version(module)
            if required and not installed.startswith(required):
                bad_version.append((module, installed, required))
            else:
                print(f"[OK] {module} - ({required})")
        except PackageNotFoundError:
            missing.append(module)
    print()

    # manage missing module
    if missing or bad_version:
        error_deps(missing, bad_version)
    else:
        bitcoin_graph()


if __name__ == "__main__":
    main()
