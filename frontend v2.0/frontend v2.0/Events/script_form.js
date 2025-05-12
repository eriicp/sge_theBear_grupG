document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('eventForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        try {
            // Validación de entradas disponibles
            const entradesInput = document.getElementById('Entrades_Disponibles');
            const entrades = parseInt(entradesInput.value);
            if (isNaN(entrades) || entrades < 0) {
                throw new Error("Les entrades disponibles han de ser un número positiu");
            }

            // Validación de fecha
            const dataEvent = document.getElementById('Data_Event').value;
            if (!dataEvent) {
                throw new Error("La data de l'event és obligatòria");
            }

            // Validación de organizador
            const orgValue = document.getElementById('Organitzador_Event').value.trim();
            if (!orgValue || isNaN(orgValue)) {
                throw new Error("L'organitzador ha de ser un ID numèric vàlid");
            }

            // Preparar datos del formulario
            const formData = new URLSearchParams();
            formData.append('Nom_Event', document.getElementById('Nom_Event').value.trim());
            formData.append('Data_Event', dataEvent);
            formData.append('Hora_Event', document.getElementById('Hora_Event').value || '00:00');
            formData.append('Ubicacio_Event', document.getElementById('Ubicacio_Event').value.trim());
            formData.append('Organitzador_Event', orgValue);
            formData.append('Estat_Event', document.getElementById('Estat_Event').value);
            formData.append('Entrades_Disponibles', entrades);
            formData.append('Privat', document.getElementById('Privat').checked ? 'true' : 'false');

            // Enviar datos al servidor
            const response = await fetch('http://localhost:8000/events/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const responseData = await response.json();

            if (!response.ok) {
                const errorMsg = responseData.detail ||
                               (responseData.message || `Error del servidor: ${response.status}`);
                throw new Error(errorMsg);
            }

            // Éxito - mostrar mensaje y redirigir
            showMessage('Event creat correctament! Redirigint...', 'success');
            setTimeout(() => {
                window.location.href = "index_table_users.html";
            }, 1500);

        } catch (error) {
            console.error("Error al crear event:", error);
            showMessage(`Error: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = `message ${type}`;
        setTimeout(() => {
            messageDiv.textContent = '';
            messageDiv.className = 'message';
        }, 5000);
    }
});