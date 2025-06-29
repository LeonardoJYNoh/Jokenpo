<<<<<<< HEAD
# JOKENPO - DEV

> **Desafio:** Construir uma API REST que gerencie partidas de jokenpô (versão estendida) entre vários jogadores.

---

## Sumário
1. [Visão Geral]
2. [Stack Tecnológico]
3. [Setup & Execução]
4. [Estrutura de Pastas]
5. [Decisões Arquiteturais]
6. [Referência da API]
7. [Regras do Jogo]
---

## Visão Geral
Esta aplicação oferece uma **API REST** capaz de:
* Cadastrar e remover jogadores  
* Registrar jogadas individuais  
* Consultar o estado atual da rodada  
* Finalizar e reiniciar rodadas  
* Calcular automaticamente o(s) vencedor(es) segundo as regras de jokenpô estendido (pedra / papel / tesoura / lagarto / spock)

---

## Stack Tecnológico
| Camada        | Tecnologia | Observação |
|---------------|------------|------------|
| **Backend**   | **Flask**  | Framework web leve para APIs |
| Rotas         | Flask Blueprints | Facilita modularização |
| CORS          | flask-cors | Libera acesso do frontend |
| **Frontend*** | HTML + JS puro | Interface simples |
| Execução      | Python 3.10+ | Recomendado 3.10 ou superior |

\* O frontend não faz parte do escopo principal.

---

## Setup & Execução

### 1 — Clonar o repositório
```bash
git clone <https://github.com/LeonardoJYNoh/Jokenpo-DEV> jokenpo-dev
cd jokenpo-dev
```

### 2 — (Opcional) Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# ou
.venv\Scripts\activate.bat     # Windows
```

### 3 — Instalar dependências
```bash
pip install flask flask-cors
```

### 4 — Iniciar o servidor
```bash
python app.py
```
> A API será exposta em **http://localhost:5000**

### 5 — Testar via navegador ou Insomnia  
Abra o arquivo `frontend/index.html` (ou use Live Server) para testar visualmente, ou siga os exemplos no Insomnia abaixo.

---

## Estrutura de Pastas
```
jokenpo-dev/
│
├── app.py                # bootstrap Flask + CORS + blueprints
│
├── rotas/                # camada de interface HTTP
│   ├── __init__.py       # register_blueprints()
│   ├── jogador.py        # /jogador    (POST, DELETE)
│   ├── jogada.py         # /jogada     (POST)
│   └── rodada.py         # /rodada ... (GET, POST)
│
├── servicos/
│   └── core.py           # dicionários in-memory e regras do jogo
│
└── frontend/             # (opcional) interface web
    ├── index.html
    ├── script.js
    └── style.css
```

---

## Decisões Arquiteturais
| Decisão | Motivação |
|---------|-----------|
| **Flask Blueprints** para cada grupo de rotas | Mantém o código enxuto e modular, facilita manutenção e testes isolados |
| **Armazenamento em memória** (dict) | Elimina complexidade de banco para cumprir o escopo do desafio rapidamente |
| **CORS global via flask-cors** | Permite que qualquer ferramenta ou frontend local consuma a API|
| **Regras isoladas em servicos/core.py** | Um único ponto de verdade para as regras do jogo facilita extensão futura |
| **Frontend** | Demonstra o funcionamento sem depender de ferramentas externas, mas sem poluir o backend |

> **Escalabilidade:** Caso seja necessário persistir dados, basta substituir os dicionários por modelos SQLAlchemy ou outro ODM/ORM, mantendo as assinaturas das funções.

---

## Referência da API

### Jogadores
| Método | Endpoint            | Descrição                     |
|--------|---------------------|-------------------------------|
| POST | /jogador`         | Cadastra um novo jogador      |
| DELETE | /jogador/<id>   | Remove jogador e sua jogada   |

**POST /jogador – Body**
```json
{ "id": 1, "nome": "Carlos" }
```

---

### Jogadas
| Método | Endpoint  | Descrição                |
|--------|-----------|--------------------------|
| POST | /jogada | Registra jogada do ID    |

**POST /jogada – Body**
```json
{ "id": 1, "jogada": "pedra" }
```

Jogadas válidas: pedra, papel, tesoura, lagarto, spock

---

### Rodada
| Método | Endpoint              | Descrição                               |
|--------|-----------------------|-----------------------------------------|
| GET  | /rodada             | Estado atual (quem jogou / faltam)      |
| POST | /rodada/finalizar   | Finaliza rodada e devolve vencedor(es)  |
| POST | /rodada/reset       | Limpa jogadas (jogadores permanecem)    |

---

## Regras do Jogo
| Jogada  | Vence de                |
|---------|-------------------------|
| Pedra   | Tesoura · Lagarto       |
| Papel   | Pedra   · Spock         |
| Tesoura | Papel   · Lagarto       |
| Lagarto | Spock   · Papel         |
| Spock   | Tesoura · Pedra         |

O cálculo de vencedor é feito:
  
1. Agrupar jogadores por tipo de jogada
2. Para cada jogada possível (como ‘pedra’), o sistema verifica quais jogadas ela vence e conta quantos jogadores escolheram essas jogadas na rodada. A soma desses jogadores representa a pontuação daquela jogada.
3. Atribuir pontos individuais a cada jogador
4. Determinar o(s) vencedor(es)

---

> Desenvolvido por Leonardo como parte do desafio **JOKENPO - DEV**.  
=======
# JOKENPO - DEV

