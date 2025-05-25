import pytest
from backend.title_manager import TitleManager
from backend.constants import TITEL_METADATA


@pytest.fixture(autouse=True)
def reset_titel_metadata():
    # Vorheriger Zustand sichern
    original_metadata = TITEL_METADATA.copy()
    yield
    # Nach Test zurücksetzen
    TITEL_METADATA.clear()
    TITEL_METADATA.update(original_metadata)


def test_add_title():
    manager = TitleManager()
    new_title = "Mag."
    gender = "unisex"
    nation = "AT"

    assert not manager.is_known_title(new_title)

    manager.add_title(new_title, gender=gender, nation=nation)

    assert manager.is_known_title(new_title)
    assert manager.get_gender_for_title(new_title) == gender
    assert new_title in manager.titles
    assert TITEL_METADATA[new_title]["nationalitaet"] == nation


def test_add_title_with_defaults():
    manager = TitleManager()
    new_title = "Lic."

    manager.add_title(new_title)

    assert manager.is_known_title(new_title)
    assert manager.get_gender_for_title(new_title) == "unisex"
    assert TITEL_METADATA[new_title]["nationalitaet"] == "DE"


def test_add_duplicate_title_does_not_overwrite():
    manager = TitleManager()
    existing_title = "Dr."
    TITEL_METADATA[existing_title] = {
        "geschlecht": "unisex",
        "nationalitaet": "DE"
    }

    manager.add_title(existing_title, gender="weiblich", nation="FR")

    # Es darf nichts überschrieben werden
    assert TITEL_METADATA[existing_title]["geschlecht"] == "unisex"
    assert TITEL_METADATA[existing_title]["nationalitaet"] == "DE"


def test_get_gender_for_unknown_title_returns_none():
    manager = TitleManager()
    assert manager.get_gender_for_title("NichtVorhanden") is None


def test_titles_list_reflects_added_title():
    manager = TitleManager()
    new_title = "Ing."

    manager.add_title(new_title)
    assert new_title in manager.titles


def test_is_known_title_for_existing_and_new():
    manager = TitleManager()
    new_title = "Dipl.-Inf."

    assert not manager.is_known_title(new_title)
    manager.add_title(new_title)
    assert manager.is_known_title(new_title)
