// Variables para simular datos dinámicos
let stats = {
    presentes: 0,
    ingresos: 0,
    salidas: 0,
    alertas: 0
};

// Funciones de navegación
function navigateTo(section) {
    console.log(`Navegando a: ${section}`);
    // Aquí implementarías la navegación real
    switch(section) {
        case 'ingreso':
            alert('Redirigiendo al módulo de Registro de Ingreso');
            break;
        case 'salida':
            alert('Redirigiendo al módulo de Registro de Salida');
            break;
        case 'aprendices':
            alert('Redirigiendo al módulo de Gestión de Aprendices');
            break;
        case 'reportes':
            alert('Redirigiendo al módulo de Reportes');
            break;
        case 'acceso':
            alert('Redirigiendo al módulo de Control de Acceso');
            break;
        case 'notificaciones':
            alert('Redirigiendo al módulo de Notificaciones');
            break;
    }
}

// Actualizar estadísticas en tiempo real (simulado)
function updateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    // Simular cambios aleatorios pequeños
    if(Math.random() > 0.7) {
        const randomStat = Math.floor(Math.random() * 4);
        const change = Math.floor(Math.random() * 3) - 1; // -1, 0, o 1
        
        switch(randomStat) {
            case 0:
                stats.presentes = Math.max(0, stats.presentes + change);
                statNumbers[0].textContent = stats.presentes;
                break;
            case 1:
                stats.ingresos = Math.max(0, stats.ingresos + Math.abs(change));
                statNumbers[1].textContent = stats.ingresos;
                break;
            case 2:
                stats.salidas = Math.max(0, stats.salidas + Math.abs(change));
                statNumbers[2].textContent = stats.salidas;
                break;
            case 3:
                stats.alertas = Math.max(0, stats.alertas + change);
                statNumbers[3].textContent = stats.alertas;
                break;
        }
    }
}

// Actualizar estadísticas cada 10 segundos
setInterval(updateStats, 10000);

// Agregar efecto de hover dinámico a las tarjetas
document.querySelectorAll('.dashboard-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Mostrar hora actual
function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('es-CO');
    console.log(`Hora actual: ${timeString}`);
}

setInterval(updateTime, 1000);

function showLogoutModal(){
    document.getElementById('logoutModal').classList.add('active');
}

function closeModal(event){
    if (event.target === event.currentTarget) {
        document.getElementById('logoutModal').classList.remove('active');
    }
}
function cancelLogout(){
    document.getElementById('logoutModal').classList.remove('active');
}