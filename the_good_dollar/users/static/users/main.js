
const userDashUrl = rootUrl + '/users/dashboard/';
const addrBookUrl = rootUrl + '/users/addressbook/';

const chartSpinnerBox = document.getElementById('chart-spinner-box');

let upId;

function ShowOrdersChart() {
	const chartDataUrl = `${rootUrl}\/users\/orders_data`

	$.ajax({
		type: 'GET',
		url: chartDataUrl,
		success: function (response) {
			respData = response.data

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

			}, 2500);

		}
	})


}

function addAddr() {
	
	const addrBookWrapper = document.querySelector('.addrbook__wrapper');
	const createAddrForm = document.getElementById('create-addr-form');

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
				'status': statusEl.checked ? true : false
			},

			success: function (response) {
				console.log(response)
				data = response.data
				
				const activatedAddrCardEl = document.querySelector('.shadow');
				const CardParentEl = document.createElement('div');
				CardParentEl.classList.add('col-md-4');
				const newAddrCard = document.createElement('div');
				newAddrCard.id = `addr-${data.id}`;
				if (data.status) {
					newAddrCard.classList.add('card', 'mb-3', 'border-secondary', 'shadow');
						if (activatedAddrCardEl) {
							deactivateAddrCardEl(activatedAddrCardEl);
						}
						
						
					newAddrCard.innerHTML= `
						<div class="card-body">
							<p class="card-text">${data.address}</p>
							<p class="card-text">${data.mobile}</p>
						</div>
						<div class="card-footer">
							<i class="fa fa-check-circle fa-2x text-success addr__checkmark" id="check-${data.id}"></i>
							<button id="${data.id}" class="btn btn-sm btn-outline-danger" style="display:none;" activate__btn>Activate</button>
							<button type="button" id="edit-${data.id}" class="btn edit__addr" data-bs-toggle="modal" data-bs-target="#update-addr-modal"><i class="fa fa-pen"></i></button>
						</div>
					`
				} else {
					newAddrCard.classList.add('card', 'mb-3');
					newAddrCard.innerHTML= `
						<div class="card-body">
							<p class="card-text">${data.address}</p>
							<p class="card-text">${data.mobile}</p>
						</div>
						<div class="card-footer">
							<i class="fa fa-check-circle fa-2x text-success addr__checkmark" id="check-${data.id}" style="display:none;"></i>
							<button id="${data.id}" class="btn btn-sm btn-outline-danger" activate__btn>Activate</button>
							<button type="button" id="edit-${data.id}" class="btn edit__addr" data-bs-toggle="modal" data-bs-target="#update-addr-modal"><i class="fa fa-pen"></i></button>
						</div>
					`
					CardParentEl.appendChild(newAddrCard);
					addrBookWrapper.insertBefore(CardParentEl, addrBookWrapper.firstChild);
				}
				$('#create-addr-modal').modal('hide');
				createAddrForm.reset();
				// handleModalAlerts('success', 'New Object added!');
			},
			error: function () {
				console.log('oops, something went wrong');
				// handleModalAlerts('danger', 'oops...something went wrong')
			}
		})
	})
}

function deactivateAddrCardEl(activatedAddrCardEl) {
	activatedAddrCardEl.classList.remove('border-secondary', 'shadow');
	const addrCheckMark = activatedAddrCardEl.querySelector('i');
	const addrActivatedBtn = activatedAddrCardEl.querySelector('button');
	const addrActivatedDelBtn = activatedAddrCardEl.querySelector('.del__addr');
	addrCheckMark.style.display = 'none';
	addrActivatedBtn.style.display = 'inline-block';
	addrActivatedDelBtn.style.display = 'inline-block';
} 

function activateAddr() {
	const activateAddrUrl = "activate_address";
	const activateAddrBtns = document.querySelectorAll('.activate__btn');
	activateAddrBtns.forEach(activateBtn => {
		const _addrId = activateBtn.id;
		activateBtn.addEventListener('click', () => {
			$.ajax({
				type: 'GET',
				url: activateAddrUrl,
				data: {
					'id': _addrId,
				},
				dataType:'json',
				success: function (response) {
					console.log(response);
					if(response.bool==true) {

						const activatedAddrCardEl = document.querySelector('.shadow');
						const newActivatedAddrCardEl = document.getElementById(`addr-${_addrId}`);
						const addrCheckMark = document.getElementById(`check-${_addrId}`);
						const delAddrBtn = activateBtn.nextElementSibling;

						deactivateAddrCardEl(activatedAddrCardEl);
						
						newActivatedAddrCardEl.classList.add('border-secondary', 'shadow');
						activateBtn.style.display = "none";
						delAddrBtn.style.display = "none";
						addrCheckMark.style.display = "inline-block";
					}
					
				},
				error: function () {
					console.log('something went wrong !!!');
				}
			})
		})
	});
}

function delAddr() {
	const deleteAddrForm = document.getElementById('delete-addr-form');
	const delAddrBtns = document.querySelectorAll('.del__addr');
	let addrId;
	delAddrBtns.forEach(delBtn => {
		delBtn.addEventListener('click', () => {
			addrId = delBtn.id.slice(4);
		});

		deleteAddrForm.addEventListener('submit', function(e) {
			e.preventDefault();

			$.ajax({
				type: 'POST',
				url: deleteUrl + addrId,
				data: {
					'csrfmiddlewaretoken': csrf[0].value,
				},
				success: function (response) {
					console.log(response.msg);
				},
				error: function (error) {
					// handleAlerts('center', 'Error!', 'Oops...something went wrong', 'error', true)
				}
			});
		})
	});
}

function getAddrData(addressInput, mobileInput) {
	const addrDataBaseUrl = 'addr_data/';

	const editAddrBtns = document.querySelectorAll('.edit__addr');
	editAddrBtns.forEach(editBtn => {
	
		editBtn.addEventListener('click', () => {

			upId = editBtn.id.slice(5);
			
			$.ajax({
				type: 'GET',
				url: addrDataBaseUrl + upId,
				success: function (response) {
					const data = response.data;
					addressInput.value = data.address;
					mobileInput.value = data.mobile;					
				},
				error: function (error) {
					console.log(error)
				}
			})
		})
		
	});
}

function updateAddr(addressInput, mobileInput) {
	const updateAddrBaseUrl = "update_address/";
	const updateAddrForm = document.getElementById('update-addr-form');

	updateAddrForm.addEventListener('submit', e => {
		e.preventDefault();

		const addrCardEl = document.getElementById('addr-' + upId);
		const addressEl = addrCardEl.firstElementChild.firstElementChild;
		const mobileEl = addrCardEl.firstElementChild.lastElementChild;

		$.ajax({
			type: 'POST',
			url: updateAddrBaseUrl + upId,
			data: {
				'csrfmiddlewaretoken': csrf[0].value,
				'address': addressInput.value,
				'mobile': mobileInput.value,

			},
			success: function (response) {
				const data = response.data;
				console.log(data)
				addressEl.textContent = data.address;
				mobileEl.textContent = data.mobile;

				$('#update-addr-modal').modal('hide');	
			},
			error: function (error) {
				console.log(error)
			}
		})

	})
}

function handleAddrBook() {
	const addressInput = document.getElementById('id_updateAddress');
	const mobileInput = document.getElementById('id_updateMobile');
	const statusInput = document.getElementById('id_updateStatus');
	addAddr();
	activateAddr();
	delAddr();
	getAddrData(addressInput, mobileInput, statusInput);
	updateAddr(addressInput, mobileInput, statusInput);
}




if (currentUrl == userDashUrl) {
	ShowOrdersChart()
} else {
	handleAddrBook();
}

