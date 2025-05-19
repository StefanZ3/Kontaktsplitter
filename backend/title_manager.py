from .constants import DEFAULT_TITLES

class TitleManager:
    def __init__(self):
        self.titles  = list()
        self.add_default_titles()
    
    def add_default_titles(self):
        for title in DEFAULT_TITLES:
            self.titles.append(title)

    def add_title(self, new_title: str):
        if new_title not in self.titles:
            self.titles.append(new_title)

