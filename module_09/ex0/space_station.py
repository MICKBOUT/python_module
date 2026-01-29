from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS00",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=80.80,
            last_maintenance=datetime(2022, 2, 20, 22, 2)
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:",
          "Operational" if station.is_operational else "deactivated")
    print(station.last_maintenance)
    print()

    print("========================================")

    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=100,
            power_level=85.5,
            oxygen_level=80.80,
            last_maintenance=datetime(2022, 2, 20, 22, 2)
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
