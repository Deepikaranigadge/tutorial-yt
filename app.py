from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h2>Hello, {name}!</h2>"

    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)
