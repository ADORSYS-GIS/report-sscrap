// chart_rendering.js

function renderChart(jsonData) {
  // Use the jsonData object to render the charts

  // Get the canvas elements for the two charts
  var textChartCanvas = document.getElementById('text-chart');
  var imageChartCanvas = document.getElementById('image-chart');

  // Extract data from jsonData
  var labels = jsonData.labels;
  var texts = jsonData.texts;
  var images = jsonData.images;

  // Render the text chart using Chart.js
  var textChart = new Chart(textChartCanvas, {
      type: 'bar',
      data: {
          labels: labels,
          datasets: [{
              label: 'Text Data',
              data: texts,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });

  // Render the image chart using Chart.js
  var imageChart = new Chart(imageChartCanvas, {
      type: 'bar',
      data: {
          labels: labels,
          datasets: [{
              label: 'Image Data',
              data: images,
              backgroundColor: 'rgba(192, 75, 192, 0.2)',
              borderColor: 'rgba(192, 75, 192, 1)',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}
