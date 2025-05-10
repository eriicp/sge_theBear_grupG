// URL del endpoint de la API
const API_URL = "http://localhost:8000/punts_de_venda/ver";

// Función para obtener los datos de los puntos de venta
async function fetchPunts() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const punts = await response.json(); // Convertimos la respuesta a JSON
        displayPunts(punts); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener los punts de venda:", error);
    }
}

// Función para mostrar los puntos de venta en la tabla
function displayPunts(punts) {
    const tableBody = document.querySelector("#puntsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de punts y creamos las filas de la tabla
    punts.forEach(punt => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del punt de venda
        const idCell = document.createElement("td");
        idCell.textContent = punt.Id_Punt;
        row.appendChild(idCell);

        const nomCell = document.createElement("td");
        nomCell.textContent = punt.Nom_Punt;
        row.appendChild(nomCell);

        const producteCell = document.createElement("td");
        producteCell.textContent = punt.Producte;
        row.appendChild(producteCell);

        const quantitatCell = document.createElement("td");
        quantitatCell.textContent = punt.Quantitat;
        row.appendChild(quantitatCell);

        const preuTotalCell = document.createElement("td");
        preuTotalCell.textContent = punt.Preu_Total;
        row.appendChild(preuTotalCell);

        const metodeCell = document.createElement("td");
        metodeCell.textContent = punt.Metode_Pagament;
        row.appendChild(metodeCell);

        const tiquetCell = document.createElement("td");
        tiquetCell.textContent = punt.Tiquet_Email ? "Sí" : "No";
        row.appendChild(tiquetCell);

        const dataVendaCell = document.createElement("td");
        dataVendaCell.textContent = punt.Data_Venda;
        row.appendChild(dataVendaCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los punts cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchPunts);