

// Abrir modal
const guardar = document.createElement('button')
const cancelar_save = document.createElement('button')
function openModal() {
    document.getElementById('modalTitle').textContent = 'Nuevo Aprendiz';
    document.getElementById('aprendizForm').reset();
    document.getElementById('modalOverlay').classList.add('active');

    guardar.textContent = 'Guardar'
    guardar.type = 'submit'
    guardar.className = 'btn-primary'
    document.getElementById('aprendizForm').appendChild(guardar)
    
    cancelar_save.textContent = 'Cancelar'
    cancelar_save.className = 'btn-secondary'
    cancelar_save.type = 'button'    
    document.getElementById('aprendizForm').appendChild(cancelar_save)
    cancelar_save.addEventListener('click', closeModal)
}

// Cerrar modal
function closeModal() {
    document.getElementById('modalOverlay').classList.remove('active');
    document.getElementById('aprendizForm').removeChild(cancelar_save)
    document.getElementById('aprendizForm').removeChild(guardar)
    editingId = null;
}

// Guardar aprendiz
function saveAprendiz() {
    const form = document.getElementById('aprendizForm');
    const formData = new FormData(form);
    
    const aprendiz = {
        nombres: document.getElementById('nombres').value,
        apellidos: document.getElementById('apellidos').value,
        documento: document.getElementById('documento').value,
        tipoDocumento: document.getElementById('tipoDocumento').value,
        telefono: document.getElementById('telefono').value,
        email: document.getElementById('email').value,
        programa: document.getElementById('programa').options[document.getElementById('programa').selectedIndex].text,
        ficha: document.getElementById('ficha').value,
        estado: document.getElementById('estado').value,
        direccion: document.getElementById('direccion').value
    };

    // Validar campos requeridos
    if (!aprendiz.nombres || !aprendiz.apellidos || !aprendiz.documento || !aprendiz.programa) {
        return;
    }

    if (editingId) {
        // Editar existente
        const index = aprendices.findIndex(a => a.id === editingId);
        aprendices[index] = { ...aprendices[index], ...aprendiz };
    } else {
        // Crear nuevo
        aprendiz.id = Date.now();
        aprendices.push(aprendiz);
    }

    renderAprendices();
    closeModal();
}

// Editar aprendiz
function editAprendiz(id) {
    const aprendiz = aprendices.find(a => a.id === id);
    if (!aprendiz) return;

    editingId = id;
    document.getElementById('modalTitle').textContent = 'Editar Aprendiz';
    
    // Llenar formulario
    document.getElementById('nombres').value = aprendiz.nombres;
    document.getElementById('apellidos').value = aprendiz.apellidos;
    document.getElementById('documento').value = aprendiz.documento;
    document.getElementById('tipoDocumento').value = aprendiz.tipoDocumento;
    document.getElementById('telefono').value = aprendiz.telefono;
    document.getElementById('email').value = aprendiz.email;
    document.getElementById('ficha').value = aprendiz.ficha;
    document.getElementById('estado').value = aprendiz.estado;
    document.getElementById('direccion').value = aprendiz.direccion;

    document.getElementById('modalOverlay').classList.add('active');
}


// Buscar aprendices
document.getElementById('searchInput').addEventListener('input', function(e) {
    const query = e.target.value.toLowerCase();
    const filtered = aprendices.filter(aprendiz => 
        aprendiz.nombres.toLowerCase().includes(query) ||
        aprendiz.apellidos.toLowerCase().includes(query) ||
        aprendiz.documento.includes(query) ||
        aprendiz.programa.toLowerCase().includes(query)
    );
    
    const grid = document.getElementById('aprendicesGrid');
    if (filtered.length === 0 && query) {
        grid.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🔍</div>
                <h3>No se encontraron resultados</h3>
                <p>No hay aprendices que coincidan con "${query}"</p>
            </div>
        `;
    } else {
        const currentAprendices = aprendices;
        aprendices = filtered;
        renderAprendices();
        aprendices = currentAprendices;
    }
});

// Cerrar modal al hacer clic fuera
document.getElementById('modalOverlay').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

// Inicializar
renderAprendices();



//Modal de eliminacion de aprendiz

function Delete(){
    document.querySelector('.eliminar').classList.add('active');
}
function cancel(){
    document.querySelector('.eliminar').classList.remove('active');
}
function OpenDelete(event){
    document.querySelector('.eliminar').classList.add('active')
    const boton = event.currentTarget
    const nombre = boton.getAttribute('data-nombre')
    const url = boton.getAttribute('data-url')

    document.getElementById('formulario').action = url
    document.getElementById('texto').textContent = `Estas seguro de eliminar a "${nombre}"` 
}
function Close(event){
    if (event.target === event.currentTarget) {
        document.querySelector('.eliminar').classList.remove('active');
    }
}
//Edicion de aprendiz//
function OpenEdicion(event){
    event.preventDefault()
    const boton = event.currentTarget   
    document.getElementById('modalOverlay').classList.add('active');

    const botones = document.querySelector('.botones')
    const formulario = document.getElementById('aprendizForm')

    formulario.action = boton.getAttribute('data-ruta') 
    
    const btn_cancelar = document.createElement('button')
    btn_cancelar.textContent = 'Cancelar'
    btn_cancelar.type = 'button'
    btn_cancelar.className = 'btn-secondary'
    
    const btn_editar = document.createElement('button')
    btn_editar.textContent = 'Editar'
    btn_editar.type = 'submit'
    btn_editar.className = 'btn-primary'
    
    botones.appendChild(btn_cancelar)
    botones.appendChild(btn_editar)
    btn_cancelar.addEventListener('click', function(){
        botones.innerHTML = ''
        formulario.action = ''
        document.getElementById('modalOverlay').classList.remove('active');
    })
    
    document.getElementById('nombres').value = boton.getAttribute('data-nombre')
    document.getElementById('apellidos').value = boton.getAttribute('data-apellido')
    document.getElementById('documento').value = boton.getAttribute('data-numero-id')
    document.getElementById('tipoDocumento').value = boton.getAttribute('data-tipo-id')
    document.getElementById('programa').value = boton.getAttribute('data-formacion')
    document.getElementById('email').value = boton.getAttribute('data-email')
    document.getElementById('ficha').value = boton.getAttribute('data-ficha')
    document.getElementById('telefono').value = boton.getAttribute('data-telefono')
}




        