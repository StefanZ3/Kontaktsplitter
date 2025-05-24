from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from .title_manager import TitleManager
# from .contact_parser import ContactParser
from .parser2 import ContactParser
from .gender_detector import GenderDetector
import os

template_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)

app = Flask(__name__, template_folder=template_dir)
app.secret_key = "super-secret-key"  # Für Flash-Messages

# Hilfsobjekte
title_manager = TitleManager()
parser = ContactParser(title_manager)
gender_detector = GenderDetector()
contacts = []  # In-Memory-Speicherung

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "add-title":
            new_title = request.form.get("new-title")
            gender = request.form.get("gender")
            if new_title and gender:
                title_manager.add_title(new_title.strip(), gender)
                flash("Titel erfolgreich hinzugefügt.", "success")

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        titles=title_manager.titles,
        contacts=contacts
    )

@app.route("/split", methods=["POST"])
def split_kontakt():
    data = request.get_json()
    kontakt = data.get("kontakt", "")
    if not kontakt.strip():
        return jsonify({"error": "Leerer Kontakt"}), 400
    
    parsed = parser.parse(kontakt)
    gender = gender_detector.get_gender(parsed)

    return jsonify(parsed)

@app.route("/save_contact", methods=["POST"])
def save_contact():
    data = request.get_json()
    # Daten extrahieren
    titel = data.get("titel", "").strip()
    vorname = data.get("vorname", "").strip()
    nachname = data.get("nachname", "").strip()

    kontakt_string = f"{titel} {vorname} {nachname}".strip()
    contacts.append(kontakt_string)
    flash("Kontakt erfolgreich hinzugefügt.", "success")

    return jsonify({"status": "success"})

@app.route("/briefanrede/<int:index>")
def briefanrede(index):
    try:
        contact = contacts[index]
    except IndexError:
        return "Kontakt nicht gefunden", 404

    # Beispielhafte Briefanrede
    anrede = f"Sehr geehrte(r) {contact}"
    return anrede

if __name__ == "__main__":
    app.run(debug=True)
