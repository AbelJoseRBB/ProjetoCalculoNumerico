const form = document.getElementById("calcForm");
const metodoSelect = document.getElementById("metodo");
const parametrosDiv = document.getElementById("parametros");
const resultadoTexto = document.getElementById("resultadoTexto");
const ctx = document.getElementById("efficiencyChart");

let chart;

// ordem fixa
const ordemMetodos = ["Bissec", "FalsaPos", "NewtonRaphson", "Secante"];
const cores = {
  Bissec: "red",
  FalsaPos: "green",
  NewtonRaphson: "yellow",
  Secante: "blue"
};

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

  const res = await fetch("http://127.0.0.1:5000/resolver", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  const resultado = await res.json();

  // mostra raiz em texto
  resultadoTexto.innerHTML = `
    <p><strong>Método:</strong> ${resultado.metodo}</p>
    <p><strong>Raiz encontrada:</strong> ${resultado.raiz.toFixed(6)}</p>
  `;

  atualizarGrafico(resultado);
});

function atualizarGrafico(resultado) {
  const metodo = resultado.metodo;
  const idx = ordemMetodos.indexOf(metodo);

  if (!chart) {
    chart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: ordemMetodos,
        datasets: [
          {
            label: "Iterações",
            data: Array(ordemMetodos.length).fill(0),
            backgroundColor: ordemMetodos.map(m => cores[m])
          },
          {
            label: "Tempo (s)",
            data: Array(ordemMetodos.length).fill(0),
            backgroundColor: ordemMetodos.map(m => cores[m]),
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true, ticks: { color: "white" } },
          x: { ticks: { color: "white" } }
        },
        plugins: {
          legend: { labels: { color: "white" } }
        }
      }
    });
  }

  chart.data.datasets[0].data[idx] = resultado.iteracoes;
  chart.data.datasets[1].data[idx] = resultado.tempo;
  chart.update();
}
