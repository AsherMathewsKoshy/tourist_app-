document.addEventListener('DOMContentLoaded', function() {
    loadCountries();  // Load countries on page load
});

function loadCountries() {
    fetch('https://countriesnow.space/api/v0.1/countries')
        .then(response => response.json())
        .then(data => {
            const countrySelect = document.getElementById('country');
            data.data.forEach(country => {
                let option = document.createElement('option');
                option.value = country.country;
                option.text = country.country;
                countrySelect.add(option);
            });
        })
        .catch(error => console.error('Error loading countries:', error));
}

function loadStates() {
    const country = document.getElementById('country').value;
    if (!country) return;

    fetch('https://countriesnow.space/api/v0.1/countries/states', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ country })
    })
    .then(response => response.json())
    .then(data => {
        const stateSelect = document.getElementById('state');
        stateSelect.innerHTML = '<option value="">Select State</option>';  // Reset states
        document.getElementById('district').innerHTML = '<option value="">Select District</option>'; // Reset districts

        data.data.states.forEach(state => {
            let option = document.createElement('option');
            option.value = state.name;
            option.text = state.name;
            stateSelect.add(option);
        });
    })
    .catch(error => console.error('Error loading states:', error));
}

function loadDistricts() {
    const country = document.getElementById('country').value;
    const state = document.getElementById('state').value;
    if (!state) return;

    fetch('https://countriesnow.space/api/v0.1/countries/state/cities', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ country, state })
    })
    .then(response => response.json())
    .then(data => {
        const districtSelect = document.getElementById('district');
        districtSelect.innerHTML = '<option value="">Select District</option>';  // Reset districts
        data.data.forEach(district => {
            let option = document.createElement('option');
            option.value = district;
            option.text = district;
            districtSelect.add(option);
        });
    })
    .catch(error => console.error('Error loading districts:', error));
}
