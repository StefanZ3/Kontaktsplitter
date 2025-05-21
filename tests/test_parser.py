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
    "input_contact, expected_return_contact, expected_gender",
    [
        ("Peter Fischer", "Peter Fischer", None),
        ("Herr Dr. Peter Fischer", " Dr. Peter Fischer", "m"),
        ("Frau Jana Müller", " Jana Müller", "w")
    ],
)
def test_get_gender(parser: ContactParser, input_contact: str, expected_return_contact: str, expected_gender: str):
    pass

@pytest.mark.parametrize(
    "input_contact, expected_return_contact, expected_titles",
    [
        ("Peter Fischer", "Peter Fischer", []),
        ("Dr. Peter Fischer", " Peter Fischer", ["Dr."]),
        ("Professor Dr. Michael Gehring", "  Michael Gehring", ["Professor", "Dr."])
    ],
)
def test_get_titles(parser: ContactParser, input_contact: str, expected_return_contact: str, expected_titles: list[str]):
    return_contact, titles = parser.get_titles(input_contact)
    assert return_contact == expected_return_contact
    assert titles == expected_titles
