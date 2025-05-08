// URL del endpoint de la API
const API_URL = "http://localhost:8000/compres/ver";

// Función para obtener los datos de las compras
async function fetchCompres() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const compres = await response.json(); // Convertimos la respuesta a JSON
        displayCompres(compres); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener las compras:", error);
    }
}

// Función para mostrar las compras en la tabla
function displayCompres(compres) {
    const tableBody = document.querySelector("#compresTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de compras y creamos las filas de la tabla
    compres.forEach(compra => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo de la compra
        const idCell = document.createElement("td");
        idCell.textContent = compra.Id_Compra;
        row.appendChild(idCell);

        const dataCell = document.createElement("td");
        dataCell.textContent = compra.Data_Compra;
        row.appendChild(dataCell);

        const proveidorCell = document.createElement("td");
        proveidorCell.textContent = compra.Proveidor;
        row.appendChild(proveidorCell);

        const producteCell = document.createElement("td");
        producteCell.textContent = compra.Producte_Compra;
        row.appendChild(producteCell);

        const quantitatCell = document.createElement("td");
        quantitatCell.textContent = compra.Quantitat;
        row.appendChild(quantitatCell);

        const preuUnitariCell = document.createElement("td");
        preuUnitariCell.textContent = compra.Preu_Unitari;
        row.appendChild(preuUnitariCell);

        const totalCell = document.createElement("td");
        totalCell.textContent = compra.Total;
        row.appendChild(totalCell);

        const estatCell = document.createElement("td");
        estatCell.textContent = compra.Estat_Comanda;
        row.appendChild(estatCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar las compras cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchCompres);