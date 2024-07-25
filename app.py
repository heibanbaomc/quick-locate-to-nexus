from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["POST"])
def main():
    r = request.form.get("q")
    return render_template("main.html", r=r)

@app.route("/locate", methods=["POST"])
def locate():
    r = request.form.get("q")
    if r:
        url = f"https://www.nexusmods.com/skyrimspecialedition/mods/{r}?tab=files"
        return redirect(url)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()