// URL del endpoint de la API
const API_URL = "http://localhost:8000/costos/ver";

// Función para obtener los datos de los costos
async function fetchCostos() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const costos = await response.json(); // Convertimos la respuesta a JSON
        displayCostos(costos); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener los costos:", error);
    }
}

// Función para mostrar los costos en la tabla
function displayCostos(costos) {
    const tableBody = document.querySelector("#costosTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de costos y creamos las filas de la tabla
    costos.forEach(cost => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del costo
        const idCell = document.createElement("td");
        idCell.textContent = cost.Id_Cost;
        row.appendChild(idCell);

        const descCell = document.createElement("td");
        descCell.textContent = cost.Descripcio;
        row.appendChild(descCell);

        const categoriaCell = document.createElement("td");
        categoriaCell.textContent = cost.Categoria;
        row.appendChild(categoriaCell);

        const quantitatCell = document.createElement("td");
        quantitatCell.textContent = cost.Quantitat;
        row.appendChild(quantitatCell);

        const dataCell = document.createElement("td");
        dataCell.textContent = cost.Data_Cost;
        row.appendChild(dataCell);

        const pagatPerCell = document.createElement("td");
        pagatPerCell.textContent = cost.Pagat_Per;
        row.appendChild(pagatPerCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los costos cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchCostos);