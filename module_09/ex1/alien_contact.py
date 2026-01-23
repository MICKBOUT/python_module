from pydantic import \
    BaseModel, field_validator, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum

ALIEN_CONTACTS = [
    {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'visual',
        'signal_strength': 9.6,
        'duration_minutes': 99,
        'witness_count': 11,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_002',
        'timestamp': '2024-08-20T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'radio',
        'signal_strength': 5.6,
        'duration_minutes': 152,
        'witness_count': 6,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_003',
        'timestamp': '2024-11-15T00:00:00',
        'location': 'Very Large Array, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 4.5,
        'duration_minutes': 19,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_004',
        'timestamp': '2024-02-24T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'telepathic',
        'signal_strength': 2.4,
        'duration_minutes': 46,
        'witness_count': 9,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_005',
        'timestamp': '2024-09-10T00:00:00',
        'location': 'SETI Institute, California',
        'contact_type': 'telepathic',
        'signal_strength': 6.4,
        'duration_minutes': 134,
        'witness_count': 5,
        'message_received': 'Warning about solar flare activity',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_006',
        'timestamp': '2024-02-02T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 2.7,
        'duration_minutes': 20,
        'witness_count': 14,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_007',
        'timestamp': '2024-03-25T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'physical',
        'signal_strength': 9.0,
        'duration_minutes': 138,
        'witness_count': 10,
        'message_received': 'Request for peaceful contact',
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_008',
        'timestamp': '2024-11-30T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 8.6,
        'duration_minutes': 122,
        'witness_count': 13,
        'message_received': 'Unknown language pattern identified',
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_009',
        'timestamp': '2024-09-27T00:00:00',
        'location': 'Mauna Kea Observatory, Hawaii',
        'contact_type': 'visual',
        'signal_strength': 2.1,
        'duration_minutes': 25,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_010',
        'timestamp': '2024-06-12T00:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'physical',
        'signal_strength': 4.3,
        'duration_minutes': 52,
        'witness_count': 11,
        'message_received': None,
        'is_verified': True
    },
    {
        'contact_id': 'AC_2024_011',
        'timestamp': '2024-11-05T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 3.7,
        'duration_minutes': 235,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_012',
        'timestamp': '2024-07-04T00:00:00',
        'location': 'International Space Station',
        'contact_type': 'radio',
        'signal_strength': 5.3,
        'duration_minutes': 111,
        'witness_count': 10,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_013',
        'timestamp': '2024-02-12T00:00:00',
        'location': 'Antarctic Research Station',
        'contact_type': 'visual',
        'signal_strength': 6.8,
        'duration_minutes': 228,
        'witness_count': 11,
        'message_received': None,
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_014',
        'timestamp': '2024-10-20T00:00:00',
        'location': 'Atacama Desert, Chile',
        'contact_type': 'radio',
        'signal_strength': 7.2,
        'duration_minutes': 113,
        'witness_count': 8,
        'message_received': 'Mathematical sequence detected: prime numbers',
        'is_verified': False
    },
    {
        'contact_id': 'AC_2024_015',
        'timestamp': '2024-01-02T00:00:00',
        'location': 'Roswell, New Mexico',
        'contact_type': 'radio',
        'signal_strength': 2.1,
        'duration_minutes': 9,
        'witness_count': 13,
        'message_received': None,
        'is_verified': False
    }
]


class contact(Enum):
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"
    RADIO = "radio"
    VISUAL = "visual"


class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: contact
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_received: Optional[str] = None
    is_verified: bool = False

    @field_validator("contact_id")
    def check_station_id(cls, v: str):
        if not (5 <= len(v) <= 15):
            raise ValueError(
                "contact_id must have between 5 and 15 characters")
        return v

    @field_validator("location")
    def check_location(cls, v: str):
        if not (3 <= len(v) <= 100):
            raise ValueError("location must have between 3 and 100 characters")
        return v

    @field_validator("signal_strength")
    def check_signal_strength(cls, v: float):
        if not (0.0 <= v <= 10.0):
            raise ValueError(
                "signal_strength must must be between 0.0 and 10.0")
        return v

    @field_validator("duration_minutes")
    def check_duration_minutes(cls, v: int):
        if not (1 <= v <= 1440):
            raise ValueError(
                "duration_minutes must must be between 1 and 1440")
        return v

    @field_validator("witness_count")
    def check_witness_count(cls, v: int):
        if not (1 <= v <= 100):
            raise ValueError("witness_count must must be between 1 and 100")
        return v

    @field_validator("message_received")
    def check_message_received(cls, v: str):
        if v is None:
            return v
        if len(v) > 100:
            raise ValueError(
                "message_received must have 100 characters max")
        return v

    @model_validator(mode="after")
    def check_overall_validation(self):
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == contact.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == contact.TELEPATHIC and self.witness_count < 3:
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


def test_value(alien: dict) -> bool:
    try:
        AlienContact(
            contact_id=alien['contact_id'],
            timestamp=alien['timestamp'],
            location=alien['location'],
            contact_type=alien['contact_type'],
            signal_strength=alien['signal_strength'],
            duration_minutes=alien['duration_minutes'],
            witness_count=alien['witness_count'],
            message_received=alien['message_received'],
            is_verified=alien['is_verified']
        )
    except ValidationError:
        return False
    else:
        return True


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")

    print("Valid contact report:")
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2000, 1, 1),
            location="Area 51, Nevada",
            contact_type=contact.RADIO,
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
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2000, 1, 1),
            location="Area 51, Nevada",
            contact_type=contact.TELEPATHIC,
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

    # Test of data generated:
    # for alien in ALIEN_CONTACTS:
    #     print(test_value(alien))
