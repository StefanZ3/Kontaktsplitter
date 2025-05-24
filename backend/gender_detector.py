import requests
import gender_guesser.detector as gender_guesser
from .constants import SALUTATIONS, TITEL_METADATA


class GenderDetector:
    def get_gender(self, parsed_contact):
        """Ermittelt das Geschlecht mithilfe Anrede, Titel und Vorname, 
        gibt \"ungültig\" zurück, wenn beide Geschlechter gefunden werden."""
        parsed_salutation = parsed_contact["salutation"]
        parsed_titles = parsed_contact["titles"]
        parsed_first_name = parsed_contact["first_name"]
        # Liste für alle Geschlechtereinträge
        gender_list = []

        # Ermitteln des Geschlechts für die Anrede, falls vorhanden.
        if parsed_salutation:
            gender_list.append(SALUTATIONS[parsed_salutation]["geschlecht"])

        # Ermitteln des Geschlechts für alle vorhandenen Titel
        if parsed_titles:
            for title in parsed_titles:
                current_gender = TITEL_METADATA[title]["geschlecht"]
                gender_list.append(current_gender)

        # Ermitteln des Geschlechts für den Vornamen, falls vorhanden
        if parsed_first_name:
            gender_list.append(self.get_gender_from_first_name(parsed_first_name))

        gender = self.evaluate_gender_list(gender_list)
        return gender

    def get_gender_from_first_name(self, first_name: str) -> str:
        """Verwendet das Modul gender_guesser, um das Geschlecht anhand des Vornamens zu bestimmen, gibt das Geschlecht zurück."""
        detector = gender_guesser.Detector()
        # Rückgabewerte: "male", "mostly_male", "female", "mostly_female", "unknown", "andy"
        detected_gender = detector.get_gender(first_name)
        normalized_gender = self.normalize_gender(detected_gender)
        return normalized_gender

    def normalize_gender(self, detected_gender: str) -> str:
        """Übersetzt das ermittelte Ergebnis in die deutsche Geschlechtsform."""
        if detected_gender == "male" or detected_gender == "mostly_male":
            return "männlich"
        elif detected_gender == "female" or detected_gender == "mostly_female":
            return "weiblich"
        return "unisex"

    def evaluate_gender_list(self, gender_list: list[str]) -> str:
        has_male = "männlich" in gender_list
        has_female = "weiblich" in gender_list

        if has_male and has_female:
            return "ungültig"
        elif has_male:
            return "männlich"
        elif has_female:
            return "weiblich"
        else:
            return "unisex"
