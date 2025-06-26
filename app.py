from flask import Flask, request, jsonify

app = Flask(__name__)

# Armazenamento temporário
jogadores = {}

@app.route("/")
def home():
    return "API Jokenpô funcionando!"

@app.route("/jogador", methods=["POST"])
def cadastrar_jogador():
    data = request.get_json()
    
    if not data or "id" not in data or "nome" not in data:
        return jsonify({"erro": "Dados inválidos"}), 400
    
    if data["id"] in jogadores:
        return jsonify({"erro": "Jogador já cadastrado"}), 400
    
    jogadores[data["id"]] = data["nome"]
    return jsonify({"mensagem": f"Jogador {data['nome']} cadastrado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)