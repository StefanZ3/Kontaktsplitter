from .constants import TITEL_METADATA

class TitleManager:
    def __init__(self):
        # Initialisiert eine Liste aller bekannten Titel aus TITEL_METADATA
        self.titles  = list(TITEL_METADATA.keys())

    def add_title(self, new_title: str, gender: str = "unisex", include_in_salutation: bool = False, nation: str = "DE"):
        """Fügt einen neuen Titel zur Liste hinzu, falls er noch nicht existiert."""
        if new_title not in self.titles:
            TITEL_METADATA[new_title] = {
                "geschlecht": gender,
                "nationalitaet": nation,
                "include_in_salutation": include_in_salutation
            }
            self.titles.append(new_title)

    def is_known_title(self, title):
        """Prüft, ob der gegebene Titel bereits vorhanden ist."""
        return title in TITEL_METADATA

    def get_gender_for_title(self, title):
        """Gibt das Geschlecht für einen bestimmten Titel zurück."""
        return TITEL_METADATA.get(title, {}).get("geschlecht")
    
    def get_title_metadata(self, title):
        """Gibt alle verfügbaren Metadaten zu einem bestimmten Titel zurück."""
        return TITEL_METADATA.get(title)
