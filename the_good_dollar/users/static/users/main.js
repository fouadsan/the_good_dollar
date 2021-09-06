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
					data: respData.total_orders,
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

function addAddrBook() {

	const createAddrForm = document.getElementById('create-addr-form');
	const addAddrBtn = document.getElementById('create-addr-btn');

	const addressEl = document.getElementById('id_address');
	const mobileEl = document.getElementById('id_mobile');
	const statusEl = document.getElementById('id_status');


	createAddrForm.addEventListener('submit', e => {
		e.preventDefault()

		$.ajax({
			type: 'POST',
			url: '',
			data: {
				'csrfmiddlewaretoken': csrf[0].value,
				'address': addressEl.value,
				'mobile': mobileEl.value,
				'status': statusEl.checked ? true : false,
			},

			success: function (response) {
				console.log(response)
				// data = response.data

				// const reviewRatEl = document.createElement('cite');
				// for (i = 0; i < data.review_rating; i++) {
				// 	reviewRatEl.innerHTML += `
				//         <i class="fa fa-star text-warning"></i>
				//     `
				// }
				// addFirstRevEl.style.display = "none";
				// reviewCardEl.insertAdjacentHTML('afterbegin', `
				//     <div class="card-body review-list" style="max-height: 400px; overflow: auto;">
				//             <blockquote class="blockquote text-right">
				//                 <small>${data.review_text}</small>
				//                 <footer class="blockquote-footer">${data.user}
				//                     ${reviewRatEl.outerHTML}
				//                 </footer>
				//             </blockquote>
				//             <hr>
				//     </div>
				// `);
				// addReviewBtn.style.display = "none";
				// $('#review-modal').modal('hide');
				// // handleModalAlerts('success', 'New Object added!');
			},
			error: function () {
				console.log('oops, something went wrong');
				// handleModalAlerts('danger', 'oops...something went wrong')
			}
		})
	})
}

// ShowOrdersChart()

addAddrBook();