import pytest
from backend.language_detector import LanguageDetector

@pytest.fixture
def language_detector():
    return LanguageDetector()

@pytest.mark.parametrize(
    "parsed_contact, expected_language",
    [
        ({
            "salutation": "",
            "titles": ["Prof.", "Dr."],
            "first_name": "",
            "last_name": []
        }, "DE"),
        ({
            "salutation": "Mr.",
            "titles": [],
            "first_name": "",
            "last_name": []
        }, "EN"),
        ({
            "salutation": "M.",
            "titles": [],
            "first_name": "Nick",
            "last_name": []
        }, "FR"),
            ({
            "salutation": "Señora",
            "titles": ["Professorin", "Dr. rer. nat."],
            "first_name": "Julia",
            "last_name": "Mustermann"
        }, "ES"),
    ],
)
def test_get_language(language_detector: LanguageDetector, parsed_contact: dict, expected_language: str):
    language = language_detector.get_language(parsed_contact)
    assert language == expected_language