> **Desafio:** Construir uma API REST que gerencie partidas de jokenpô (versão estendida) entre vários jogadores.

---

## Sumário
1. [Visão Geral]
2. [Stack Tecnológico]
3. [Setup & Execução]
4. [Estrutura de Pastas]
5. [Decisões Arquiteturais]
6. [Referência da API]
7. [Regras do Jogo]
---

## Visão Geral
Esta aplicação oferece uma **API REST** capaz de:
* Cadastrar e remover jogadores  
* Registrar jogadas individuais  
* Consultar o estado atual da rodada  
* Finalizar e reiniciar rodadas  
* Calcular automaticamente o(s) vencedor(es) segundo as regras de jokenpô estendido (pedra / papel / tesoura / lagarto / spock)

---

## Stack Tecnológico
| Camada        | Tecnologia | Observação |
|---------------|------------|------------|
| **Backend**   | **Flask**  | Framework web leve para APIs |
| Rotas         | Flask Blueprints | Facilita modularização |
| CORS          | flask-cors | Libera acesso do frontend |
| **Frontend*** | HTML + JS puro | Interface simples |
| Execução      | Python 3.10+ | Recomendado 3.10 ou superior |

\* O frontend não faz parte do escopo principal.

---

## Setup & Execução

### 1 — Clonar o repositório
```bash
git clone <https://github.com/LeonardoJYNoh/Jokenpo-DEV> jokenpo-dev
cd jokenpo-dev
```

### 2 — (Opcional) Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# ou
.venv\Scripts\activate.bat     # Windows
```

### 3 — Instalar dependências
```bash
pip install flask flask-cors
```

### 4 — Iniciar o servidor
```bash
python app.py
```
> A API será exposta em **http://localhost:5000**

### 5 — Testar via navegador ou Insomnia  
Abra o arquivo `frontend/index.html` (ou use Live Server) para testar visualmente, ou siga os exemplos no Insomnia abaixo.

---

## Estrutura de Pastas
```
jokenpo-dev/
│
├── app.py                # bootstrap Flask + CORS + blueprints
│
├── rotas/                # camada de interface HTTP
│   ├── __init__.py       # register_blueprints()
│   ├── jogador.py        # /jogador    (POST, DELETE)
│   ├── jogada.py         # /jogada     (POST)
│   └── rodada.py         # /rodada ... (GET, POST)
│
├── servicos/
│   └── core.py           # dicionários in-memory e regras do jogo
│
└── frontend/             # (opcional) interface web
    ├── index.html
    ├── script.js
    └── style.css
```

---

## Decisões Arquiteturais
| Decisão | Motivação |
|---------|-----------|
| **Flask Blueprints** para cada grupo de rotas | Mantém o código enxuto e modular, facilita manutenção e testes isolados |
| **Armazenamento em memória** (dict) | Elimina complexidade de banco para cumprir o escopo do desafio rapidamente |
| **CORS global via flask-cors** | Permite que qualquer ferramenta ou frontend local consuma a API|
| **Regras isoladas em servicos/core.py** | Um único ponto de verdade para as regras do jogo facilita extensão futura |
| **Frontend** | Demonstra o funcionamento sem depender de ferramentas externas, mas sem poluir o backend |

> **Escalabilidade:** Caso seja necessário persistir dados, basta substituir os dicionários por modelos SQLAlchemy ou outro ODM/ORM, mantendo as assinaturas das funções.

---

## Referência da API

### Jogadores
| Método | Endpoint            | Descrição                     |
|--------|---------------------|-------------------------------|
| POST | /jogador`         | Cadastra um novo jogador      |
| DELETE | /jogador/<id>   | Remove jogador e sua jogada   |

**POST /jogador – Body**
```json
{ "id": 1, "nome": "Carlos" }
```

---

### Jogadas
| Método | Endpoint  | Descrição                |
|--------|-----------|--------------------------|
| POST | /jogada | Registra jogada do ID    |

**POST /jogada – Body**
```json
{ "id": 1, "jogada": "pedra" }
```

Jogadas válidas: pedra, papel, tesoura, lagarto, spock

---

### Rodada
| Método | Endpoint              | Descrição                               |
|--------|-----------------------|-----------------------------------------|
| GET  | /rodada             | Estado atual (quem jogou / faltam)      |
| POST | /rodada/finalizar   | Finaliza rodada e devolve vencedor(es)  |
| POST | /rodada/reset       | Limpa jogadas (jogadores permanecem)    |

---

## Regras do Jogo
| Jogada  | Vence de                |
|---------|-------------------------|
| Pedra   | Tesoura · Lagarto       |
| Papel   | Pedra   · Spock         |
| Tesoura | Papel   · Lagarto       |
| Lagarto | Spock   · Papel         |
| Spock   | Tesoura · Pedra         |

O cálculo de vencedor é feito:
  
1. Agrupar jogadores por tipo de jogada
2. Para cada jogada possível (como ‘pedra’), o sistema verifica quais jogadas ela vence e conta quantos jogadores escolheram essas jogadas na rodada. A soma desses jogadores representa a pontuação daquela jogada.
3. Atribuir pontos individuais a cada jogador
4. Determinar o(s) vencedor(es)

---

> Desenvolvido por Leonardo como parte do desafio **JOKENPO - DEV**.  
>>>>>>> 3b132a0 (feat: exibe situação da rodada)
