document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('puntForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Nom_Punt = document.getElementById('Nom_Punt').value.trim();
        const Producte = document.getElementById('Producte').value.trim();
        const Quantitat = parseInt(document.getElementById('Quantitat').value);
        const Preu_Total = parseFloat(document.getElementById('Preu_Total').value);
        const Metode_Pagament = document.getElementById('Metode_Pagament').value.trim();
        const Tiquet_Email = document.getElementById('Tiquet_Email').checked;
        const Data_Venda = document.getElementById('Data_Venda').value.trim();

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Nom_Punt', Nom_Punt);
            formData.append('Producte', Producte);
            formData.append('Quantitat', Quantitat);
            formData.append('Preu_Total', Preu_Total);
            formData.append('Metode_Pagament', Metode_Pagament);
            formData.append('Tiquet_Email', Tiquet_Email);
            formData.append('Data_Venda', Data_Venda);

            const response = await fetch('http://localhost:8000/punts_de_venda/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Punt de venda creat correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchPunts(); // Actualizar tabla tras creación
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