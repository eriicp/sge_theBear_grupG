document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('compraForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Data_Compra = document.getElementById('Data_Compra').value.trim();
        const Proveidor = document.getElementById('Proveidor').value.trim();
        const Producte_Compra = document.getElementById('Producte_Compra').value.trim();
        const Quantitat = parseInt(document.getElementById('Quantitat').value);
        const Preu_Unitari = parseFloat(document.getElementById('Preu_Unitari').value);
        const Total = parseFloat(document.getElementById('Total').value);
        const Estat_Comanda = document.getElementById('Estat_Comanda').value.trim();

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Data_Compra', Data_Compra);
            formData.append('Proveidor', Proveidor);
            formData.append('Producte_Compra', Producte_Compra);
            formData.append('Quantitat', Quantitat);
            formData.append('Preu_Unitari', Preu_Unitari);
            formData.append('Total', Total);
            formData.append('Estat_Comanda', Estat_Comanda);

            const response = await fetch('http://localhost:8000/compres/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Compra creada correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchCompres(); // Actualizar tabla tras creación
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