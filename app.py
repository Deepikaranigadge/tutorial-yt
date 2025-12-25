from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# =====================================================
# 1️⃣ GET DATA USING URL (request.args)
# URL: http://127.0.0.1:5000/search?name=Deepika
# =====================================================
@app.route('/search')
def search():
    name = request.args.get('name')
    return f"Searching for: {name}"


# =====================================================
# 2️⃣ GET + POST USING SINGLE ROUTE (HTML FORM)
# =====================================================
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Form submitted by {name}"

    # GET request
    return '''
        <form method="POST">
            <input name="name" placeholder="Enter name">
            <button type="submit">Submit</button>
        </form>
    '''


# =====================================================
# 3️⃣ SEPARATE GET & POST ROUTES (BEST PRACTICE - LOGIN)
# =====================================================
@app.route('/login', methods=['GET'])
def login():
    return '''
        <form method="POST" action="/login">
            <input name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    return f"Logged in as {username}"


# =====================================================
# 4️⃣ API STYLE (JSON POST)
# Test using Postman
# =====================================================
@app.route('/api/user', methods=['POST'])
def api_user():
    data = request.get_json()
    return jsonify({
        "username": data['username'],
        "status": "created"
    })


# =====================================================
# RUN APP
# =====================================================
if __name__ == '__main__':
    app.run(debug=True)
