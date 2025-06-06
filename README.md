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

Dieses Prototyp wurde vom Team *SplitForce* im Rahmen der Vorlesung *„Softwarequalität“* an der DHBW Stuttgart Campus Horb entwickelt.

## Installation & Ausführung

### Voraussetzungen
- Python 3.10+
- Pip
- Git

### Schritte
1. Repo klonen:
   ```bash
   git clone https://github.com/StefanZ3/Kontaktsplitter.git
   ```

2. In das Projektverzeichnis wechseln:
   ```bash
   cd Kontaktsplitter
   ```

3. Virtuelle Umgebung (Windows)(empfohlen)

   **Wichtig bei PowerShell-Fehlermeldung:**  
   Falls beim Ausführen der virtuellen Umgebung eine Fehlermeldung wie  
   *„Die Ausführung von Skripten ist auf diesem System deaktiviert“* erscheint, muss die Ausführungsrichtlinie geändert werden. Führe dazu vor dem Aktivieren der Umgebung einen der folgenden Befehle aus. Je nach System können Administratorrechte erforderlich sein::

   - **Nur für die aktuelle PowerShell-Session:**
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
     ```
   - **Für den aktuellen Benutzer dauerhaft:**
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```

   Virtuelle Umgebung anlegen:
   ```bash
   python -m venv venv
   ```

   > Hinweis: Unter Windows kann es nötig sein, statt `python` den Befehl `py` zu verwenden, wenn python nicht in der Systeemvariable `PATH` steht:
   > ```bash
   > py -m venv venv
   > ```

   Virtuelle Umgebung starten:
   ```bash
   .\venv\Scripts\activate
   ```

4. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

5. Anwendung starten:
   ```bash
   python -m backend.app
   ```
   > Hinweis: Unter Windows kann es nötig sein, statt `python` den Befehl `py` zu verwenden, wenn python nicht in der Systeemvariable `PATH` steht:
   > ```bash
   > py -m backend.app
   > ```


6. Im Browser öffnen:
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
