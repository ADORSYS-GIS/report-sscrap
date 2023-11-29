// Rendering analyst results to charts

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
              label: 'Number of Text',
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
                  beginAtZero: true,
                  title: {
                      display: true,
                      text: 'Number of Text'
                  }
              },
              x: {
                  title: {
                      display: true,
                      text: 'Websites URL Number'
                  }
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
              label: 'Number of Images',
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
                  beginAtZero: true,
                  title: {
                      display: true,
                      text: 'Number of Images'
                  }
              },
              x: {
                  title: {
                      display: true,
                      text: 'Websites URL Number'
                  }
              }
          }
      }
  });

  // Display text_data and image_data in .details divs
  var textDetails = document.querySelector('.textchart-details .details');
  var imageDetails = document.querySelector('.imagechart-details .details');

  var textDataHtml = '';
  for (var i = 0; i < texts.length; i++) {
      textDataHtml += 'Website ' + labels[i] + ': ' + texts[i] + ' text<br>';
  }
  
  textDetails.innerHTML = textDataHtml;

  var imageDataHtml = '';
  for (var i = 0; i < images.length; i++) {
      imageDataHtml += 'Website '+ labels[i] + ': ' + images[i] + ' images<br>';
  }
  imageDetails.innerHTML = imageDataHtml;
}