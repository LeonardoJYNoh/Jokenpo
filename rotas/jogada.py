from flask import Blueprint, request, jsonify
from servicos.core import jogadores, jogadas, regras

jogada_bp = Blueprint("jogada", __name__)

@jogada_bp.route("/jogada", methods=["POST"])
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