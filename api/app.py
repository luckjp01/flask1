from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask on Vercel!'})

# Vercel expects this to be called "app"
handler = app
