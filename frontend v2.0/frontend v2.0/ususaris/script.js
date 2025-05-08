// URL del endpoint de la API
const API_URL = "http://localhost:8000/empleats/ver";

// Función para obtener los datos de los usuarios
async function fetchUsers() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`Error en la solicitud: ${response.status}`);
        }
        const users = await response.json(); // Convertimos la respuesta a JSON
        displayUsers(users); // Mostramos los datos en la tabla
        // console.log(users);
    } catch (error) {
        console.error("Error al obtener los usuarios:", error);
    }
}

// Función para mostrar los usuarios en la tabla
function displayUsers(users) {
    const tableBody = document.querySelector("#usersTable tbody");

    // Limpiamos el contenido actual de la tabla
    tableBody.innerHTML = "";

    // Iteramos sobre la lista de usuarios y creamos las filas de la tabla
    users.forEach(user => {
        const row = document.createElement("tr");

        // Creamos las celdas para cada campo del usuario
        const idCell = document.createElement("td");
        idCell.textContent = user.Id_Empleat;
        row.appendChild(idCell);

        const nameCell = document.createElement("td");
        nameCell.textContent = user.Nombre_Empleat;
        row.appendChild(nameCell);

        const puestoCell = document.createElement("td");
        puestoCell.textContent = user.Puesto_Empleat;
        row.appendChild(puestoCell);

        const departamentCell = document.createElement("td");
        departamentCell.textContent = user.Departament_Empleat;
        row.appendChild(departamentCell);

        const emailCell = document.createElement("td");
        emailCell.textContent = user.Email_Empleat;
        row.appendChild(emailCell);

        const telefonCell = document.createElement("td");
        telefonCell.textContent = user.Telefon_Empleat;
        row.appendChild(telefonCell);

        const idGerentCell = document.createElement("td");
        idGerentCell.textContent = user.Id_Gerent_Empleat ?? ""; // Por si es null o undefined
        row.appendChild(idGerentCell);

        // Añadimos la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Llamamos a la función para obtener y mostrar los usuarios cuando la página se carga
document.addEventListener("DOMContentLoaded", fetchUsers);