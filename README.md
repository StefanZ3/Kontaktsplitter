# Kontaktsplitter

## Projektbeschreibung

Der Kontaktsplitter ist ein Web-Prototyp zur Zerlegung von Kontaktangaben (z. B. aus Visitenkarten oder Formularen) in strukturierte Einzelfelder:
- Anrede
- Titel
- Vorname
- Nachname
- Geschlecht
- Sprache
- Briefanrede

Das Tool unterstützt auch manuelle Nachbearbeitung und das dynamische Hinzufügen von Titeln.

Es wurde im Rahmen der Vorlesung „Softwarequalität“ an der DHBW Stuttgart Campus Horb entwickelt.

## Installation & Ausführung

### Voraussetzungen
- Python 3.10+
- Pip

### Schritte
1. Repo klonen:
   ```bash
   git clone https://github.com/StefanZ3/Kontaktsplitter.git
   ```

2. In das Projektverzeichnis wechseln:
   ```bash
   cd Kontaktsplitter
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. Anwendung starten:
   ```bash
   python -m backend.app
   ```

4. Im Browser öffnen:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)


## Tests

Die Tests können mit `pytest` im Projektverzeichnis ausgeführt werden:
```bash
pytest
```

## Projektstruktur

- `backend/`: Enthält die Logik zur Zerlegung, Titelverwaltung, Spracherkennung etc.
- `frontend/`: HTML-UI mit Bootstrap
- `tests/`: Unit-Tests für zentrale Module
- `doku/`: Projektdokumentation inkl. User Stories, DoD, Design
