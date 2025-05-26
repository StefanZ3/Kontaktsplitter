from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from .title_manager import TitleManager
from .contact_parser import ContactParser
from .letter_salutation_generator import LetterSalutationGenerator
import os

template_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)

# Initialisiert die Flask-App
app = Flask(__name__, template_folder=template_dir)
app.secret_key = "super-secret-key"  # Für Flash-Messages

# Hilfsobjekte
title_manager = TitleManager()
parser = ContactParser(title_manager)
letter_generator = LetterSalutationGenerator(title_manager)

# In-Memory-Speicherung der Kontakte (nicht persistent)
contacts = []

@app.route("/", methods=["GET", "POST"])
def index():
    """Startseite der App. Zeigt die Titel und bestehenden Kontakte an.
    Verarbeitet außerdem das Hinzufügen neuer Titel über ein Formular."""

    if request.method == "POST":
        action = request.form.get("action", "").strip()

        if action == "add-title":
            new_title = request.form.get("new-title", "").strip()
            gender = request.form.get("gender", "").strip()
            include_in_salutation_str = request.form.get("include_in_salutation", "").strip()
            include_in_salutation = include_in_salutation_str.lower() == "true"

            if not new_title or not gender:
                flash("Bitte geben Sie sowohl Titel als auch Geschlecht an.", "danger")
            elif title_manager.is_known_title(new_title):
                flash(f"Der Titel '{new_title}' ist bereits vorhanden.", "warning")
            else:
                title_manager.add_title(new_title, gender, include_in_salutation)
                flash(f"Der Titel '{new_title}' wurde erfolgreich hinzugefügt.", "success")

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        titles=title_manager.titles,
        contacts=contacts
    )

@app.route("/split", methods=["POST"])
def split_new_contact():
    """API-Endpunkt zum Parsen eines neuen Kontakts.
    Erwartet JSON mit dem Schlüssel "new_contact".
    Gibt geparste Kontaktinformationen zurück."""

    data = request.get_json()
    new_contact = data.get("new_contact", "").strip()

    if not new_contact:
        return jsonify({"error": "Leerer Kontakt"}), 400
    
    parsed = parser.parse(new_contact)
    return jsonify(parsed)

@app.route("/save_contact", methods=["POST"])
def save_contact():
    """API-Endpunkt zum Speichern eines Kontakts.
    Erwartet JSON-Daten mit Kontaktinformationen.
    Fügt den Kontakt der In-Memory-Liste hinzu und gibt eine Erfolgsmeldung zurück."""

    data = request.get_json()
    contacts.append(data)
    flash("Kontakt erfolgreich hinzugefügt.", "success")

    return jsonify({"status": "success"})

@app.route("/briefanrede/<int:index>")
def briefanrede(index):
    """Gibt eine Briefanrede für den Kontakt mit dem angegebenen Index zurück."""

    try:
        contact = contacts[index]
    except IndexError:
        return "Kontakt nicht gefunden", 404

    letter=letter_generator.get_letter_salutation(contact)
    return letter

if __name__ == "__main__":
    app.run(debug=True)
