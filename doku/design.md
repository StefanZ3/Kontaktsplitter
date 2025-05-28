## Technische Architekturbeschreibung 

### Überblick

Die Anwendung „Kontaktsplitter“ besteht aus einem HTML-basierten Frontend und einem modular aufgebauten Python-Backend mit Flask. Sie dient der Zerlegung von Kontaktdaten und der Generierung formeller Briefanreden. Eine persistente Speicherung erfolgt nicht.

---

### Komponenten

#### Frontend
- HTML-Formular zur Eingabe und Bearbeitung von Namen
- Editierbare Felder (Anrede, Titel, Vorname, Nachname, Geschlecht)
- Hinzufügen neuer Titel via Eingabe
- Anzeige aller erzeugten Briefanreden durch betätigen des Buttons beim angelegten Kontakt
- Bootstrap für Gestaltung
- Übergabe der Daten über klassische HTML-POST-Requests

#### Backend (Flask)
| Route                  | Funktion                                                                |
|------------------------|-------------------------------------------------------------------------|
| `/`                    | Startseite, Formular zur Eingabe & Hinzufügen von Titeln                |
| `/split`               | Nimmt Roh-Namen als JSON, gibt geparste Felder zurück (`contact_parser`)|
| `/save_contact`        | Fügt Kontakt zur temporären RAM-Liste hinzu                             |
| `/briefanrede/<index>` | Gibt Briefanrede zum Kontakt zurück (per Index aus RAM-Liste)           |

---

### Backend-Module

| Modul                            | Aufgabe |
|----------------------------------|---------|
| `contact_parser.py`              | Zerlegung in Anrede, Titel, Vorname, Nachname |
| `gender_detector.py`             | Geschlecht erkennen |
| `language_detector.py`           | Sprache identifizieren |
| `letter_salutation_generator.py` | Briefanrede erzeugen |
| `title_manager.py`               | Verwaltung der Titel + Hinzufügen |
| `constants.py`                   | Enthält Titel,Namens Prefixe, Briefanreden, Übersetzungen|

---

### Datenspeicherung

- Alle Daten werden **nur temporär in einer In-Memory-Liste (`contacts`) gehalten**
- Kein Einsatz einer Datenbank oder Dateispeicherung

---