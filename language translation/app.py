from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        src = request.form["source"]
        dest = request.form["target"]

        result = translator.translate(text, src=src, dest=dest)
        translated_text = result.text

    return render_template(
        "index.html",
        languages=LANGUAGES,
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)