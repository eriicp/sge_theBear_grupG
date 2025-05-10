// URL del endpoint de la API
const API_URL = "http://localhost:8000/planificacio/ver";

// Función para obtener los datos de las planificaciones
async function fetchPlanificacions() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const plans = await response.json(); // Convertimos la respuesta a JSON
        displayPlanificacions(plans); // Mostramos los datos en la tabla
    } catch (error) {
        console.error("Error al obtener las planificaciones:", error);
    }
}

// Función para mostrar las planificaciones en la tabla
function displayPlanificacions(plans) {
    const tableBody = document.querySelector("#planificacionsTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de planificaciones y creamos las filas de la tabla
    plans.forEach(plan => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo de la planificación
        const idCell = document.createElement("td");
        idCell.textContent = plan.Id_Planificacio;
        row.appendChild(idCell);

        const projecteCell = document.createElement("td");
        projecteCell.textContent = plan.Projecte;
        row.appendChild(projecteCell);

        const tascaCell = document.createElement("td");
        tascaCell.textContent = plan.Tasca;
        row.appendChild(tascaCell);

        const responsableCell = document.createElement("td");
        responsableCell.textContent = plan.Responsable;
        row.appendChild(responsableCell);

        const dataIniciCell = document.createElement("td");
        dataIniciCell.textContent = plan.Data_Inici;
        row.appendChild(dataIniciCell);

        const dataFiCell = document.createElement("td");
        dataFiCell.textContent = plan.Data_Fi;
        row.appendChild(dataFiCell);

        const estatCell = document.createElement("td");
        estatCell.textContent = plan.Estat_Tasca;
        row.appendChild(estatCell);

        const materialCell = document.createElement("td");
        materialCell.textContent = plan.Material_Utilitzat ?? "";
        row.appendChild(materialCell);

        const comentarisCell = document.createElement("td");
        comentarisCell.textContent = plan.Comentaris ?? "";
        row.appendChild(comentarisCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar las planificaciones cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchPlanificacions);