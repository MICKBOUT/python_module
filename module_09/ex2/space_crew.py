from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import \
    BaseModel, field_validator, ValidationError, model_validator


class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str
    name: str
    rank: CrewRanks
    age: int
    specialization: str
    years_experience: int
    is_active: Optional[bool] = True

    @field_validator("member_id")
    def check_mission_id(cls, v: str):
        if not 3 <= len(v) <= 10:
            raise ValueError("member_id must have b/w 3 and 10 char")
        return v

    @field_validator("name")
    def check_name(cls, v: str):
        if not 2 <= len(v) <= 50:
            raise ValueError("name must have b/w 2 and 50 char")
        return v

    @field_validator("age")
    def check_age(cls, v: int):
        if not 18 <= v <= 80:
            raise ValueError("name must be b/w 18 and 80")
        return v

    @field_validator("specialization")
    def check_specialization(cls, v: str):
        if not 3 <= len(v) <= 30:
            raise ValueError("specialization must have b/w 3 and 30 char")
        return v

    @field_validator("years_experience")
    def check_years_experience(cls, v: int):
        if not 0 <= v <= 50:
            raise ValueError("years_experience must be b/w 0 and 50")
        return v


class SpaceMission(BaseModel):
    mission_id: str
    mission_name: str
    destination: str
    launch_date: datetime
    duration_days: int
    crew: list[CrewMember]
    mission_status: Optional[str] = "planned"
    budget_millions: float

    @field_validator("mission_id")
    def check_mission_id(cls, v: str):
        if not 5 <= len(v) <= 50:
            raise ValueError("mission_id must have b/w 5 and 50 char")
        return v

    @field_validator("mission_name")
    def check_mission_name(cls, v: str):
        if not 3 <= len(v) <= 100:
            raise ValueError("mission_name must have b/w 3 and 100 char")
        return v

    @field_validator("destination")
    def check_destination(cls, v: str):
        if not 3 <= len(v) <= 50:
            raise ValueError("destination must have b/w 3 and 50 char")
        return v

    @field_validator("duration_days")
    def check_duration_days(cls, v: int):
        if not 1 <= v <= 3650:
            raise ValueError("duration_days must have b/w 1 and 3650 days")
        return v

    @field_validator("budget_millions")
    def check_budget_millions(cls, v: float):
        if not 1.0 <= v <= 10000.0:
            raise ValueError("budget_millions must be b/w 1.0 and 10000.0")
        return v

    @model_validator(mode="after")
    def check_overall_validation(self):
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        if not any([member.rank == CrewRanks.COMMANDER
                    or member.rank == CrewRanks.CAPTAIN
                    for member in self.crew]):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            if len([member for member in self.crew
                    if member.years_experience >= 5]) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days)"
                    "need 50% experienced crew (5+ years)")

        if any(member.is_active is False for member in self.crew):
            raise ValueError("All crew members must be active")
        return self

    def print_attributes(self) -> None:
        print("Mission:", self.mission_name)
        print("ID:", self.mission_id)
        print("Destination:", self.destination)
        print(f"Duration:, {self.duration_days} days")
        print(f"Budget:, ${self.budget_millions}M")
        print("Crew size:", len(self.crew))
        print("Crew members:")
        for ell in [f" - {member.name} ({member.rank.value}) - "
                    f"{member.specialization}" for member in self.crew]:
            print(ell)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2000, 1, 1),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="Saconnor",
                    name="Sarah Connor",
                    rank=CrewRanks.COMMANDER,
                    age=55,
                    specialization="Mission Command",
                    years_experience="20"),
                CrewMember(
                    member_id="Jsmith",
                    name="John Smith",
                    rank=CrewRanks.LIEUTENANT,
                    age=25,
                    specialization=" Navigation",
                    years_experience="6"),
                CrewMember(
                    member_id="Aljohnso",
                    name="Alice Johnson",
                    rank=CrewRanks.OFFICER,
                    age=40,
                    specialization="Engineering",
                    years_experience="2")
                ],
            budget_millions=2500.0,
        )
        mission.print_attributes()
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("=========================================")
    print("Expected validation error:")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2000, 1, 1),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="Jsmith",
                    name="John Smith",
                    rank=CrewRanks.LIEUTENANT,
                    age=25,
                    specialization=" Navigation",
                    years_experience="6"),
                CrewMember(
                    member_id="Aljohnso",
                    name="Alice Johnson",
                    rank=CrewRanks.OFFICER,
                    age=40,
                    specialization="Engineering",
                    years_experience="2"),
            ],
            budget_millions=2500.0,
        )
        mission.print_attributes()
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
