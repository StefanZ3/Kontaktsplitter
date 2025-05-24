class ContactParser:
    def __init__(self, title_manager):
        self.title_manager = title_manager

    def parse(self, input_string: str) -> dict:
        parts = input_string.strip().split()
        titel = ""
        vorname = ""
        nachname = ""
        geschlecht = ""

        if not parts:
            return {
                "titel": "",
                "vorname": "",
                "nachname": "",
                "geschlecht": ""
            }

        # Titel-Erkennung
        if self.title_manager.is_known_title(parts[0]):
            titel = parts[0]
            parts = parts[1:]  # Rest nach dem Titel

        if len(parts) == 1:
            nachname = parts[0]
        elif len(parts) >= 2:
            vorname = parts[0]
            nachname = " ".join(parts[1:])

        # Geschlecht aus Titel ableiten, falls vorhanden
        if titel:
            geschlecht = self.title_manager.get_gender_for_title(titel)
            if geschlecht == "unisex":
                geschlecht = ""  # nur setzen, wenn klar

        return {
            "titel": titel,
            "vorname": vorname,
            "nachname": nachname,
            "geschlecht": self.map_gender_to_code(geschlecht)
        }
    
    def map_gender_to_code(self, gender_string):
        if gender_string == 'männlich':
            return '1'
        elif gender_string == 'weiblich':
            return '2'
        elif gender_string == 'divers':
            return '3'
        return ''  # fallback