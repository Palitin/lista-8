from flask import Flask, render_template
import classes

app = Flask(__name__)

@app.route("/")
def index():
    clubes = classes.clubes
    conteudo = render_template("index.html", clubes=clubes)
    return conteudo


if __name__ == "__main__":
    app.run(debug=True)
