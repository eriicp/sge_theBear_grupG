document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('planificacioForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        try {
            // Validación de fechas
            const dataInici = new Date(document.getElementById('Data_Inici').value);
            const dataFi = new Date(document.getElementById('Data_Fi').value);

            if (dataFi < dataInici) {
                throw new Error("La data fi no pot ser anterior a la data d'inici");
            }

            // Obtener valores
            const formData = new URLSearchParams();
            formData.append('Projecte', document.getElementById('Projecte').value.trim());
            formData.append('Tasca', document.getElementById('Tasca').value.trim());

            // Validar que Responsable es un número
            const responsableValue = document.getElementById('Responsable').value.trim();
            if (isNaN(responsableValue)) {
                throw new Error("El responsable debe ser un ID numérico");
            }
            formData.append('Responsable', responsableValue);

            formData.append('Data_Inici', document.getElementById('Data_Inici').value);
            formData.append('Data_Fi', document.getElementById('Data_Fi').value);
            formData.append('Estat_Tasca', document.getElementById('Estat_Tasca').value.trim());

            const material = document.getElementById('Material_Utilitzat').value.trim();
            if (material) formData.append('Material_Utilitzat', material);

            const comentaris = document.getElementById('Comentaris').value.trim();
            if (comentaris) formData.append('Comentaris', comentaris);

            const response = await fetch('http://localhost:8000/planificacio/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData.toString()
            });

            const responseData = await response.json();

            if (!response.ok) {
                // Manejar errores del backend
                const errorMsg = responseData.detail ||
                                (responseData.message || 'Error desconegut');
                if (typeof errorMsg === 'object') {
                    throw new Error(JSON.stringify(errorMsg));
                } else {
                    throw new Error(errorMsg);
                }
            }

            // Éxito
            showMessage('Planificació creada correctament!');
            setTimeout(() => {
                window.location.href = "index_table_users.html";
            }, 1500);

        } catch (error) {
            // Mostrar mensaje de error claro
            let errorMessage = error.message;

            // Si es un string JSON, parsearlo
            try {
                const parsedError = JSON.parse(error.message);
                if (parsedError && typeof parsedError === 'object') {
                    errorMessage = Object.entries(parsedError)
                        .map(([key, value]) => `${key}: ${value}`)
                        .join(', ');
                }
            } catch (e) {
                // No es JSON, mantener el mensaje original
            }

            showMessage(`Error: ${errorMessage}`, 'error');
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