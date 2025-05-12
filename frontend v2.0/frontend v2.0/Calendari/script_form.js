document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reunionForm');  // Cambiado a reunionForm
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Nom_Reunio = document.getElementById('Nom_Reunio').value.trim();
        const Data_Reunio = document.getElementById('Data_Reunio').value.trim();
        const Hora_Inici = document.getElementById('Hora_Inici').value.trim();
        const Hora_Fi = document.getElementById('Hora_Fi').value.trim();
        const Ubicacio_Reunio = document.getElementById('Ubicacio_Reunio').value.trim();
        const Etiquetes = document.getElementById('Etiquetes').value.trim();
        const Recurrencia = document.getElementById('Recurrencia').checked;  // Ahora es un checkbox

        try {
            const formData = new URLSearchParams();
            formData.append('Nom_Reunio', Nom_Reunio);
            formData.append('Data_Reunio', Data_Reunio);
            formData.append('Hora_Inici', Hora_Inici);
            formData.append('Hora_Fi', Hora_Fi);
            formData.append('Ubicacio_Reunio', Ubicacio_Reunio);
            if (Etiquetes) formData.append('Etiquetes', Etiquetes);
            formData.append('Recurrencia', Recurrencia);

            const response = await fetch('http://localhost:8000/calendari/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Reunió creada correctament!', 'success');
                form.reset();
                
            } else {
                showMessage(`Error: ${data.detail || 'Error desconegut'}`, 'error');
            }
        } catch (error) {
            console.error("Error completo:", error);
            showMessage(`Error de connexió: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});