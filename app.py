from flask import Flask, request, jsonify

app = Flask(__name__)

jogadores = {}  # {id: nome}
jogadas = {}  # {id: jogada}

# Tabela "ganha de"
regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["tesoura", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
}

@app.route("/")
def home():
    return "API Jokenpô funcionando!"

@app.route("/jogador", methods=["POST"])
def cadastrar_jogador():

    """
    Registra um novo jogador.
    Espera JSON: { "id": 1, "nome": "Carlos" }
    """

    data = request.get_json()
    
    # Validação
    if not data or ("id" not in data) or ("nome" not in data):
        return jsonify({"erro": "Dados inválidos"}), 400

    #bloqueia IDs duplicados
    if data["id"] in jogadores:
        return jsonify({"erro": "Jogador já cadastrado"}), 400

    # Persistência na memória
    jogadores[data["id"]] = data["nome"]
    return jsonify({"mensagem": f"Jogador {data['nome']} cadastrado com sucesso!"}), 201

@app.route("/jogada", methods=["POST"])
def fazer_jogada():

    """
    Registra a escolha de um jogador.
    Espera JSON: { "id": 1, "jogada": "pedra" }
    """

    data = request.get_json()

    #validação
    if not data or ("id" not in data) or ("jogada" not in data):
        return jsonify({"erro": "Dados inválidos"}), 400

    #existência do jogador
    if data["id"] not in jogadores:
        return jsonify({"erro": "Jogador não encontrado"}), 404

    #bloqueia duplas jogadas
    if data["id"] in jogadas:
        return jsonify({"erro": "Jogador já jogou"}), 400

    escolha = data["jogada"].lower()

    #checa se a escolha é valida
    if jogada not in regras:
        return jsonify({"erro": "Jogada inválida"}), 400

    #armazena a escolha
    jogadas[data["id"]] = jogada
    return jsonify({"mensagem": f"Jogada registrada para {jogadores[data['id']]}"}), 201

if __name__ == "__main__":
    app.run(debug=True)

