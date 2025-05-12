const API_URL = "http://localhost:8000/planificacio/ver";

async function fetchPlanificacions() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        const plans = await response.json();
        displayPlanificacions(plans);
    } catch (error) {
        console.error("Error al obtener planificaciones:", error);
    }
}

function displayPlanificacions(plans) {
    const tableBody = document.querySelector("#planificacionsTable tbody");
    tableBody.innerHTML = "";

    plans.forEach(plan => {
        const row = document.createElement("tr");

        // ID
        const idCell = document.createElement("td");
        idCell.textContent = plan.Id_Planificacio;
        row.appendChild(idCell);

        // Proyecto
        const projecteCell = document.createElement("td");
        projecteCell.textContent = plan.Projecte;
        row.appendChild(projecteCell);

        // Tarea
        const tascaCell = document.createElement("td");
        tascaCell.textContent = plan.Tasca;
        row.appendChild(tascaCell);

        // Responsable (convertir ID a nombre si es necesario)
        const responsableCell = document.createElement("td");
        responsableCell.textContent = plan.Responsable;
        row.appendChild(responsableCell);

        // Fechas
        const dataIniciCell = document.createElement("td");
        dataIniciCell.textContent = new Date(plan.Data_Inici).toLocaleDateString();
        row.appendChild(dataIniciCell);

        const dataFiCell = document.createElement("td");
        dataFiCell.textContent = new Date(plan.Data_Fi).toLocaleDateString();
        row.appendChild(dataFiCell);

        // Estado
        const estatCell = document.createElement("td");
        estatCell.textContent = plan.Estat_Tasca;
        row.appendChild(estatCell);

        // Materiales (puede ser null)
        const materialCell = document.createElement("td");
        materialCell.textContent = plan.Material_Utilitzat || "-";
        row.appendChild(materialCell);

        // Comentarios (puede ser null)
        const comentarisCell = document.createElement("td");
        comentarisCell.textContent = plan.Comentaris || "-";
        row.appendChild(comentarisCell);

        tableBody.appendChild(row);
    });
}

document.addEventListener("DOMContentLoaded", fetchPlanificacions);