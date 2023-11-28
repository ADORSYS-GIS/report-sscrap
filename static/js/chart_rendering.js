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

// Passing image data to script
const imageData = urlParams.getAll('images');
const imageList = document.getElementById('imageList');
imageData.forEach(image => {
    const li = document.createElement('li');
    li.textContent = image;
    imageList.appendChild(li);
});
