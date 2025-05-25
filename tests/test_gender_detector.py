import pytest
from backend.gender_detector import GenderDetector


@pytest.fixture
def gender_detector():
    return GenderDetector()


@pytest.mark.parametrize(
    "first_name, expected_gender_list",
    [
        ("Peter", ["männlich"]),
        ("Petra", ["weiblich"]),
        ("Sandra Sandro Pascal", ["weiblich", "männlich", "männlich"])
    ],
)
def test_get_gender_from_first_name(
    gender_detector: GenderDetector, first_name: str, expected_gender_list: str
):
    gender = gender_detector.get_gender_from_first_name(first_name)
    assert gender == expected_gender_list


@pytest.mark.parametrize(
    "gender_list, expected_gender",
    [
        ([], ""),
        (["unisex", "unisex"], ""),
        (["weiblich", "weiblich", "männlich"], ""),
        (["unisex", "weiblich"], "weiblich"),
        (["unisex", "männlich"], "männlich"),
    ],
)
def test_evaluate_gender(
    gender_detector: GenderDetector, gender_list: list[str], expected_gender: str
):
    gender = gender_detector.evaluate_gender_list(gender_list)
    assert gender == expected_gender

@pytest.mark.parametrize(
    "parsed_contact, expected_gender",
    [
        ({
            "salutation": "Mr.",
            "titles": [],
            "first_name": "",
            "last_name": []
        }, "männlich"),
        ({
            "salutation": "",
            "titles": ["Baronin"],
            "first_name": "",
            "last_name": []
        }, "weiblich"),
        ({
            "salutation": "",
            "titles": ["Prof.", "Dr."],
            "first_name": "",
            "last_name": []
        }, ""),
        ({
            "salutation": "",
            "titles": [],
            "first_name": "Nick",
            "last_name": []
        }, "männlich"),
        ({
            "salutation": "",
            "titles": [],
            "first_name": "Nick Jan Peter",
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
        }, ""),
    ],
)
def test_get_gender(gender_detector: GenderDetector, parsed_contact: dict, expected_gender: str):
    gender = gender_detector.get_gender(
        parsed_contact["salutation"],
        parsed_contact["titles"],
        parsed_contact["first_name"]
    )
    assert gender == expected_gender
