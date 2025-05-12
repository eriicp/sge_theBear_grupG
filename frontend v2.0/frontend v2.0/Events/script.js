const API_URL = "http://localhost:8000/events/ver";

async function fetchEvents() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        const events = await response.json();

        console.log("Datos recibidos:", events); // Para depuración
        displayEvents(events);
    } catch (error) {
        console.error("Error al obtener eventos:", error);
        showTableError(error.message);
    }
}

function displayEvents(events) {
    const tableBody = document.querySelector("#eventsTable tbody");
    tableBody.innerHTML = "";

    if (!events || events.length === 0) {
        showTableMessage("No hi ha events disponibles");
        return;
    }

    events.forEach(event => {
        const row = document.createElement("tr");

        // Aplicar clase según el estado
        if (event.Estat_Event) {
            const estatClass = `estat-${event.Estat_Event.toLowerCase().replace(/[·\s]/g, '-')}`;
            row.classList.add(estatClass);
        }

        row.innerHTML = `
            <td>${event.Id_Event || '-'}</td>
            <td>${event.Nom_Event || '-'}</td>
            <td>${formatDate(event.Data_Event)}</td>
            <td>${event.Hora_Event || '-'}</td>
            <td>${event.Ubicacio_Event || '-'}</td>
            <td>${event.Organitzador_Event || 'Desconegut'}</td>
            <td>${event.Estat_Event || '-'}</td>
            <td>${event.Entrades_Disponibles ?? 0}</td>
            <td>${formatBoolean(event.Privat)}</td>
        `;

        tableBody.appendChild(row);
    });
}

function formatDate(dateString) {
    if (!dateString) return '-';
    try {
        const date = new Date(dateString);
        return isNaN(date.getTime()) ? 'Data invàlida' : date.toLocaleDateString('ca-ES');
    } catch {
        return dateString; // Si falla el parsing, mostrar el valor original
    }
}

function formatBoolean(value) {
    if (value === true) return "Sí";
    if (value === false) return "No";
    return '-';
}

function showTableMessage(message) {
    const tableBody = document.querySelector("#eventsTable tbody");
    tableBody.innerHTML = `<tr><td colspan="9" style="text-align: center;">${message}</td></tr>`;
}

function showTableError(errorMsg) {
    const tableBody = document.querySelector("#eventsTable tbody");
    tableBody.innerHTML = `
        <tr><td colspan="9" style="color: red; text-align: center;">
            Error carregant dades: ${errorMsg}
        </td></tr>`;
}

// Iniciar carga de eventos
document.addEventListener("DOMContentLoaded", fetchEvents);