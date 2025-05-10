// URL del endpoint de la API
const API_URL = "http://localhost:8000/vendes/ver";

// Función para obtener los datos de las ventas
async function fetchVendes() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const vendes = await response.json(); // Convertimos la respuesta a JSON
        displayVendes(vendes); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener las ventas:", error);
    }
}

// Función para mostrar las ventas en la tabla
function displayVendes(vendes) {
    const tableBody = document.querySelector("#vendesTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de ventas y creamos las filas de la tabla
    vendes.forEach(venda => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo de la venta
        const idCell = document.createElement("td");
        idCell.textContent = venda.Id_Venda;
        row.appendChild(idCell);

        const dataCell = document.createElement("td");
        dataCell.textContent = venda.Data_Venda;
        row.appendChild(dataCell);

        const clientCell = document.createElement("td");
        clientCell.textContent = venda.Client_Venda;
        row.appendChild(clientCell);

        const producteCell = document.createElement("td");
        producteCell.textContent = venda.Producte_Venda;
        row.appendChild(producteCell);

        const quantitatCell = document.createElement("td");
        quantitatCell.textContent = venda.Quantitat;
        row.appendChild(quantitatCell);

        const preuUnitariCell = document.createElement("td");
        preuUnitariCell.textContent = venda.Preu_Unitari;
        row.appendChild(preuUnitariCell);

        const totalCell = document.createElement("td");
        totalCell.textContent = venda.Total;
        row.appendChild(totalCell);

        const metodeCell = document.createElement("td");
        metodeCell.textContent = venda.Metode_Pagament;
        row.appendChild(metodeCell);

        const idPuntCell = document.createElement("td");
        idPuntCell.textContent = venda.Id_Punt;
        row.appendChild(idPuntCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar las ventas cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchVendes);