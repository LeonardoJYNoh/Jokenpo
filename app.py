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

def jogadores_osciosos(): 

    """
    essa função serve para detectar jogadores que não estajam jogando na rodada
    """
    osciosos = []
    for id, nome in jogadores.items():
        if id not in jogadas:
            osciosos.append(nome)
    return osciosos

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

@app.route("/jogador/<int:id>", methods=["DELETE"])
def remover_jogador():
    """
    Remove um jogador cadastrado pelo ID.
    Também remove sua jogada, se já tiver jogado.
    """
    if id not in jogadores:
        return jsonify({"erro": "Jogador não encontrado"}), 404

    nome = jogadores.pop(id)  # Remove o jogador
    jogadas.pop(id, None)     # Remove a jogada (se existir)

    return jsonify({"mensagem": f"Jogador {nome} removido com sucesso!"})

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

    jogada = data["jogada"].lower()

    #checa se a escolha é valida
    if jogada not in regras:
        return jsonify({"erro": "Jogada inválida"}), 400

    #armazena a jogada
    jogadas[data["id"]] = jogada
    return jsonify({"mensagem": f"Jogada registrada para {jogadores[data['id']]}"}), 201


@app.route("/rodada", methods=["GET"])
def consultar_rodada():
    
    """
    Retorna o estado atual da rodada:
    - Jogadores cadastrados
    - Quem jogou
    - Quem não jogou
    """

    #todos os jogadores
    cadastrados = list(jogadores.values())

    #lista das pessoas que jogaram
    jogaram = []
    for id in jogadas:
        nome = jogadores[id]
        jogaram.append(nome)

    #lista de pessoas que não jogaram
    osciosos = jogadores_osciosos()


    return jsonify({
        "jogadores": cadastrados,
        "jogaram": jogaram,
        "osciosos": osciosos
    })

@app.route("/rodada/finalizar", methods=["POST"])
def finalizar_rodada():

    """
    Finaliza a rodada e determina o(s) vencedor(es).
    Retorna erro se ainda houver jogadores que não jogaram.
    """

    #busca a lista de pessoas que não jogaram
    osciosos = jogadores_osciosos()

    #caso oscioso, vai retornar um erro, e uma lista das pessoas que não jogaram ainda
    if osciosos:
        return jsonify({
            "erro": "Ainda há jogadores que não jogaram",
            "jogadores_pendentes": osciosos
        }), 400
    
    # Calcula o número de vitórias de cada jogador, quem tiver a maior quantidade de vitórias vence a rodada dentro de uma biblioteca
    resultados = {}

    #uso de loops duplos para comparar o "duelo" de dois jogadores até completar todas as duplas, possiveis
    for id_1, jogada_1 in jogadas.items():
        vitorias = 0
        for id_2, jogada_2 in jogadas.items():
            if id_1 != id_2 and jogada_2 in regras[jogada_1]: #se os jogadores forem diferetes jogada do primeiro vence
                vitorias += 1
        resultados[id_1] = vitorias #registra a quantidade de vitorias

    maior_vitoria = max(resultados.values()) #vai determinar o maior numero de vitorias 
    vencedores = [] 

    #nesse loop, listamos os jogadores que ganharam essa rodada
    for id, vitorias in resultados.items():
        if vitorias == maior_vitoria:
            vencedores.append(jogadores[id])

    # Limpa a rodada
    jogadas.clear()

    return jsonify({"vencedores": vencedores})



if __name__ == "__main__":
    app.run(debug=True)
