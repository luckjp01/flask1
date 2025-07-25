from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! Welcome to my Flask app on Vercel!'

@app.route('/about')
def about():
    return 'This is the About page of the Flask app.'

if __name__ == '__main__':
    app.run()
