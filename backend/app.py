from flask import Flask, render_template, request, redirect, url_for
from .title_manager import TitleManager
from .parser import ContactParser
import os

template_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)
app = Flask(__name__, template_folder=template_dir)
app.secret_key = "super-secret-key"

title_manager = TitleManager()
parser = ContactParser(title_manager)
contacts = []

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add-contact":
            input_string = request.form.get("input-string")
            if input_string:
                result = input_string.strip()
                contacts.append(result)  # Kontakt speichern

        elif action == "add-title":
            new_title = request.form.get("new-title")
            gender = request.form.get("gender")
            if new_title and gender:
                title_manager.add_title(new_title, gender)

        return redirect(url_for("index"))
      
        # parsedNumber = parser.parse(number_input)
        # formatter = ContentFormatter()
    return render_template(
        "index.html",
        result=result,
        titles=title_manager.titles,
        contacts=contacts
    )
#Brief Anrede
@app.route("/briefanrede/<int:index>")
def briefanrede(index):
    contact = contacts[index]
    anrede = f"Sehr geehrte(r) {contact}"  # Beispieltext
    return anrede

if __name__ == "__main__":
    app.run(debug=True)
