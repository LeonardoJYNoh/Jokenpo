const apiBaseUrl = "http://localhost:5000"; 

function mostrarResultado(dados) {
  const resultadoElemento = document.getElementById("resultado");

  if (dados.erro) {
    resultadoElemento.innerText = `ERRO: ${dados.erro.toUpperCase()}`;
    resultadoElemento.style.color = "red";
    resultadoElemento.style.fontWeight = "bold";
  } 
  else if (dados.vencedores) {
    const vencedoresStr = dados.vencedores.join(", ");
    resultadoElemento.innerText = `Vencedores: ${vencedoresStr}`;
    resultadoElemento.style.color = "green";
    resultadoElemento.style.fontWeight = "bold";
  }
  else if (dados.mensagem) {
    resultadoElemento.innerText = dados.mensagem;
    resultadoElemento.style.color = "black";
    resultadoElemento.style.fontWeight = "normal";
  }
  else if (dados.jogaram && dados.osciosos) {
    const jogaramStr = dados.jogaram.map(nome => `${nome} já jogou`).join(", ");
    const osciososStr = dados.osciosos.map(nome => `${nome} precisa jogar`).join(", ");
    resultadoElemento.innerText = `${jogaramStr}${jogaramStr && osciososStr ? ", " : ""}${osciososStr}`;
    resultadoElemento.style.color = "black";
    resultadoElemento.style.fontWeight = "normal";
  }
  else {
    resultadoElemento.innerText = JSON.stringify(dados, null, 2);
    resultadoElemento.style.color = "black";
    resultadoElemento.style.fontWeight = "normal";
  }
}
function cadastrarJogador() {
  const jogadorId = parseInt(document.getElementById("id").value);
  const nomeJogador = document.getElementById("nome").value;

  fetch(`${apiBaseUrl}/jogador`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      id: jogadorId, 
      nome: nomeJogador 
    })
  })
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro ao cadastrar:', error));
}

function removerJogador() {
  const jogadorId = parseInt(document.getElementById("id-remover").value);

  fetch(`${apiBaseUrl}/jogador/${jogadorId}`, {
    method: "DELETE"
  })
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro ao remover:', error));
}

function fazerJogada() {
  const jogadorId = parseInt(document.getElementById("id-jogada").value);
  const jogada = document.getElementById("jogada").value;

  fetch(`${apiBaseUrl}/jogada`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      id: jogadorId, 
      jogada: jogada 
    })
  })
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro na jogada:', error));
}

function verRodadaAtual() {
  fetch(`${apiBaseUrl}/rodada`)
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro ao consultar:', error));
}

function encerrarRodada() {
  fetch(`${apiBaseUrl}/rodada/finalizar`, { 
    method: "POST" 
  })
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro ao finalizar:', error));
}

function reiniciarRodada() {
  fetch(`${apiBaseUrl}/rodada/reset`, { 
    method: "POST" 
  })
  .then(response => response.json())
  .then(data => mostrarResultado(data))
  .catch(error => console.error('Erro ao resetar:', error));
}