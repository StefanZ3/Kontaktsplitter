from .constants import SALUTATIONS

class LanguageDetector:
    def get_language(self, parsed_contact: dict) -> str:
        """Ermittelt die Sprache anhand der Anrede."""
        salutation = parsed_contact["salutation"]
        if salutation:
            language = SALUTATIONS[salutation]["nationalitaet"]
        else:
            language = "DE"
        return language