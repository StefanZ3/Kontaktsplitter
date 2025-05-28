# Releasenote – Kontaktsplitter Prototyp

## Enthaltene Funktionen

- Automatische Zerlegung von Kontaktdaten in:
  - Anrede
  - Titel (inkl. Mehrfachtitel, akademische Titel und Adelstitel)
  - Vorname
  - Nachname
  - Geschlecht (basierend auf Anrede, Titel und Vornamen)
  - Sprache (basierend auf Anrede, z. B. „Mme.“, „Mrs.“ etc.)
- Generierung einer vollständigen Briefanrede gemäß den Empfehlungen des Dudens und des Bundesinnenministeriums, z. B.:  
  `Sehr geehrte Frau Professorin von Leuthäuser-Schnarrenberger`
- Benutzeroberfläche zur manuellen Bearbeitung aller erkannten Felder
- Möglichkeit zum Hinzufügen neuer Titel mit Geschlechtszuordnung und optionaler Angabe, ob der Titel in der Briefanrede berücksichtigt werden soll (sitzungsbasiert)
- Auflistung aller erfassten Kontakte mit den jeweils generierten Briefanreden innerhalb der aktuellen Sitzung
- Sitzungsbasierte Datenspeicherung (keine dauerhafte Speicherung der Daten)

## Testdaten


## Installation & Ausführung

### Voraussetzungen:
- Python 3.10+
- Pip

### Setup:

1. Repo klonen:
   ```bash
   git clone https://github.com/StefanZ3/Kontaktsplitter.git
   ```

2. In das Projektverzeichnis wechseln:
   ```bash
   cd Kontaktsplitter
   ```
3. Virtuelle Umgebung (Windows)(empfohlen)

   Virtuelle Umgebung anlegen:
   ```bash
   python -m venv venv
   ```
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

### Zugriff:

- Im Browser öffnen: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Webformular zur Eingabe und Analyse nutzen

## Bekannte Einschränkungen

- Die Sprach- und Ländererkennung ist rudimentär (z. B. „Mme“ → Französisch).
- Es erfolgt keine persistente Speicherung über die laufende Sitzung hinaus.
- Neu hinzugefügte Titel werden nur lokal gespeichert und nach Sitzungsende verworfen.
- Für neu hinzugefügte Titel erfolgt keine automatische Priorisierung in der Briefanrede – nur einige vordefinierte Titel werden korrekt behandelt, z. B.:
  - *Herr Prof. Dr.* → „Sehr geehrter Herr Professor“
  - *Herr Dr. rer. nat. Dr. med.* → „Sehr geehrter Herr Dr.“
  - *König* → „Eure Majestät“
  - *Prinzessin* → „Eure Königliche Hoheit“
- Es erfolgt keine automatische Fehlererkennung bei falsch geschriebenen Titeln, Anreden oder Namen.  
  Beispiel: „Dipl. Ing.“ ohne Bindestrich wird nicht als Titel erkannt, sondern fälschlicherweise als Namensbestandteil interpretiert – korrekt wäre „Dipl.-Ing.“
- Für eine korrekte Erkennung sollte die Namensangabe der folgenden Struktur folgen (sofern vorhanden):  
  `[Anrede] [Titel] [Vorname] [Nachname]`

## Verwendete Pakete

- `Flask` – Backend Web Framework
- `pytest` – Unit Testing Framework
- `gender-guesser` – zur automatischen Geschlechtserkennung basierend auf Vornamen
- `requests` – HTTP-Client für API-Aufrufe oder Webzugriffe (optional verwendet)

---

**Hinweis:** 
Dieser Prototyp wurde vom Team *SplitForce* im Rahmen der Vorlesung *„Softwarequalität“* an der DHBW Stuttgart Campus Horb entwickelt.