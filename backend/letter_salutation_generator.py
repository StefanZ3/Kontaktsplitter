from .constants import TITEL_METADATA, SALUTATIONS_BY_LANGUAGE

class LetterSalutationGenerator:
    def get_letter_salutation(self, parsed_contact):
        """Generiert eine förmliche Briefanrede gemäß Etikette."""

        first_name = parsed_contact.get("first_name", "").strip()
        last_name = parsed_contact.get("last_name", "").strip()
        raw_titles = parsed_contact.get("titles", "").strip()
        gender = parsed_contact.get("gender", "").lower()
        language = parsed_contact.get("language", "DE").upper()

        # Titel vorbereiten
        title_tokens = [t.strip() for t in raw_titles.replace(",", " ").split() if t.strip()]
        highest_title = self.get_highest_title(title_tokens, gender)

        # Sonderfälle: Monarchen, Prinzen, Adelige mit Spezialanrede
        if highest_title in ["König", "Königin"]:
            return "Majestät,"
        elif highest_title in ["Prinz", "Prinzessin"]:
            return "Königliche Hoheit,"
        elif highest_title in ["Graf", "Gräfin"]:
            sal = SALUTATIONS_BY_LANGUAGE.get(language, SALUTATIONS_BY_LANGUAGE["DE"])
            base = sal.get(gender, "Sehr geehrte Damen und Herren")
            return f"{base} {highest_title} {last_name},".strip()

        # Standardanrede (Professor, Dr. etc.)
        salutation_prefix = SALUTATIONS_BY_LANGUAGE.get(language, SALUTATIONS_BY_LANGUAGE["DE"]).get(
            gender, "Sehr geehrte Damen und Herren"
        )

        if gender not in ["männlich", "weiblich"]:
            return salutation_prefix + ","

        # Endgültige Anrede zusammensetzen
        name_part = last_name
        parts = [salutation_prefix, highest_title, name_part]
        return " ".join(p for p in parts if p).strip() + ","

    def get_highest_title(self, titles: list[str], gender: str) -> str:
        """Bestimmt den höchsten relevanten Titel nach Etikette."""

        # Titel, die in der Briefanrede NICHT erscheinen sollen
        ignored_titles = {"M.Sc.", "B.Sc."}

        priority = [
            "König", "Königin",
            "Prinz", "Prinzessin",
            "Graf", "Gräfin",
            "Professor", "Professorin", "Prof.",
            "Dr.", "Dr.-Ing.", "Dr. rer. nat.", "Dr. med."
        ]

        for prio_title in priority:
            for t in titles:
                if prio_title.lower() in t.lower() and t not in ignored_titles:
                    if prio_title in ["Prof.", "Professor", "Professorin"]:
                        return "Professorin" if gender == "weiblich" else "Professor"
                    return prio_title

        return ""
