from .constants import SALUTATIONS

class LanguageDetector:
    def get_language(self, salutation) -> str:
        """Ermittelt die Sprache anhand der Anrede."""
        if salutation:
            language = SALUTATIONS[salutation]["nationalitaet"]
        else:
            language = "DE"
        return language