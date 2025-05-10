document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('planificacioForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Projecte = document.getElementById('Projecte').value.trim();
        const Tasca = document.getElementById('Tasca').value.trim();
        const Responsable = parseInt(document.getElementById('Responsable').value);
        const Data_Inici = document.getElementById('Data_Inici').value.trim();
        const Data_Fi = document.getElementById('Data_Fi').value.trim();
        const Estat_Tasca = document.getElementById('Estat_Tasca').value.trim();
        const Material_Utilitzat = document.getElementById('Material_Utilitzat').value.trim();
        const Comentaris = document.getElementById('Comentaris').value.trim();

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Projecte', Projecte);
            formData.append('Tasca', Tasca);
            formData.append('Responsable', Responsable);
            formData.append('Data_Inici', Data_Inici);
            formData.append('Data_Fi', Data_Fi);
            formData.append('Estat_Tasca', Estat_Tasca);
            if (Material_Utilitzat) formData.append('Material_Utilitzat', Material_Utilitzat);
            if (Comentaris) formData.append('Comentaris', Comentaris);

            const response = await fetch('http://localhost:8000/planificacio/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Planificació creada correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchPlanificacions(); // Actualizar tabla tras creación
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