document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('compraForm');
    const messageDiv = document.getElementById('message');
    const quantitatInput = document.getElementById('Quantitat');
    const preuUnitariInput = document.getElementById('Preu_Unitari');
    const totalInput = document.getElementById('Total');

    // Calcular total automáticamente
    function calcularTotal() {
        const quantitat = parseFloat(quantitatInput.value) || 0;
        const preuUnitari = parseFloat(preuUnitariInput.value) || 0;
        totalInput.value = (quantitat * preuUnitari).toFixed(2);
    }

    quantitatInput.addEventListener('input', calcularTotal);
    preuUnitariInput.addEventListener('input', calcularTotal);

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const formData = new URLSearchParams();
        formData.append('Data_Compra', document.getElementById('Data_Compra').value);
        formData.append('Proveidor', document.getElementById('Proveidor').value.trim());
        formData.append('Producte_Compra', document.getElementById('Producte_Compra').value.trim());
        formData.append('Quantitat', document.getElementById('Quantitat').value);
        formData.append('Preu_Unitari', document.getElementById('Preu_Unitari').value);
        formData.append('Total', document.getElementById('Total').value);
        formData.append('Estat_Comanda', document.getElementById('Estat_Comanda').value.trim());

        try {
            const response = await fetch('http://localhost:8000/compres/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData.toString()
            });

            // Manejo mejorado de la respuesta
            let responseData;
            try {
                responseData = await response.json();
            } catch (error) {
                throw new Error("El servidor devolvió una respuesta no válida");
            }

            if (response.ok) {
                showMessage('Compra creada correctament! Actualitzant...', 'success');
                form.reset();

                // Actualizar la tabla si la función existe
                if (typeof fetchCompres === 'function') {
                    fetchCompres();
                }

                // Redirigir después de 2 segundos
                setTimeout(() => {
                    window.location.href = "index_table_users.html";
                }, 2000);
            } else {
                // Extraer mensaje de error de diferentes formatos posibles
                let errorMsg = "Error desconocido";
                if (responseData.detail) {
                    errorMsg = typeof responseData.detail === 'string'
                        ? responseData.detail
                        : JSON.stringify(responseData.detail);
                } else if (responseData.message) {
                    errorMsg = responseData.message;
                } else {
                    errorMsg = JSON.stringify(responseData);
                }
                throw new Error(errorMsg);
            }
        } catch (error) {
            console.error("Error en el formulario:", error);
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