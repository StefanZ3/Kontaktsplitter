class ContactParser:
    def __init__(self, title_manager):
        self.title_manager = title_manager
        self.last_name_prefixes = {"von", "van", "de", "del", "di", "le", "la", "du"}  # Nachnamenspräfixe

    def parse(self, input_string: str) -> dict:
        parts = input_string.strip().split()
        titles = ""
        first_name = ""
        last_name = ""
        gender = ""
        language = "DE"

        if not parts:
            return {
                "titles": "",
                "first_name": "",
                "last_name": "",
                "gender": "",
                "language": ""
            }

        # Titel-Erkennung
        if self.title_manager.is_known_title(parts[0]):
            titles = parts[0]
            parts = parts[1:]  # Rest nach dem Titel

        if len(parts) == 1:
            last_name = parts[0]
        elif len(parts) >= 2:
            # Nachnamenspräfixe erkennen
            # Suche von hinten nach einem Präfix und kombiniere diesen mit dem letzten Namensteil
            if len(parts) >= 3 and parts[-2].lower() in self.last_name_prefixes:
                last_name = " ".join(parts[-2:])
                first_name = " ".join(parts[:-2])
            else:
                last_name = parts[-1]
                first_name = " ".join(parts[:-1])

        # Geschlecht aus titles ableiten, falls vorhanden
        if titles:
            gender = self.title_manager.get_gender_for_title(titles)
            if gender == "unisex":
                gender = ""  # nur setzen, wenn klar

        return {
            "titles": titles,
            "first_name": first_name,
            "last_name": last_name,
            "gender": self.map_gender_to_code(gender),
            "language": language
        }

    def map_gender_to_code(self, gender_string):
        if gender_string == 'männlich':
            return '1'
        elif gender_string == 'weiblich':
            return '2'
        elif gender_string == 'divers':
            return '3'
        return ''  # fallback
