from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = None

    @field_validator("station_id")
    def check_station_id(cls, v: str):
        if not (3 <= len(v) <= 10):
            raise ValueError(
                "station_id must have between 3 and 10 characters")
        return v

    @field_validator("name")
    def check_name(cls, v: str):
        if not (1 <= len(v) <= 50):
            raise ValueError("name must have between 1 and 50 characters")
        return v

    @field_validator("crew_size")
    def check_crew_size(cls, v: int):
        if not (1 <= v <= 20):
            raise ValueError("crew_size must be between 1 and 20 pepole")
        return v

    @field_validator("power_level")
    def check_power_level(cls, v: float):
        if not (0.0 <= v <= 100.0):
            raise ValueError("power_level must be between 0.0 and 100.0 %")
        return v

    @field_validator("oxygen_level")
    def check_oxygen_level(cls, v: float):
        if not (0.0 <= v <= 100.0):
            raise ValueError("oxygen_level must be between 0.0 and 100.0 %")
        return v

    @field_validator("notes")
    def check_notes(cls, v: str):
        if not (v is None) and len(v) > 200:
            raise ValueError("notes must have 200 characters or less")
        return v


def main():
    print("Space Station Data Validation")
    print("========================================")

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=80.80,
        last_maintenance=datetime(2022, 2, 20, 22, 2)
    )
    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print(f"Crew: {station.crew_size} pepole")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:",
          "Operational" if station.is_operational else "deactivated")
    print(station.last_maintenance)
    print()

    print("========================================")

    print("Expected validation error:")
    try:
        SpaceStation(
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
