from flask import Blueprint, request, jsonify
from servicos.core import jogadores, jogadas

jogador_bp = Blueprint("jogador", __name__)

@jogador_bp.route("/jogador", methods=["POST"])
def cadastrar_jogador():

    """
    Registra um novo jogador.
    Espera JSON: { "id": 1, "nome": "Carlos" }
    """

    data = request.get_json()
    
    if not data or ("id" not in data) or ("nome" not in data):
        return jsonify({"erro": "Dados inválidos"}), 400
    if not data["nome"].strip():
        return jsonify({"erro": "Nome do jogador não pode ser vazio"}), 400
    if data["id"] in jogadores:
        return jsonify({"erro": "Jogador já cadastrado"}), 400
    jogadores[data["id"]] = data["nome"]    
    return jsonify({"mensagem": f"Jogador {data['nome']} cadastrado com sucesso!"}), 201


@jogador_bp.route("/jogador/<int:id>", methods=["DELETE"])
def remover_jogador(id):

    """
    Remove um jogador cadastrado pelo ID.
    Também remove sua jogada, se já tiver jogado.
    """

    if id not in jogadores:
        return jsonify({"erro": "Jogador não encontrado"}), 404
    nome = jogadores.pop(id)  # Remove o jogador
    jogadas.pop(id, None)     # Remove a jogada (se existir)

    return jsonify({"mensagem": f"Jogador {nome} removido com sucesso!"})

