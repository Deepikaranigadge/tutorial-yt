from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    success_message = None

    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        if name and message:
            success_message = f"Thanks {name}, we received your message!"
        else:
            success_message = "All fields are required."

    return render_template("contact.html", success_message=success_message)

if __name__ == "__main__":
    app.run(debug=True)
