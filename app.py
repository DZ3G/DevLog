from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devlog.db'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "DevLog fonctionne !"

if __name__ == '__main__':
    app.run(debug=True)