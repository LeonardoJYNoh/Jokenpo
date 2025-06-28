jogadores = {}  # {id: nome}
jogadas = {}    # {id: jogada}

regras = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["tesoura", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
}

def jogadores_osciosos():
    return [nome for id, nome in jogadores.items() if id not in jogadas]
