document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('puntForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores (IDs actualizados)
        const Nom_Punt = document.getElementById('Nom_punt').value.trim();
        const Producte = document.getElementById('Producte').value.trim();
        const Quantitat = parseInt(document.getElementById('Quantitat').value);
        const Preu_Total = parseFloat(document.getElementById('Preu_Total').value);
        const Metode_Pagament = document.getElementById('metode').value.trim();
        const Tiquet_Email = document.getElementById('Tiquet_Email').checked;
        const Data_Venda = document.getElementById('data').value.trim();

        try {
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
                },
                body: formData.toString()
            });

            if (response.ok) {
                showMessage('Punt creat correctament! Redirigint...', 'success');
                setTimeout(() => {
                    window.location.href = "index_table_users.html";
                }, 1500);
            } else {
                const error = await response.json();
                showMessage(`Error: ${error.detail || 'Error desconegut'}`, 'error');
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