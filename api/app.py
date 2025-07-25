from flask import Flask, request, render_template_string

app = Flask(__name__)

USERS = {
    "user1": "password123",
    "admin": "adminpass"
}

LOGIN_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Login Page</title>
    <style>
        /* Reset and base */
        body, html {
            height: 100%;
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #71b7e6, #9b59b6);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .login-container {
            background: white;
            padding: 2.5rem 3.5rem;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
            width: 350px;
            text-align: center;
        }

        h2 {
            margin-bottom: 1.5rem;
            color: #333;
            font-weight: 700;
        }

        form {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
        }

        input[type="text"], input[type="password"] {
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: 1.8px solid #ccc;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }

        input[type="text"]:focus, input[type="password"]:focus {
            outline: none;
            border-color: #6a5acd;
            box-shadow: 0 0 8px rgba(106, 90, 205, 0.5);
        }

        input[type="submit"] {
            background: #6a5acd;
            border: none;
            color: white;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 0.85rem 0;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #5941a9;
        }

        .message {
            font-size: 0.95rem;
            padding: 0.75rem;
            border-radius: 8px;
        }

        .error {
            background-color: #f8d7da;
            color: #842029;
            margin-bottom: 1rem;
        }

        .success {
            background-color: #d1e7dd;
            color: #0f5132;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        {% if error %}
            <div class="message error">{{ error }}</div>
        {% elif success %}
            <div class="message success">{{ success }}</div>
        {% endif %}
        <form method="POST" novalidate>
            <input type="text" name="username" placeholder="Username" required autocomplete="username" />
            <input type="password" name="password" placeholder="Password" required autocomplete="current-password" />
            <input type="submit" value="Log In" />
        </form>
    </div>
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
        if username in USERS and USERS[username] == password:
            success = f"Welcome, {username}! You have logged in successfully."
        else:
            error = "Invalid username or password."
    return render_template_string(LOGIN_PAGE, error=error, success=success)

if __name__ == "__main__":
    app.run(debug=True)
