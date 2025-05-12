const API_URL = "http://localhost:8000/costos/ver";

async function fetchCostos() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`Error: ${response.status}`);
        const costos = await response.json();

        console.log("Datos recibidos del servidor:", costos);
        displayCostos(costos);
    } catch (error) {
        console.error("Error al obtener costos:", error);
        document.querySelector("#costosTable tbody").innerHTML =
            `<tr><td colspan="6" style="color: red; text-align: center;">Error carregant dades: ${error.message}</td></tr>`;
    }
}

function displayCostos(costos) {
    const tableBody = document.querySelector("#costosTable tbody");
    tableBody.innerHTML = "";

    if (!costos || costos.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="6" style="text-align: center;">No hi ha costos registrats</td></tr>`;
        return;
    }

    costos.forEach(cost => {
        const row = document.createElement("tr");

        // ID
        const idCell = document.createElement("td");
        idCell.textContent = cost.Id_Cost || '-';
        row.appendChild(idCell);

        // Descripción
        const descCell = document.createElement("td");
        descCell.textContent = cost.Descripcio || '-';
        row.appendChild(descCell);

        // Categoría
        const categoriaCell = document.createElement("td");
        categoriaCell.textContent = cost.Categoria || '-';
        row.appendChild(categoriaCell);

        // Cantidad (formato moneda)
        const quantitatCell = document.createElement("td");
        const quantitat = parseFloat(cost.Quantitat);
        quantitatCell.textContent = isNaN(quantitat) ? '-' :
                                  `${quantitat.toFixed(2)} €`;
        quantitatCell.style.textAlign = 'right';
        row.appendChild(quantitatCell);

        // Fecha (formateada)
        const dataCell = document.createElement("td");
        const costDate = new Date(cost.Data_Cost);
        dataCell.textContent = isNaN(costDate.getTime()) ?
            'Data invàlida' :
            costDate.toLocaleDateString('ca-ES');
        row.appendChild(dataCell);

        // Pagado por
        const pagatPerCell = document.createElement("td");
        pagatPerCell.textContent = cost.Pagat_Per || 'Desconegut';
        row.appendChild(pagatPerCell);

        tableBody.appendChild(row);
    });
}

// Iniciar carga de costos
document.addEventListener("DOMContentLoaded", fetchCostos);