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
    
    #Agrupa os IDs dos jogadores por tipo de jogada por um dicionario
    grupo_por_jogada= {}
    for id, jogada in jogadas.items():  
        if jogada not in grupo_por_jogada:
            grupo_por_jogada[jogada] = [] #cria uma chave jogada no dicionário com uma lista vazia
        grupo_por_jogada[jogada].append(id) #registra o ID do jogador a determinada jogada feita
    
    #Determina a quantidade de vitorias de cada jogada.
    vitorias_por_jogada = {} 
    for jogada, vencem_de in regras.items():    
        vitorias = 0
        for vencida in vencem_de:   
            vitorias += len(grupo_por_jogada.get(vencida, [])) #soma a quantidade de ganhos da jogada
        vitorias_por_jogada[jogada] = vitorias  #demonstra quantas quantas vitorias tem cada jogada

    resultados = {}
    for jogada, ids in grupo_por_jogada.items():
        for id in ids:
            resultados[id] = vitorias_por_jogada[jogada]

    maior_vitoria = max(resultados.values())
    vencedores = [jogadores[id] for id, v in resultados.items() if v == maior_vitoria]

    jogadas.clear()
    return jsonify({"vencedores": vencedores})

if __name__ == "__main__":
    app.run(debug=True)
