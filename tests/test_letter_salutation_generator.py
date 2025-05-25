import pytest
from backend.letter_salutation_generator import LetterSalutationGenerator


@pytest.fixture
def letter_salutation_generator():
    return LetterSalutationGenerator()

@pytest.mark.parametrize(
    "parsed_contact, expected_letter_salutation",
    [
        ({
            "salutation": "",
            "titles": ["Professor", "Dr."],
            "first_name": "",
            "last_name": "Schmied",
            "gender": "divers"
        }, 
        "Sehr geehrte Damen und Herren"),
        ({
            "salutation": "",
            "titles": ["Professor", "Dr."],
            "first_name": "",
            "last_name": "Schmied",
            "gender": "männlich"
        }, 
        "Sehr geehrter Herr Prof. Dr. Schmied"),
        ({
            "salutation": "Frau",
            "titles": ["Dr. h.c. mult.", "Dr. h.c. mult.", "Dr. rer. nat."],
            "first_name": "",
            "last_name": "Schmied",
            "gender": "weiblich"
        }, 
        "Sehr geehrte Frau Dr. Dr. Dr. Schmied"),
        ({
            "salutation": "Herr",
            "titles": [],
            "first_name": "Miachel",
            "last_name": "van Gerwen",
            "gender" : "männlich"
        }, 
        "Sehr geehrter Herr van Gerwen"),
    ],
)
def test_get_letter_salutation(
    letter_salutation_generator: LetterSalutationGenerator,
    parsed_contact: dict,
    expected_letter_salutation
):
    letter_salutation = letter_salutation_generator.get_letter_salutation(parsed_contact)
    assert letter_salutation == expected_letter_salutation
