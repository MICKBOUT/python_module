from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    RADIO = "radio"
    VISUAL = "visual"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=100)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_overall_validation(self):
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self

    def print_attributes(self) -> None:
        print("ID:", self.contact_id)
        print("Type:", self.contact_type.value)
        print("Location:", self.location)
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.signal_strength} minutes")
        print("Witnesses", self.witness_count)
        if self.message_received is not None:
            print(f"Message: '{self.message_received}'")


def main() -> None:
    print("Alien Contact Log Validation")

    print("========================================")
    print("Valid contact report:")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2000, 2, 2),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    else:
        alien.print_attributes()
    print()

    print("========================================")
    print("Expected validation error:")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2000, 1, 1),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    else:
        alien.print_attributes()


if __name__ == "__main__":
    main()
