document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('vendaForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Data_Venda = document.getElementById('Data_Venda').value.trim();
        const Client_Venda = document.getElementById('Client_Venda').value.trim();
        const Producte_Venda = document.getElementById('Producte_Venda').value.trim();
        const Quantitat = parseInt(document.getElementById('Quantitat').value);
        const Preu_Unitari = parseFloat(document.getElementById('Preu_Unitari').value);
        const Total = parseFloat(document.getElementById('Total').value);
        const Metode_Pagament = document.getElementById('Metode_Pagament').value.trim();
        const Id_Punt = parseInt(document.getElementById('Id_Punt').value);

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Data_Venda', Data_Venda);
            formData.append('Client_Venda', Client_Venda);
            formData.append('Producte_Venda', Producte_Venda);
            formData.append('Quantitat', Quantitat);
            formData.append('Preu_Unitari', Preu_Unitari);
            formData.append('Total', Total);
            formData.append('Metode_Pagament', Metode_Pagament);
            formData.append('Id_Punt', Id_Punt);

            const response = await fetch('http://localhost:8000/vendes/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Venda creada correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchVendes(); // Actualizar tabla tras creación
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