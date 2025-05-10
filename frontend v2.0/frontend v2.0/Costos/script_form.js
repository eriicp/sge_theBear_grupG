document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('costForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Descripcio = document.getElementById('Descripcio').value.trim();
        const Categoria = document.getElementById('Categoria').value.trim();
        const Quantitat = parseFloat(document.getElementById('Quantitat').value);
        const Data_Cost = document.getElementById('Data_Cost').value.trim();
        const Pagat_Per = parseInt(document.getElementById('Pagat_Per').value);

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Descripcio', Descripcio);
            formData.append('Categoria', Categoria);
            formData.append('Quantitat', Quantitat);
            formData.append('Data_Cost', Data_Cost);
            formData.append('Pagat_Per', Pagat_Per);

            const response = await fetch('http://localhost:8000/costos/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Cost creat correctament!', 'success');
                form.reset(); // Limpiar formulario
                fetchCostos(); // Actualizar tabla tras creación
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