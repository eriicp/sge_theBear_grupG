document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('vendaForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
const Data_Venda = document.getElementById('data_venda').value.trim();
const Client_Venda = document.getElementById('client_venda').value.trim();
const Producte_Venda = document.getElementById('producte_venda').value.trim();
const Quantitat = parseInt(document.getElementById('quantitat').value);
const Preu_Unitari = parseFloat(document.getElementById('preu_unitari').value);
const Total = parseFloat(document.getElementById('total').value);
const Metode_Pagament = document.getElementById('metode_pagament').value.trim();
const Id_Punt = parseInt(document.getElementById('id_punt').value);

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