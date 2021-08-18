// Filter data
function filterData() {
    const filterUrl = 'filter-products'
    const filterEls = document.querySelectorAll('.form-check-input');
    data = [];
    filterEls.forEach( filterEl => {
        filterEl.addEventListener('change', () => {

            if (filterEl.checked) {
                data.push(filterEl.id)
            } else {
                removeArr(data, filterEl.id)
            }
            console.log(data)
            $.ajax({
                type: 'GET',
                url: filterUrl,
                data: {
                    'data': JSON.stringify(data),
                },
                success: function (response) {
                    console.log(response.data);
                }
            })
        })
    });
}
setTimeout(() => {
    filterData();
}, 2700);
