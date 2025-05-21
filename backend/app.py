from flask import Flask, render_template, request
from .title_manager import TitleManager
from .parser import ContactParser
import os

template_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)
app = Flask(__name__, template_folder=template_dir)
title_manager = TitleManager()
parser = ContactParser(title_manager)


@app.route("/", methods=["GET", "POST"])
def index():
    result = {}

    if request.method == "POST":
        action = request.form.get("action")

        if action == "add-contact":
            input_string = request.form.get("input-string")
            if input_string:
                result = input_string

        if action == "add-title":
            new_title = request.form.get("new-title")
            if new_title:
                title_manager.add_title(new_title)

        # parsedNumber = parser.parse(number_input)
        # formatter = ContentFormatter()
    return render_template(
        "index.html",
        result=result,
        titles=title_manager.titles,
    )


if __name__ == "__main__":
    app.run(debug=True)
