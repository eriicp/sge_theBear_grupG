// URL del endpoint de la API
const API_URL = "http://localhost:8000/calendari/ver";

// Función para obtener los datos de las reuniones
async function fetchReunions() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const reunions = await response.json(); // Convertimos la respuesta a JSON
        displayReunions(reunions); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener las reuniones:", error);
    }
}

// Función para mostrar las reuniones en la tabla
function displayReunions(reunions) {
    const tableBody = document.querySelector("#reunionsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de reuniones y creamos las filas de la tabla
    reunions.forEach(reunion => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo de la reunión
        const idCell = document.createElement("td");
        idCell.textContent = reunion.Id_Reunio;
        row.appendChild(idCell);

        const nomCell = document.createElement("td");
        nomCell.textContent = reunion.Nom_Reunio;
        row.appendChild(nomCell);

        const dataCell = document.createElement("td");
        dataCell.textContent = reunion.Data_Reunio;
        row.appendChild(dataCell);

        const iniciCell = document.createElement("td");
        iniciCell.textContent = reunion.Hora_Inici;
        row.appendChild(iniciCell);

        const fiCell = document.createElement("td");
        fiCell.textContent = reunion.Hora_Fi;
        row.appendChild(fiCell);

        const ubicacioCell = document.createElement("td");
        ubicacioCell.textContent = reunion.Ubicacio_Reunio;
        row.appendChild(ubicacioCell);

        const etiquetesCell = document.createElement("td");
        etiquetesCell.textContent = reunion.Etiquetes ?? "";
        row.appendChild(etiquetesCell);

        const recurrenciaCell = document.createElement("td");
        recurrenciaCell.textContent = reunion.Recurrencia ? "Sí" : "No";
        row.appendChild(recurrenciaCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar las reuniones cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchReunions);