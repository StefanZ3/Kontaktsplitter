import pytest
from backend.title_manager import TitleManager
from backend.parser import ContactParser


@pytest.fixture
def title_manager():
    return TitleManager()


@pytest.fixture
def parser(title_manager: TitleManager):
    return ContactParser(title_manager=title_manager)

@pytest.mark.parametrize(
    "input_contact, expected_return_contact, expected_salutation",
    [
        ("Peter Fischer", "Peter Fischer", ""),
        ("Herr Dr. Peter Fischer", "Dr. Peter Fischer", "Herr"),
        ("Frau Jana Müller", "Jana Müller", "Frau"),
        ("frau Müller", "frau Müller", ""),
        ("Dr. Frau Müller", "Dr. Frau Müller", ""),
        ("Mr. Schulz", "Schulz", "Mr."),
        ("Señora Schulz", "Schulz", "Señora"),
        ("Señor Schulz", "Schulz", "Señor"),
    ],
)
def test_get_salutation(parser: ContactParser, input_contact: str, expected_return_contact: str, expected_salutation: str):
    return_contact, salutation = parser.get_salutation(input_contact)
    assert return_contact == expected_return_contact
    assert salutation == expected_salutation

@pytest.mark.parametrize(
    "input_contact, expected_return_contact, expected_titles",
    [
        ("Peter Fischer", "Peter Fischer", []),
        ("Dr. Peter Fischer", "Peter Fischer", ["Dr."]),
        ("Professor Dr. Michael Gehring", "Michael Gehring", ["Professor", "Dr."])
    ],
)
def test_get_titles(parser: ContactParser, input_contact: str, expected_return_contact: str, expected_titles: list[str]):
    return_contact, titles = parser.get_titles(input_contact)
    assert return_contact == expected_return_contact
    assert titles == expected_titles

@pytest.mark.parametrize(
    "contact_with_names, expected_first_name, expected_last_name",
    [
        ("Kleinert", "", ["Kleinert"]),
        ("Peter Fischer", "Peter", ["Fischer"]),
        ("Antonius van Hoof", "Antonius", ["van", "Hoof"]),
    ],
)
def test_get_names(parser: ContactParser, contact_with_names: str, expected_first_name: str, expected_last_name: list[str]):
    first_name, last_name = parser.get_names(contact_with_names)
    assert first_name == expected_first_name
    assert last_name == expected_last_name