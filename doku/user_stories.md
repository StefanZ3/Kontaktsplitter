# User Stories

## 1. Automatische Zerlegung von Namen

**Als Nutzer** möchte ich einen Namen eingeben können, der automatisch in Anrede, Titel, Vorname, Nachname, Geschlecht und Sprache zerlegt wird,  
**damit** ich alle relevanten Informationen auf einen Blick sehe.

**Akzeptanzkriterien:**
- Bei Eingabe von z. B. „Herr Dr. Max Mustermann“ wird korrekt erkannt:
  - Anrede: Herr
  - Titel: Dr.
  - Vorname: Max
  - Nachname: Mustermann
  - Geschlecht: männlich
  - Sprache: Deutsch
- Aus den Bestandteilen wird automatisch eine vollständige Briefanrede generiert:  
  „Sehr geehrter Herr Dr. Mustermann“

## 2. Manuelle Korrektur

**Als Nutzer** möchte ich einzelne erkannte Felder manuell korrigieren können,  
**damit** ich falsche automatische Zuordnungen anpassen kann.

**Akzeptanzkriterien:**
- Alle Felder sind in der UI editierbar.
- Eine Korrektur ist vor dem Speichern möglich.
- Ein Dialog oder Interface-Element ermöglicht die manuelle Bearbeitung.

## 3. Hinzufügen neuer Titel

**Als Nutzer** möchte ich neue Titel zur Erkennung hinzufügen können,  
**damit** das System diese automatisch berücksichtigt.

**Akzeptanzkriterien:**
- Es wird eine Liste der aktuell bekannten Titel angezeigt.
- Ein neuer Titel kann in ein Textfeld eingetragen werden.
- Das zugehörige Geschlecht muss ausgewählt werden.
- Beide Felder (Titel und Geschlecht) sind Pflichtangaben.
- Eine Prüfung verhindert doppelte Einträge.
- Nach erfolgreicher Eingabe wird der Titel für die laufende Sitzung übernommen.

## 4. Anzeige aller generierten Briefanreden

**Als Nutzer** möchte ich, dass alle Briefanreden der bearbeiteten Kontakte angezeigt werden,  
**damit** ich diese einsehen und direkt verwenden kann.

**Akzeptanzkriterien:**
- Generierte Anreden werden durch einen Button bei dem Kontakt angezeigt.
- Die Daten bleiben während der Sitzung verfügbar.

## 5. Verarbeitung von Ein-Wort-Eingaben

**Als Nutzer** möchte ich, dass bei Eingabe nur eines Worts dieses automatisch als Nachname erkannt wird,  
**damit** einfache Fälle schnell erfasst werden können.

**Akzeptanzkriterium:**
- Bei Eingabe von „Müller“ wird gesetzt:
  - Nachname: Müller
  - Alle anderen Felder bleiben leer

## 6. Spracherkennung (Nice to Have)

**Als Nutzer** möchte ich, dass das System erkennt, wenn ein Name aus einer anderen Sprache stammt,  
**damit** ich auf mögliche Abweichungen hingewiesen werde.

**Akzeptanzkriterien:**
- Namen wie „Mme. Charlotte Noir“ führen zur Anzeige: „Sprache: Französisch“
- Eine Empfehlung zur manuellen Prüfung wird angezeigt.
- Die Sprache wird anhand der Anrede oder Namensbestandteile erkannt (z. B. „Mrs.“, „Mme“, …)
