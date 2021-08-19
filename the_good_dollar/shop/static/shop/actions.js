// // Filter data
// function filterData(data) {
//     // const filterUrl = 'filter-products'
//     const filterEls = document.querySelectorAll('.form-check-input');

//     filterEls.forEach(filterEl => {
//         filterEl.addEventListener('change', () => {

//             if (filterEl.checked) {
//                 data.push(filterEl.id)
//             } else {
//                 removeArr(data, filterEl.id)
//             }

//             // $.ajax({
//             //     type: 'GET',
//             //     url: filterUrl,
//             //     data: {
//             //         'filters-data': JSON.stringify(data),
//             //     },
//             //     success: function (response) {
//             //         console.log(response.data);
//             //     }
//             // })
//         })
//     });
// }
// // setTimeout(() => {
// //     filterData();
// // }, 2700);


function filterData() {
    filtersData = [];

    const filterEls = document.querySelectorAll('.form-check-input');

    filterEls.forEach(filterEl => {
        filterEl.addEventListener('change', () => {
            productsContainer.innerHTML = ""
            if (filterEl.checked) {
                filtersData.push(filterEl.id)
                console.log(filtersData)
            } else {
                removeArr(filtersData, filterEl.id)
            }
            getData(filtersData)
        })
    });
}

setTimeout(() => {
    filterData();
}, 2700);