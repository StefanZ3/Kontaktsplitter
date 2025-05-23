# User Stories

Als Nutzer möchte ich, dass der Eingabe-String so zerlegt wird, dass Anrede, Titel, Geschlecht, Vorname, Nachname und eine standardisierte Briefanrede erstellt und angezeigt werden, damit ich einen Überblick über alle wichtigen Informationen erhalte.

Akzeptanzkriterien:

1. ...
2. ...

Als Nutzer möchte ich, dass alle generierten Briefanreden aller hinzugefügten Kontakte in der aktuellen Sitzung angezeigt werden, damit ich diese einsehen und verwenden kann.

Akzeptanzkriterien:

1. Es werden alle Briefanreden lokal gespeichert und angezeigt.

Als Nutzer möchte ich, dass alle Titel angezeigt werden und ein neuer Titel manuell hinzugefügt werden kann, damit das System diese automatisch erkennt und korrekt zuordnet.

Akzeptanzkriterien:

1. Es werden alle aktuellen Titel in einer Liste angezeigt.
2. Der Nutzer kann den neuen Titel in ein Textfeld eintragen und das zugehörige Geschlecht auswählen und über einen Button hinzufügen.
3. Beide Eingabefelder (Titel und Geschlecht) müssen ausgefüllt sein, um einen Titel hinzuzufügen. Der Nutzer wird informiert, wenn diese Eingabefelder nicht ausgefüllt sind.
4. Das System überprüft, ob der eingegebene Titel bereits existiert, um doppelte Einträge zu vermeiden.


Als Nutzer möchte ich auch manuell einzelne Felder korrigieren können, wenn die automatische Erkennung fehlschlägt.
Akzeptanzkriterium: 
1. Ein Dialog ermöglicht die manuelle Nachbearbeitung.

Als Nutzer möchte ich sicherstellen, dass bei Eingabe nur eines Worts dieses automatisch als Nachname erkannt wird.
Akzeptanzkriterium: 
1. Bei Eingabe von „Müller“ wird Nachname = Müller gesetzt, alle anderen Felder leer.

Als Nutzer möchte ich, dass aus den erkannten Bestandteilen automatisch eine vollständige, standardisierte Briefanrede erstellt wird damit ich diese direkt verwenden kann.
Akzeptanzkriterien:
1. Bei "Herr Dr. Max Mustermann" wird generiert: "Sehr geehrter Herr Dr. Mustermann".
2. Die Anrede berücksichtigt Titel und Geschlecht korrekt.

Sprache und Herkunft erkennen (nice to have)
Als Nutzer möchte ich, dass das System erkennt, wenn ein Name nicht deutsch ist damit ich über mögliche Formatierungsabweichungen informiert werde.
Akzeptanzkriterien:
1. Namen wie "Mme. Charlotte Noir" lösen eine Meldung "Sprache: Französisch" aus.
2. Eine entsprechende Empfehlung zur manuellen Prüfung wird angezeigt.
3. Die Sprache wird basierend auf Anrede oder Namensbestandteilen ermittelt (z. B. "Mrs.", "Mme", ...).
