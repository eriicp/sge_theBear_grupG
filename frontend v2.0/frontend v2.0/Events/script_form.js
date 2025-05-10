document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('eventForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Nom_Event = document.getElementById('Nom_Event').value.trim();
        const Data_Event = document.getElementById('Data_Event').value.trim();
        const Hora_Event = document.getElementById('Hora_Event').value.trim();
        const Ubicacio_Event = document.getElementById('Ubicacio_Event').value.trim();
        const Organitzador_Event = parseInt(document.getElementById('Organitzador_Event').value);
        const Estat_Event = document.getElementById('Estat_Event').value.trim();
        const Entrades_Disponibles = parseInt(document.getElementById('Entrades_Disponibles').value);
        const Privat = document.getElementById('Privat').checked;

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Nom_Event', Nom_Event);
            formData.append('Data_Event', Data_Event);
            formData.append('Hora_Event', Hora_Event);
            formData.append('Ubicacio_Event', Ubicacio_Event);
            formData.append('Organitzador_Event', Organitzador_Event);
            formData.append('Estat_Event', Estat_Event);
            formData.append('Entrades_Disponibles', Entrades_Disponibles);
            formData.append('Privat', Privat);

            const response = await fetch('http://localhost:8000/events/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Event creat correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchEvents(); // Actualizar tabla tras creación
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});