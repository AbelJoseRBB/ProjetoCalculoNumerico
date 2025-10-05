const form = document.getElementById("calcForm");
const metodoSelect = document.getElementById("metodo");
const parametrosDiv = document.getElementById("parametros");
const resultadoTexto = document.getElementById("resultadoTexto");

const ctxIter = document.getElementById("iterationsChart");
const ctxTime = document.getElementById("timeChart");

let chartIter, chartTime;

const ordemMetodos = ["Bissec", "FalsaPos", "NewtonRaphson", "Secante"];
const cores = {
  Bissec: "#ff5252",          // vermelho
  FalsaPos: "#4caf50",        // verde
  NewtonRaphson: "#ffeb3b",   // amarelo
  Secante: "#2196f3"          // azul
};

// =============================
// 🔹 Atualiza parâmetros conforme método
// =============================
function atualizarParametros() {
  const metodo = metodoSelect.value;
  parametrosDiv.innerHTML = "";

  if (metodo === "Bissec" || metodo === "FalsaPos") {
    parametrosDiv.innerHTML = `
      <label>Intervalo A:</label>
      <input type="number" step="any" id="a" required>
      <label>Intervalo B:</label>
      <input type="number" step="any" id="b" required>
    `;
  } else if (metodo === "NewtonRaphson") {
    parametrosDiv.innerHTML = `
      <label>x0 (chute inicial):</label>
      <input type="number" step="any" id="x0" required>
    `;
  } else if (metodo === "Secante") {
    parametrosDiv.innerHTML = `
      <label>x0:</label>
      <input type="number" step="any" id="x0" required>
      <label>x1:</label>
      <input type="number" step="any" id="x1" required>
    `;
  }
}
metodoSelect.addEventListener("change", atualizarParametros);
atualizarParametros();

// =============================
// 🔹 Cria os gráficos vazios no carregamento
// =============================
document.addEventListener("DOMContentLoaded", () => {
  criarGraficos();
});

// =============================
// 🔹 Envia os dados ao backend
// =============================
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const funcao = document.getElementById("funcao").value;
  const metodo = metodoSelect.value;

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
    const res = await fetch("http://127.0.0.1:5000/resolver", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Erro ao se comunicar com o servidor Flask.");

    const resultado = await res.json();

    resultadoTexto.innerHTML = `
      <p><strong>Método:</strong> ${resultado.metodo}</p>
      <p><strong>Raiz encontrada:</strong> ${resultado.raiz.toFixed(6)}</p>
      <p><strong>Iterações:</strong> ${resultado.iteracoes}</p>
      <p><strong>Tempo:</strong> ${(resultado.tempo * 1000).toFixed(3)} ms</p>
    `;

    atualizarGraficos(resultado);
  } catch (error) {
    console.error(error);
    resultadoTexto.innerHTML = `<p style="color:red;">Erro: não foi possível se conectar ao backend.</p>`;
  }
});

// =============================
// 🔹 Criação inicial dos gráficos (formato padrão)
// =============================
function criarGraficos() {
  if (chartIter) chartIter.destroy();
  if (chartTime) chartTime.destroy();

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

  chartIter = new Chart(ctxIter, {
    type: "bar",
    data: {
      labels: ordemMetodos,
      datasets: [{
        label: "Iterações",
        data: [null, null, null, null], // mantém formato visual limpo
        backgroundColor: ordemMetodos.map(m => cores[m])
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Número de Iterações", color: "white" },
          ticks: { color: "white", precision: 0 }
        },
        x: { ticks: { color: "white" } }
      },
      plugins: { legend: legendaSemCor }
    }
  });

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
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Tempo de Execução (ms)", color: "white" },
          ticks: { color: "white" }
        },
        x: { ticks: { color: "white" } }
      },
      plugins: { legend: legendaSemCor }
    }
  });
}

// =============================
// 🔹 Atualiza gráficos com novos resultados
// =============================
function atualizarGraficos(resultado) {
  const idx = ordemMetodos.indexOf(resultado.metodo);

  // garante que os gráficos existam
  if (!chartIter || !chartTime) criarGraficos();

  chartIter.data.datasets[0].data[idx] = resultado.iteracoes;
  chartIter.update();

  chartTime.data.datasets[0].data[idx] = resultado.tempo * 1000; // s -> ms
  chartTime.update();
}
