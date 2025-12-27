from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []  # fake database

@app.route("/", methods=["GET", "POST"])
def users_page():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        if name and email:
            users.append({
                "id": len(users) + 1,
                "name": name,
                "email": email
            })

        return redirect(url_for("users_page"))

    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
