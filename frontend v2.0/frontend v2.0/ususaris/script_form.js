document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('userForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Obtener valores del formulario
        const Nombre_Empleat = document.getElementById('Nombre_Empleat').value.trim();
        const Puesto_Empleat = document.getElementById('Puesto_Empleat').value.trim();
        const Departament_Empleat = document.getElementById('Departament_Empleat').value.trim();
        const Email_Empleat = document.getElementById('Email_Empleat').value.trim();
        const Telefon_Empleat = document.getElementById('Telefon_Empleat').value.trim();
        const Id_Gerent_Empleat_value = document.getElementById('Id_Gerent_Empleat').value.trim();
        const Id_Gerent_Empleat = Id_Gerent_Empleat_value === '' ? null : parseInt(Id_Gerent_Empleat_value);

        try {
            // Crear objeto FormData para enviar como application/x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('Nombre_Empleat', Nombre_Empleat);
            formData.append('Puesto_Empleat', Puesto_Empleat);
            formData.append('Departament_Empleat', Departament_Empleat);
            formData.append('Email_Empleat', Email_Empleat);
            formData.append('Telefon_Empleat', Telefon_Empleat);
            if (Id_Gerent_Empleat !== null) {
                formData.append('Id_Gerent_Empleat', Id_Gerent_Empleat);
            }

            const response = await fetch('http://localhost:8000/empleats/crear', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'application/json'
                },
                body: formData.toString()
            });

            const data = await response.json();

            if (response.ok) {
                showMessage(data.message || 'Empleado creado correctamente!', 'success');
                form.reset(); // Limpiar formulario
            } else {
                showMessage(`Error: ${data.detail || 'Error desconocido'}`, 'error');
            }
        } catch (error) {
            showMessage(`Error de conexiÃ³n: ${error.message}`, 'error');
        }
    });

    function showMessage(text, type) {
        messageDiv.textContent = text;
        messageDiv.className = 'message ' + type;
    }
});