// Pega referências dos elementos principais do HTML
const form = document.getElementById("calcForm");
const metodoSelect = document.getElementById("metodo");
const parametrosDiv = document.getElementById("parametros");
const resultadoTexto = document.getElementById("resultadoTexto");

// Canvas dos dois gráficos
const ctxIter = document.getElementById("iterationsChart");
const ctxTime = document.getElementById("timeChart");

// Variáveis globais para guardar os gráficos 
let chartIter, chartTime;

// Ordem fixa dos métodos e cores associadas a cada um
const ordemMetodos = ["Bissec", "FalsaPos", "NewtonRaphson", "Secante"];
const cores = {
  Bissec: "#ff5252",          // vermelho
  FalsaPos: "#4caf50",        // verde
  NewtonRaphson: "#ffeb3b",   // amarelo
  Secante: "#2196f3"          // azul
};


// Atualiza parâmetros conforme método
function atualizarParametros() {
  const metodo = metodoSelect.value;
  parametrosDiv.innerHTML = ""; // limpa os campos anteriores

  // Para métodos que precisam de intervalo [a, b]
  if (metodo === "Bissec" || metodo === "FalsaPos") {
    parametrosDiv.innerHTML = `
      <label>Intervalo A:</label>
      <input type="number" step="any" id="a" required>
      <label>Intervalo B:</label>
      <input type="number" step="any" id="b" required>
    `;
  } 
  // Newton-Raphson: só precisa de um chute inicial
  else if (metodo === "NewtonRaphson") {
    parametrosDiv.innerHTML = `
      <label>x0 (chute inicial):</label>
      <input type="number" step="any" id="x0" required>
    `;
  } 
  // Secante: precisa de dois chutes iniciais
  else if (metodo === "Secante") {
    parametrosDiv.innerHTML = `
      <label>x0:</label>
      <input type="number" step="any" id="x0" required>
      <label>x1:</label>
      <input type="number" step="any" id="x1" required>
    `;
  }
}

// Atualiza os campos quando o método muda
metodoSelect.addEventListener("change", atualizarParametros);
// E chama uma vez no início pra aparecer os campos certos
atualizarParametros();


// Cria os gráficos vazios no carregamento
document.addEventListener("DOMContentLoaded", () => {
  criarGraficos();
});

// Envia os dados ao backend Flask
form.addEventListener("submit", async (e) => {
  e.preventDefault(); // impede o recarregamento da página

  // Pega os valores informados no formulário
  const funcao = document.getElementById("funcao").value;
  const metodo = metodoSelect.value;

  // Monta o JSON com os parâmetros adequados
  let payload = { funcao, metodo };
  if (metodo === "Bissec" || metodo === "FalsaPos") {
    payload.a = parseFloat(document.getElementById("a").value);
    payload.b = parseFloat(document.getElementById("b").value);
  } else if (metodo === "NewtonRaphson") {
    payload.x0 = parseFloat(document.getElementById("x0").value);
  } else if (metodo === "Secante") {
    payload.x0 = parseFloat(document.getElementById("x0").value);
    payload.x1 = parseFloat(document.getElementById("x1").value);
  }

  try {
    // Envia a requisição POST para o servidor Flask
    const res = await fetch("http://127.0.0.1:5000/resolver", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    // Caso ocorra erro de comunicação
    if (!res.ok) throw new Error("Erro ao se comunicar com o servidor Flask.");

    // Recebe o resultado do backend
    const resultado = await res.json();

    // Exibe os resultados numéricos abaixo do formulário
    resultadoTexto.innerHTML = `
      <p><strong>Método:</strong> ${resultado.metodo}</p>
      <p><strong>Raiz encontrada:</strong> ${resultado.raiz.toFixed(6)}</p>
      <p><strong>Iterações:</strong> ${resultado.iteracoes}</p>
      <p><strong>Tempo:</strong> ${(resultado.tempo * 1000).toFixed(3)} ms</p>
    `;

    // Atualiza os gráficos com os novos valores
    atualizarGraficos(resultado);
  } catch (error) {
    // Caso o Flask não esteja rodando, mostra erro na tela
    console.error(error);
    resultadoTexto.innerHTML = `<p style="color:red;">Erro: não foi possível se conectar ao backend.</p>`;
  }
});


// Criação inicial dos gráficos (com valores visíveis)
Chart.register(ChartDataLabels); // ativa o plugin de labels

function criarGraficos() {
  // Remove gráficos antigos se já existirem (evita sobreposição)
  if (chartIter) chartIter.destroy();
  if (chartTime) chartTime.destroy();

  // Remove legenda colorida padrão (apenas texto branco)
  const legendaSemCor = {
    labels: {
      color: "white",
      generateLabels: (chart) => {
        const dataset = chart.data.datasets[0];
        return [{
          text: dataset.label,
          fillStyle: "transparent",
          strokeStyle: "transparent",
          hidden: false
        }];
      }
    }
  };

  // ---------- Gráfico de Iterações ----------
  chartIter = new Chart(ctxIter, {
    type: "bar", // tipo de gráfico: barras
    data: {
      labels: ordemMetodos, // nomes dos métodos
      datasets: [{
        label: "Iterações",
        data: [null, null, null, null], // começa vazio
        backgroundColor: ordemMetodos.map(m => cores[m]) // cores por método
      }]
    },
    options: {
      plugins: {
        legend: legendaSemCor,
        datalabels: {
          color: "white", // texto branco acima das barras
          anchor: "end",
          align: "top",
          font: { weight: "bold" },
          formatter: (value) => (value ? Math.round(value) : "")
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Número de Iterações", color: "white" },
          ticks: { color: "white", precision: 0 }
        },
        x: { ticks: { color: "white" } }
      }
    },
    plugins: [ChartDataLabels]
  });

  // ---------- Gráfico de Tempo ----------
  chartTime = new Chart(ctxTime, {
    type: "bar",
    data: {
      labels: ordemMetodos,
      datasets: [{
        label: "Tempo (ms)",
        data: [null, null, null, null],
        backgroundColor: ordemMetodos.map(m => cores[m])
      }]
    },
    options: {
      plugins: {
        legend: legendaSemCor,
        datalabels: {
          color: "white",
          anchor: "end",
          align: "top",
          font: { weight: "bold" },
          formatter: (value) => (value ? value.toFixed(2) : "")
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Tempo de Execução (ms)", color: "white" },
          ticks: { color: "white" }
        },
        x: { ticks: { color: "white" } }
      }
    },
    plugins: [ChartDataLabels]
  });
}

// Atualiza gráficos com os novos dados
function atualizarGraficos(resultado) {

  // Encontra o índice do método no array ordemMetodos
  const idx = ordemMetodos.indexOf(resultado.metodo);

  // Se os gráficos ainda não existem, recria
  if (!chartIter || !chartTime) criarGraficos();

  // Atualiza o valor de iterações do método correspondente
  chartIter.data.datasets[0].data[idx] = resultado.iteracoes;
  chartIter.update();

  // Atualiza o valor de tempo (converte segundos → milissegundos)
  chartTime.data.datasets[0].data[idx] = resultado.tempo * 1000;
  chartTime.update();
}
