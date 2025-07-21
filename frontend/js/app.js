const BASE_URL = "http://localhost:5477/blackrock/challenge/v1/transactions";

let transactions = [];

// Mostrar la lista de transacciones
function updateTransactionsList() {
    document.getElementById("transactionsList").textContent =
    JSON.stringify(transactions, null, 2);
}

// Agregar una transacción
function addTransaction() {
    const datetime = document.getElementById("datetime").value;
    const amount = parseFloat(document.getElementById("amount").value);
    if (!datetime || isNaN(amount)) {
        alert("Ingresa fecha, hora y monto válidos");
        return;
    }
    transactions.push({ datetime, amount });
    updateTransactionsList();
}

// Llamar a /parse
function callParse() {
    fetch(`${BASE_URL}/parse`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ transactions })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    })
    .catch(err => alert("Error: " + err));
}

// Llamar a /validator (requiere sueldo)
function callValidator() {
    const salary = prompt("Introduce el sueldo anual:", "450000");
    fetch(`${BASE_URL}/validator`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ transactions, salary: parseFloat(salary) })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    });
}

// Llamar a returns:ppr o returns:ishares
function callReturns(type) {
    const age = prompt("Introduce tu edad:", "30");
    const salary = prompt("Introduce el sueldo anual:", "450000");
    fetch(`http://localhost:5477/blackrock/challenge/v1/returns:${type}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            age: parseInt(age),
                             salary: parseFloat(salary),
                             transactions,
                             q: [],
                             p: [],
                             k: []
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent = JSON.stringify(data, null, 2);
    });
}
