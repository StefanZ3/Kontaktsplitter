from .constants import TITEL_METADATA

class TitleManager:
    def __init__(self):
        self.titles  = list(TITEL_METADATA.keys())

    def add_title(self, new_title: str, gender: str = "0", nation: str = "DE"):
        if new_title not in self.titles:
            TITEL_METADATA[new_title] = {
                "geschlecht": gender,
                "nationalitaet": nation
            }
            self.titles.append(new_title)

    def is_known_title(self, title):
        return title in TITEL_METADATA

    def get_gender_for_title(self, title):
        return TITEL_METADATA.get(title, {}).get("geschlecht")
    
    def map_coder_to_gende(self, gender):
        if gender == "1":
            return "männlich"
        elif gender == "2":
            return "weiblich"
        elif gender == "3":
            return "divers"
        return "unisex"  # fallback