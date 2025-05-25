from .title_manager import TitleManager
from .constants import SALUTATIONS, LASTNAME_PREFIXES
from typing import Tuple


class ContactParser:
    def __init__(self, title_manager: TitleManager):
        self.title_manager: TitleManager = title_manager

    def parse(self, input_contact: str):
        contact_without_salutation, salutaion = self.get_salutation(input_contact)
        contact_with_names, titles = self.get_titles(contact_without_salutation)
        first_name, last_name = self.get_names(contact_with_names)

        return {
            "salutation": salutaion,
            "titles": titles,
            "first_name": first_name,
            "last_name": last_name
        }

    def get_salutation(self, input_contact: str) -> Tuple[str, str]:
        salutation = next((original for original in SALUTATIONS.keys() if input_contact.startswith(original)),"")
        # Gefundene Anrede entfernen und String bereinigen
        input_contact = input_contact[len(salutation):].strip()
        return input_contact, salutation

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

    def old_get_names(self, contact_with_names: str) -> Tuple[str, list[str]]:
        names = contact_with_names.split()
        # Wenn die Liste leer ist, sind keine Namen enthalten
        if not names:
            return "", []
        # Wenn die Liste einen Namen enthält, wird dieser als Nachname interpretiert
        if len(names) == 1:
            return "", [names[0]]
        # Wenn die Liste mehr als einen Namen enthält wird der erste Name als Vorname und der Rest als Nachname interpretiert
        else:
            first_name = names[0]
            last_name = names[1:]
            return first_name, last_name
        
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

