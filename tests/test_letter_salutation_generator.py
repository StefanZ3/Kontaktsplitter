import pytest
from backend.title_manager import TitleManager
from backend.letter_salutation_generator import LetterSalutationGenerator

@pytest.fixture
def title_manager():
    return TitleManager()

@pytest.fixture
def letter_salutation_generator(title_manager):
    return LetterSalutationGenerator(title_manager)

@pytest.mark.parametrize(
    "parsed_contact, expected_letter_salutation",
    [
        # Divers → neutrale Anrede, keine Titel
        ({
            "titles": "Professor Dr.",
            "first_name": "",
            "last_name": "Schmied",
            "gender": "divers",
            "language": "DE"
        },
        "Sehr geehrte Damen und Herren,"),

        # Professor → höchster Titel, ausgeschrieben
        ({
            "titles": "Professor Dr.",
            "first_name": "",
            "last_name": "Schmied",
            "gender": "männlich",
            "language": "DE"
        },
        "Sehr geehrter Herr Professor Schmied,"),

        # Mehrere Dr.-Titel → nur ein "Dr." in Anrede
        ({
            "titles": "Dr. h.c. mult. Dr. h.c. mult. Dr. rer. nat.",
            "first_name": "",
            "last_name": "Schmied",
            "gender": "weiblich",
            "language": "DE"
        },
        "Sehr geehrte Frau Dr. Schmied,"),

        # Mehrere anzuzeigende Titel, beide Titel anzeigen
        ({
            "titles": "Baron Edler",
            "first_name": "",
            "last_name": "Schmidt",
            "gender": "männlich",
            "language": "DE"
        },
        "Sehr geehrter Herr Baron Edler Schmidt,"),

        # Kein Titel, normaler Nachname
        ({
            "titles": "",
            "first_name": "Miachel",
            "last_name": "van Gerwen",
            "gender": "männlich",
            "language": "DE"
        },
        "Sehr geehrter Herr van Gerwen,"),

        # König → spezielle Monarchen-Anrede
        ({
            "titles": "König",
            "first_name": "Friedrich",
            "last_name": "von Hohenberg",
            "gender": "männlich",
            "language": "DE"
        },
        "Majestät,"),

        # Graf → ausgeschrieben, mit Herr
        ({
            "titles": "Graf",
            "first_name": "Otto",
            "last_name": "von Hohenberg",
            "gender": "männlich",
            "language": "DE"
        },
        "Sehr geehrter Herr Graf von Hohenberg,"),

        # Prinz → Königliche Hoheit
        ({
            "titles": "Prinz",
            "first_name": "Ludwig",
            "last_name": "von Bayern",
            "gender": "männlich",
            "language": "DE"
        },
        "Königliche Hoheit,"),

        # M.Sc. → wird ignoriert
        ({
            "titles": "M.Sc.",
            "first_name": "Lisa",
            "last_name": "Maier",
            "gender": "weiblich",
            "language": "DE"
        },
        "Sehr geehrte Frau Maier,"),

        # Englische Anrede, Professor
        ({
            "titles": "Prof. Dr.",
            "first_name": "Alice",
            "last_name": "Johnson",
            "gender": "weiblich",
            "language": "EN"
        },
        "Dear Ms. Professorin Johnson,"),

        # Französische Anrede, kein Titel
        ({
            "titles": "",
            "first_name": "Jean",
            "last_name": "Dupont",
            "gender": "männlich",
            "language": "FR"
        },
        "Monsieur Dupont,"),

        # Spanische Anrede, divers
        ({
            "titles": "",
            "first_name": "",
            "last_name": "Martinez",
            "gender": "divers",
            "language": "ES"
        },
        "Estimados señores,"),
    ],
)
def test_get_letter_salutation(letter_salutation_generator, parsed_contact, expected_letter_salutation):
    result = letter_salutation_generator.get_letter_salutation(parsed_contact)
    assert result == expected_letter_salutation
