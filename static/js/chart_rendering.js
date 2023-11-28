// Load the data from the CSV file
fetch('data.csv')
.then(response => response.text())
.then(csv => {
    // Parse the CSV data
    const data = Papa.parse(csv, { header: true }).data;
    
    // Extract the required columns from the data
    const ID = data.map((column, index) => `Website ${index + 1}`);
    const total_characters = data.map(column => column.total_characters);
    const images_found = data.map(column => column.images_found)
    
    // Create the chart
    const ctx = document.getElementById('Total_number_of_characters').getContext('2d');
    const tes = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ID,
            datasets: [{
                label: 'Total Characters On Each Website',
                data: total_characters,
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
    const characters = tes.data.datasets[0].data;
    console.log(characters)
    const ctxn = document.getElementById('Total_number_of_images').getContext('2d');
    new Chart(ctxn, {
        type: 'bar',
        data: {
            labels: ID,
            datasets: [{
                label: 'Images Found On Each Website',
                data: images_found,
                backgroundColor: 'rgba(100, 100, 100, 1)',
                borderColor: 'rgba(100, 100, 100, 1)',
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
    
});