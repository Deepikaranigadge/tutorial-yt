from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name} (Data received using POST)"

    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)
