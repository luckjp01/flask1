from flask import Flask, request, render_template_string

app = Flask(__name__)

# A very simple user "database"
USERS = {
    "user1": "password123",
    "admin": "adminpass"
}

# Single-page login template with inline HTML
LOGIN_PAGE = """
<!doctype html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% elif success %}
        <p style="color: green;">{{ success }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    success = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Simple authentication check
        if username in USERS and USERS[username] == password:
            success = f"Welcome, {username}! You have logged in successfully."
        else:
            error = "Invalid username or password."
    return render_template_string(LOGIN_PAGE, error=error, success=success)

if __name__ == "__main__":
    app.run(debug=True)
