document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('costForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        try {
            // Validar datos
            const quantitat = parseFloat(document.getElementById('Quantitat').value);
            if (isNaN(quantitat) || quantitat <= 0) {
                throw new Error("La quantitat ha de ser un número positiu");
            }

            const dataCost = new Date(document.getElementById('Data_Cost').value);
            if (isNaN(dataCost.getTime())) {
                throw new Error("La data del cost no és vàlida");
            }

            const pagatPer = parseInt(document.getElementById('Pagat_Per').value);
            if (isNaN(pagatPer)) {
                throw new Error("L'ID de qui ha pagat ha de ser un número");
            }

            // Preparar datos
            const formData = new URLSearchParams();
            formData.append('Descripcio', document.getElementById('Descripcio').value.trim());
            formData.append('Categoria', document.getElementById('Categoria').value.trim());
            formData.append('Quantitat', quantitat.toFixed(2)); // Formato 2 decimales
            formData.append('Data_Cost', document.getElementById('Data_Cost').value);
            formData.append('Pagat_Per', pagatPer);

            // Enviar datos
            const response = await fetch('http://localhost:8000/costos/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData.toString()
            });

            const responseData = await response.json();

            if (!response.ok) {
                const errorMsg = responseData.detail ||
                               (responseData.message || 'Error desconegut');
                throw new Error(typeof errorMsg === 'object' ? JSON.stringify(errorMsg) : errorMsg);
            }

            // Éxito
            showMessage('Cost creat correctament! Redirigint...', 'success');
            setTimeout(() => {
                window.location.href = "index_table_users.html";
            }, 1500);

        } catch (error) {
            let errorMessage = error.message;
            try {
                const parsedError = JSON.parse(error.message);
                if (parsedError && typeof parsedError === 'object') {
                    errorMessage = Object.entries(parsedError)
                        .map(([key, value]) => `${key}: ${value}`)
                        .join(', ');
                }
            } catch (e) {}

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