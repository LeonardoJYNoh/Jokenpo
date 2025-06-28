from flask import Flask
from rotas import register_blueprints

app = Flask(__name__)

# Registro dos blueprints definidos em rotas/__init__.py
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)