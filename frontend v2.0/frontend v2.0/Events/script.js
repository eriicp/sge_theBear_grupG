// URL del endpoint de la API
const API_URL = "http://localhost:8000/events/ver";

// Función para obtener los datos de los eventos
async function fetchEvents() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const events = await response.json(); // Convertimos la respuesta a JSON
        displayEvents(events); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener los eventos:", error);
    }
}

// Función para mostrar los eventos en la tabla
function displayEvents(events) {
    const tableBody = document.querySelector("#eventsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de eventos y creamos las filas de la tabla
    events.forEach(event => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del evento
        const idCell = document.createElement("td");
        idCell.textContent = event.Id_Event;
        row.appendChild(idCell);

        const nomCell = document.createElement("td");
        nomCell.textContent = event.Nom_Event;
        row.appendChild(nomCell);

        const dataCell = document.createElement("td");
        dataCell.textContent = event.Data_Event;
        row.appendChild(dataCell);

        const horaCell = document.createElement("td");
        horaCell.textContent = event.Hora_Event;
        row.appendChild(horaCell);

        const ubicacioCell = document.createElement("td");
        ubicacioCell.textContent = event.Ubicacio_Event;
        row.appendChild(ubicacioCell);

        const organitzadorCell = document.createElement("td");
        organitzadorCell.textContent = event.Organitzador_Event;
        row.appendChild(organitzadorCell);

        const estatCell = document.createElement("td");
        estatCell.textContent = event.Estat_Event;
        row.appendChild(estatCell);

        const entradesCell = document.createElement("td");
        entradesCell.textContent = event.Entrades_Disponibles;
        row.appendChild(entradesCell);

        const privatCell = document.createElement("td");
        privatCell.textContent = event.Privat ? "Sí" : "No";
        row.appendChild(privatCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los eventos cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchEvents);