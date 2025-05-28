Kontaktsplitter/
│
├── backend/                            # Python-Backend (Flask-App)
│   ├── app.py                          # Flask-Anwendung (Entry Point)
│   ├── contact_parser.py               # Kernlogik zur Zerlegung von Namen
│   ├── title_manager.py                # Verwaltung und Erweiterung von Titeln
│   ├── gender_detector.py              # Geschlechtserkennung
│   ├── language_detector.py            # Spracherkennung anhand der Anrede
│   ├── letter_salutation_generator.py  # Generierung der Briefanrede
│   ├── constants.py                    # Konstanten (Titel-Liste, Nachnamen Präfixe, Briefanreden etc.)
│   └── __init__.py                     # Paketinitialisierung
│
├── frontend/                           # Einfaches HTML/CSS/JS-Frontend
│   └── index.html                      # Webformular zur Eingabe und Anzeige
│
├── tests/                              # Unit-Tests für Backend-Module
│   ├── test_app.py
│   ├── test_contact_parser.py
│   ├── test_gender_detector.py
│   ├── test_language_detector.py
│   ├── test_letter_salutation_generator.py
│   └── test_title_manager.py
│
├── doku/                               # Dokumentation
│   ├── definition_of_done.md
│   ├── design.md
│   ├── releasenote.md
│   ├── Model.png
│   ├── Projektstruktur.md
│   └── user_stories.md
│
├── requirements.txt                    # Python-Abhängigkeiten (Flask, pytest etc.)
├── README.md                           # Projektübersicht & Anleitung
└── pytest.ini                          # Pytest-Konfiguration
