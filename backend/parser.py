from .title_manager import TitleManager
from typing import Tuple


class ContactParser:
    def __init__(self, title_manager: TitleManager):
        self.title_manager: TitleManager = title_manager

    def parse(self, input_contact: str):
        contact_without_salutation, gender = self.get_gender(input_contact)
        contact_only_names = self.get_titles(contact_without_salutation)
        

    def get_gender(self, input_contact: str) -> Tuple[str, str | None]:
        gender = None
        if input_contact.startswith("Herr"):
            gender = "m"
            # Anrede entferen
            input_contact = input_contact[4:]
            return
        elif input_contact.startswith("Frau"):
            gender = "w"
            # Anrede entfernen
            input_contact = input_contact[4:]
        return input_contact, gender

    def get_titles(self, input_contact: str) -> str:
        # Die Titel absteigend nach Länge sortieren, damit Professorin vor Professor oder Dr.-Ing. vor Dr. gefunden wird
        sorted_titles = sorted(self.title_manager.titles, key=len, reverse=True)
        titles = list()
        for title in sorted_titles:
            if title in input_contact:
                titles.append(title)
                # Gefundene Titel entfernen
                input_contact = input_contact.replace(title, "")
        return input_contact, titles
