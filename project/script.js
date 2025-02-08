const banks = [
    { name: "Bank A" },
    { name: "Bank B" },
    { name: "Bank C" },
    { name: "Bank D" },
    { name: "Bank E" },
    { name: "Bank F" },
    { name: "Bank G" },
    { name: "Bank H" },
    { name: "Bank I" },
    { name: "Bank J" }
];

const baseRatesUSD = {};
const baseRatesEUR = {};


function generateRandomRates() {
    for (let day = 1; day <= 900; day += 20) {
        baseRatesUSD[day] = Array.from({ length: 10 }, () => (Math.random() * 4 + 1).toFixed(2));
        baseRatesEUR[day] = Array.from({ length: 10 }, () => (Math.random() * 4 + 1).toFixed(2));
    }
}


function getRatesForDay(currency, days) {
    const baseRates = currency === 'usd' ? baseRatesUSD : baseRatesEUR;
    let closestDay = Object.keys(baseRates).reduce((prev, curr) => {
        return (Math.abs(curr - days) < Math.abs(prev - days) ? curr : prev);
    });
    return baseRates[closestDay];
}


function adjustRatesForAmount(rates, amount) {
    return rates.map(rate => {
        let adjustment = (amount / 5000) * 0.1;
        return (parseFloat(rate) + adjustment).toFixed(2);
    });
}

function calculateInterest() {
    const currency = document.getElementById('currency').value;
    const amount = parseInt(document.getElementById('amount').value);
    const days = parseInt(document.getElementById('days').value);
    const resultTable = document.getElementById('resultTable');
    const resultsSection = document.getElementById('resultsSection');
    resultTable.innerHTML = ''; 

    if (!amount || amount <= 0 || !days || days <= 0 || days > 900) {
        alert('Please enter valid amount and days (1-900)');
        return;
    }

    resultsSection.style.display = 'block';

    const baseRates = getRatesForDay(currency, days);
    const rates = adjustRatesForAmount(baseRates, amount);

    const table = document.createElement('table');
    table.className = 'table';
    const headerRow = document.createElement('tr');
    headerRow.innerHTML = '<th>Bank Name</th><th>Interest Rate (%)</th><th>Interest Amount</th><th>Total Amount</th>';
    table.appendChild(headerRow);

    banks.forEach((bank, index) => {
        const rate = rates[index];
        const interest = (amount * rate / 100 * (days / 365)).toFixed(2);
        const totalAmount = (parseFloat(amount) + parseFloat(interest)).toFixed(2);
        const row = document.createElement('tr');
        row.innerHTML = `<td>${bank.name}</td><td>${rate}</td><td>${interest}</td><td>${totalAmount}</td>`;
        table.appendChild(row);
    });

    resultTable.appendChild(table);
}


document.addEventListener('DOMContentLoaded', () => {
    generateRandomRates();
});
