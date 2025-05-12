const API_URL = "http://localhost:8000/compres/ver";

async function fetchCompres() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || errorData.message || `Error ${response.status}`);
        }
        const compres = await response.json();
        displayCompres(compres);
    } catch (error) {
        console.error("Error al obtener compres:", error);
        showTableError(error.message);
    }
}

function displayCompres(compres) {
    const tableBody = document.querySelector("#compresTable tbody");
    tableBody.innerHTML = "";

    if (!compres || compres.length === 0) {
        showTableMessage("No hi ha compres registrades");
        return;
    }

    compres.forEach(compra => {
        const row = document.createElement("tr");

        // Formatear fecha
        const dataCell = document.createElement("td");
        try {
            const data = new Date(compra.Data_Compra);
            dataCell.textContent = data.toLocaleDateString('ca-ES');
        } catch {
            dataCell.textContent = compra.Data_Compra || '-';
        }

        // Formatear precios
        const preuCell = document.createElement("td");
        preuCell.textContent = compra.Preu_Unitari ?
            `${parseFloat(compra.Preu_Unitari).toFixed(2)} €` : '-';
        preuCell.style.textAlign = 'right';

        const totalCell = document.createElement("td");
        totalCell.textContent = compra.Total ?
            `${parseFloat(compra.Total).toFixed(2)} €` : '-';
        totalCell.style.textAlign = 'right';

        // Añadir celdas
        row.innerHTML = `
            <td>${compra.Id_Compra || '-'}</td>
            <td>${dataCell.textContent}</td>
            <td>${compra.Proveidor || '-'}</td>
            <td>${compra.Producte_Compra || '-'}</td>
            <td style="text-align: right;">${compra.Quantitat || 0}</td>
            <td style="text-align: right;">${preuCell.textContent}</td>
            <td style="text-align: right;">${totalCell.textContent}</td>
            <td>${compra.Estat_Comanda || '-'}</td>
        `;

        tableBody.appendChild(row);
    });
}

function showTableMessage(message) {
    const tableBody = document.querySelector("#compresTable tbody");
    tableBody.innerHTML = `
        <tr>
            <td colspan="8" style="text-align: center;">
                ${message}
            </td>
        </tr>`;
}

function showTableError(error) {
    const tableBody = document.querySelector("#compresTable tbody");
    tableBody.innerHTML = `
        <tr>
            <td colspan="8" style="text-align: center; color: red;">
                Error: ${error}
            </td>
        </tr>`;
}

// Iniciar carga de compras
document.addEventListener("DOMContentLoaded", fetchCompres);

// Hacer la función accesible globalmente
window.fetchCompres = fetchCompres;