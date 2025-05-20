from .constants import TITEL_METADATA

class TitleManager:
    def __init__(self):
        self.titles  = list(TITEL_METADATA.keys())
        self.add_default_titles()
    
    def add_default_titles(self):
        for title in TITEL_METADATA:
            self.titles.append(title)

    def add_title(self, new_title: str, gender: str = "unisex", nation: str = "DE"):
        if new_title not in self.titles:
            TITEL_METADATA[new_title] = {
                "geschlecht": gender,
                "nationalitaet": nation
            }
            self.titles.append(new_title)
