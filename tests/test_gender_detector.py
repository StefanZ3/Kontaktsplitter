import pytest
from backend.gender_detector import GenderDetector


@pytest.fixture
def gender_detector():
    return GenderDetector()


@pytest.mark.parametrize(
    "first_name, expected_gender",
    [
        ("Peter", "männlich"),
        ("Petra", "weiblich"),
    ],
)
def test_get_gender_from_first_name(
    gender_detector: GenderDetector, first_name: str, expected_gender: str
):
    gender = gender_detector.get_gender_from_first_name(first_name)
    assert gender == expected_gender


@pytest.mark.parametrize(
    "gender_list, expected_gender",
    [
        ([], "unisex"),
        (["unisex", "unisex"], "unisex"),
        (["weiblich", "weiblich", "männlich"], "ungültig"),
        (["unisex", "weiblich"], "weiblich"),
        (["unisex", "männlich"], "männlich"),
    ],
)
def test_evaluate_gender(
    gender_detector: GenderDetector, gender_list: list[str], expected_gender: str
):
    gender = gender_detector.evaluate_gender(gender_list)
    assert gender == expected_gender

@pytest.mark.parametrize(
    "parsedContact, expected_gender",
    [
        ({
            "salutation": "Mr.",
            "titles": [],
            "first_name": "",
            "last_name": []
        }, "männlich"),
        ({
            "salutation": "",
            "titles": ["Prof.", "Dr."],
            "first_name": "",
            "last_name": []
        }, "unisex"),
        ({
            "salutation": "",
            "titles": [],
            "first_name": "Nick",
            "last_name": []
        }, "männlich"),
            ({
            "salutation": "Frau",
            "titles": ["Professorin", "Dr. rer. nat."],
            "first_name": "Julia",
            "last_name": "Mustermann"
        }, "weiblich"),
            ({
            "salutation": "Frau",
            "titles": ["Professorin", "Dr. rer. nat."],
            "first_name": "Jan",
            "last_name": "Mustermann"
        }, "ungültig"),
    ],
)
def test_get_gender(gender_detector: GenderDetector, parsedContact: dict, expected_gender: str):
    gender = gender_detector.get_gender(parsedContact)
    assert gender == expected_gender