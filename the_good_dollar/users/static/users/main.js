rootUrl = window.location.origin

const chartSpinnerBox = document.getElementById('chart-spinner-box');

function ShowOrdersChart() {
	const chartDataUrl = `${rootUrl}\/users\/orders_data`

	$.ajax({
        type: 'GET',
        url: chartDataUrl,
        success: function (response) {
			respData = response.data
            console.log(response)
			const labels = respData.month_number;
				const data = {
					labels: labels,
					datasets: [{
						label: 'Orders By Month',
						backgroundColor: 'rgb(255, 99, 132)',
						borderColor: 'rgb(255, 99, 132)',
						data: respData.total_orders ,
					}]
				};
				const config = {
					type: 'bar',
					data,
					options: {}
					};
			setTimeout(() => {
				chartSpinnerBox.classList.add('not-visible');		
				var myChart = new Chart(
					document.getElementById('myChart'),
					config
				);

			}, 5000);
			
		}
		})

    
}

ShowOrdersChart()

function renderChart() {
	
}