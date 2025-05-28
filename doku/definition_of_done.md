# Definition of Done

## 1. Ziele

- Hohe Testabdeckung (Parser, Titel, Sprache, Geschlecht)
- Korrekte Zerlegung aller Bestandteile
- Korrekte Anzeige der extrahierten Daten nach der Verarbeitung durch den Parser
- Die Briefanrede wird für jeden Kontakt korrekt generiert (inkl. Adelstitel)
- Sprache wird automatisch anhand der Anrede erkannt (z. B. „Mme.“ = Französisch)
- Manuelle Eingabe- und Korrekturoptionen sind integriert und funktionsfähig
- Fehlerhafte oder unklare Eingaben führen zu sinnvoller Benutzerführung
- Neue Titel können manuell hinzugefügt und in der Sitzung verwendet werden
- Der Prototyp zeigt Beispieleingaben aus Testdaten korrekt an.

## 2. Testendekriterien

- Parser verarbeitet alle Beispiel-Testdaten fehlerfrei
- Titelketten, Doppelnamen und Sonderfälle (wie Nachnamenspräfixe) werden korrekt erkannt
- Sprache & Geschlecht werden korrekt bestimmt
- Alle User Stories wurden erfolgreich umgesetzt
- Alle gefundenen Fehler wurden behoben
- Die Anwendung läuft stabil unter Windows 11 mit Flask-Backend

## 3. Testmethoden / Abdeckung

- **Unit-Tests** zur Prüfung einzelner Module
- **Integrations-Tests** zur Überprüfung des Zusammenspiels der Komponenten
- **Manueletests** für die gesamte Verarbeitungskette (Eingabe → Ausgabe über UI)
- **Testfälle** sind direkt aus den User Stories abgeleitet

## 4. Dokumentation

- **Testplan** mit Teststrategie und Fallauswahl
- **Testprotokoll** mit durchgeführten Tests und Ergebnissen
- **Abschlussbericht** mit Bewertung der Testabdeckung, bekannten Einschränkungen und offenen Punkten
- **Releasenote** mit Liste umgesetzter Features und bekannter Einschränkungen
