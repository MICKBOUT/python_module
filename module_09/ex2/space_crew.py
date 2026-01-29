from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, model_validator, Field


class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: Optional[bool] = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: Optional[str] = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

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


def crew_member_creator(crew_member_data: dict) -> CrewMember | None:
    member = None
    try:
        member = CrewMember(
            member_id=crew_member_data["member_id"],
            name=crew_member_data["name"],
            rank=crew_member_data["rank"],
            age=crew_member_data["age"],
            specialization=crew_member_data["specialization"],
            years_experience=crew_member_data["years_experience"]
        )
    except Exception:
        print("Crew member Not created")
    return member


def main() -> None:
    print("Space Mission Crew Validation")

    # Creation of crew members :
    saconnor = crew_member_creator({
        "member_id": "Saconnor",
        "name": "Sarah Connor",
        "rank": CrewRanks.COMMANDER,
        "age": 55,
        "specialization": "Mission Command",
        "years_experience": 20,
    })
    jsmith = crew_member_creator({
        "member_id": "Jsmith",
        "name": "John Smith",
        "rank": CrewRanks.LIEUTENANT,
        "age": 25,
        "specialization": "Navigation",
        "years_experience": 6,
    })
    aljohnso = crew_member_creator({
        "member_id": "Aljohnso",
        "name": "Alice Johnson",
        "rank": CrewRanks.OFFICER,
        "age": 40,
        "specialization": "Engineering",
        "years_experience": 2
    })

    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2000, 1, 1),
            duration_days=900,
            crew=[saconnor, jsmith, aljohnso],
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
            crew=[jsmith, aljohnso],
            budget_millions=2500.0,
        )
        mission.print_attributes()
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
