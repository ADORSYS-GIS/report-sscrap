// Retrieving chart data from query parameters
const urlParams = new URLSearchParams(window.location.search);
console.log(window.location.search);
const labels = JSON.parse(decodeURIComponent(urlParams.get('labels')));
console.log(labels);
const text_data = JSON.parse(urlParams.get('text_data'));
console.log(text_data)
const no_images = JSON.parse(urlParams.get('no_images'));
console.log(no_images)
const images = JSON.parse(urlParams.get('images'));
console.log(images);

// Creating the chart for total number of characters
const ctx = document.getElementById('Total_number_of_characters').getContext('2d');
const chart1 = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: labels,
    datasets: [{
      label: 'Number of Text',
      data: text_data,
      backgroundColor: 'rgba(255, 255, 255, 1)',
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

// Creating the chart for images found
const ctxn = document.getElementById('Total_number_of_images').getContext('2d');
const chart2 = new Chart(ctxn, {
  type: 'bar',
  data: {
    labels: labels,
    datasets: [{
      label: 'Number of Images',
      data: no_images,
      backgroundColor: 'rgba(255, 255, 255, 1)',
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