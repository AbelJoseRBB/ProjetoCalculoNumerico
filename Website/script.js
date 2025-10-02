(async function(){
  const ctx = document.getElementById('efficiencyChart').getContext('2d');

  function drawChart(labels, values){
    if (window._effChart) window._effChart.destroy();

    window._effChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Tempo de execução (ms)',
          data: values,
          backgroundColor: [
            'rgba(79,195,247,0.8)',
            'rgba(129,199,132,0.8)',
            'rgba(255,202,40,0.8)',
            'rgba(239,83,80,0.8)'
          ],
          borderColor: [
            'rgba(79,195,247,1)',
            'rgba(129,199,132,1)',
            'rgba(255,202,40,1)',
            'rgba(239,83,80,1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: { mode: 'index', intersect: false }
        },
        scales: {
          x: {
            ticks: { color: '#9aa3b2' },
            grid: { color: 'rgba(255,255,255,0.03)' }
          },
          y: {
            ticks: { color: '#9aa3b2' },
            grid: { color: 'rgba(255,255,255,0.03)' },
            beginAtZero: true,
            title: {
              display: true,
              text: 'Tempo (ms)',
              color: '#cfeaf8'
            }
          }
        }
      }
    });
  }

  try {
    const resp = await fetch('resultado.json', {cache: "no-store"});
    if (!resp.ok) throw new Error('Arquivo não encontrado');
    const data = await resp.json();

    // Formato esperado: objeto com tempos de cada método
    // Exemplo:
    // {
    //   "Bissecção": 12.4,
    //   "Falsa Posição": 10.8,
    //   "Newton-Raphson": 6.2,
    //   "Secante": 7.1
    // }

    const labels = Object.keys(data);
    const valores = Object.values(data);

    drawChart(labels, valores);
  } catch (err) {
    console.warn('Não foi possível carregar resultado.json — usando dados de exemplo.', err);

    // Dados de exemplo
    const labels = ["Bissecção", "Falsa Posição", "Newton-Raphson", "Secante"];
    const valores = [12.4, 10.8, 6.2, 7.1];

    drawChart(labels, valores);
  }
})();
