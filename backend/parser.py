from .title_manager import TitleManager
from typing import Tuple


class ContactParser:
    def __init__(self, title_manager: TitleManager):
        self.title_manager: TitleManager = title_manager

    def parse(self, input_contact: str):
        contact_without_salutation, gender = self.get_gender(input_contact)
        contact_with_names, titles = self.get_titles(contact_without_salutation)
        first_name, last_name = self.get_names(contact_with_names)

        

    def get_gender(self, input_contact: str) -> Tuple[str, str | None]:
        gender = None
        if input_contact.startswith("Herr"):
            gender = "m"
            # Anrede entferen
            input_contact = input_contact[4:]
        elif input_contact.startswith("Frau"):
            gender = "w"
            # Anrede entfernen
            input_contact = input_contact[4:]
        return input_contact, gender

    def get_titles(self, input_contact: str) -> Tuple[str, list[str]]:
        # Die Titel absteigend nach Länge sortieren, damit Professorin vor Professor oder Dr.-Ing. vor Dr. gefunden wird
        sorted_titles = sorted(self.title_manager.titles, key=len, reverse=True)
        titles = list()
        for title in sorted_titles:
            if title in input_contact:
                titles.append(title)
                # Gefundene Titel entfernen
                input_contact = input_contact.replace(title, "")
        return input_contact, titles
    
    def get_names(self, contact_with_names: str) -> Tuple[str | None, list[str]]:
        names = contact_with_names.split()
        # Wenn die Liste leer ist, sind keine Namen enthalten
        if not names:
            return None, []
        # Wenn die Liste einen Namen enthält, wird dieser als Nachname interpretiert 
        if len(names) == 1:
            return None, [names[0]]
        # Wenn die Liste mehr als einen Namen enthält wird der erste Name als Vorname und der Rest als Nachname interpretiert
        else: 
            first_name = names[0]
            last_name = names[1:]
            return first_name, last_name
