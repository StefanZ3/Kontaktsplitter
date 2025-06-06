from .title_manager import TitleManager
from .constants import SALUTATIONS, LASTNAME_PREFIXES
from typing import Tuple
from .gender_detector import GenderDetector
from .language_detector import LanguageDetector


class ContactParser:
    def __init__(self, title_manager: TitleManager):
        self.title_manager: TitleManager = title_manager
        self.gender_detector = GenderDetector()
        self.language_detector = LanguageDetector()

    def parse(self, input_contact: str):
        """Ermittelt Anrede, Titel, Vorname, Nachname, Geschlecht und Nationalität
        vom Eingabe-String, gibt die Werte als dict zurück."""
        contact_without_salutation, salutaion = self.get_salutation(input_contact)
        contact_with_names, titel_liste = self.get_titles(contact_without_salutation)
        first_name, last_name = self.get_names(contact_with_names) 
        gender = self.gender_detector.get_gender(salutaion,titel_liste, first_name)
        language = self.language_detector.get_language(salutaion)
        titel_string = " ".join(titel_liste)

        return {
            "salutation": salutaion,
            "titles": titel_string,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "language": language
        }

    def get_salutation(self, input_contact: str) -> Tuple[str, str]:
        input_lower = input_contact.lower()
        for original in SALUTATIONS:
            if input_lower.startswith(original.lower()):
                # Korrigierte Länge basierend auf dem gefundenen Schlüssel
                match_length = len(original)
                return input_contact[match_length:].strip(), original
        return input_contact, ""

    def get_titles(self, input_contact: str) -> Tuple[str, list[str]]:
        # Die Titel absteigend nach Länge sortieren, damit Professorin vor Professor oder Dr.-Ing. vor Dr. gefunden wird
        sorted_titles = sorted(self.title_manager.titles, key=len, reverse=True)
        titles = list()
        for title in sorted_titles:
            if title in input_contact:
                titles.append(title)
                # Gefundene Titel entfernen
                input_contact = input_contact.replace(title, "")
        return input_contact.strip(), titles
        
    def get_names(self, contact_with_names: str) -> Tuple[str, str]:
        names = contact_with_names.strip().split()
        # Wenn die Liste leer ist, sind keine Namen enthalten
        if not names:
            return "", []
        # Wenn die Liste einen Namen enthält, wird dieser als Nachname interpretiert
        if len(names) == 1:
            return "", names[0]  # Ein-Wort-Name = Nachname   
        # Rückwärts durchgehen und nach der letzten Präfix-Kette suchen
        last_name_start = len(names) - 1
        for i in range(len(names) - 1, 0, -1):
            if names[i - 1].lower() in LASTNAME_PREFIXES:
                last_name_start = i - 1
            elif last_name_start != len(names) - 1:
                # Sobald ein Nicht-Präfix nach einem Präfix auftaucht, abbrechen
                break

        first_name = " ".join(names[:last_name_start])
        last_name = " ".join(names[last_name_start:])

        return first_name, last_name

