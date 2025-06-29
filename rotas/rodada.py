from flask import Blueprint, jsonify
from servicos.core import jogadores, jogadas, regras

rodada_bp = Blueprint("rodada", __name__)

def jogadores_osciosos(): 

    """
    essa função serve para detectar jogadores que não estajam jogando na rodada
    """

    osciosos = []

    for id, nome in jogadores.items():
        if id not in jogadas:
            osciosos.append(nome)

    return osciosos

@rodada_bp.route("/rodada", methods=["GET"])
def consultar_rodada():
    
    """
    Retorna o estado atual da rodada:
    - Jogadores cadastrados
    - Quem jogou
    - Quem não jogou
    """

    cadastrados = list(jogadores.values())

    jogaram = []

    for id in jogadas:
        nome = jogadores[id]
        jogaram.append(nome)

    osciosos = jogadores_osciosos()

    return jsonify({
        "jogadores": cadastrados,
        "jogaram": jogaram,
        "osciosos": osciosos
    })

@rodada_bp.route("/rodada/finalizar", methods=["POST"])
def finalizar_rodada():

    """
    Finaliza a rodada e determina o(s) vencedor(es).
    Retorna erro se ainda houver jogadores que não jogaram.
    """

    osciosos = jogadores_osciosos()

    if osciosos:
        return jsonify({
            "erro": "Ainda há jogadores que não jogaram",
            "jogadores_pendentes": osciosos
        }), 400
    
    if len(jogadas) < 2:
        return jsonify({
            "erro": "Jogadores insuficientes para finalizar a rodada. Mínimo de 2 jogadores."
        }), 400


    #Agrupa os IDs dos jogadores por tipo de jogada por um dicionario
    grupo_por_jogada= {}

    for id, jogada in jogadas.items():  
        if jogada not in grupo_por_jogada:
            grupo_por_jogada[jogada] = [] #cria uma chave jogada no dicionário com uma lista vazia
        grupo_por_jogada[jogada].append(id) #registra o ID agrupando pelas jogadas feitas
    

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
    #Lista os nomes dos jogadores que tiveram a maior pontuação de vitórias nesta rodada.

    return jsonify({"vencedores": vencedores}), 200

@rodada_bp.route("/rodada/reset", methods=["POST"])
def reset_rodada():

    jogadas.clear()
    return jsonify({"mensagem": "Rodada reiniciada com sucesso!"}), 200