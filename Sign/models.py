from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField, BooleanField, IntField, ListField, ReferenceField, EmbeddedDocumentField, URLField, EmailField, fields
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
import re

class Usuario(Document):
    
    # Información personal
    numero_documento = StringField(required=True, unique=True, max_length=20)
    tipo_documento = StringField(
        required=True, 
        choices=['CC', 'TI', 'CE', 'PAS'], 
        default='CC'
    )
    nombres = StringField(required=True, max_length=100)
    apellidos = StringField(required=True, max_length=100)
    email = EmailField()
    telefono = StringField(max_length=15)
    contraseña = StringField(max_length=15, requeired=True)
    rol = StringField(requered=True, 
        choices=['ADMINISTRADOR', 'APRENDIZ', 'INSTRUCTOR', 'COORDINADOR'], 
        default='APRENDIZ'  
    )
    
    # Información académica
    codigo_estudiante = fields.StringField(required=True, unique=True, max_length=20)
    formacion = fields.StringField(required=True, max_length=100)
    estado = fields.StringField(
        choices=['ACTIVO', 'INACTIVO', 'GRADUADO', 'RETIRADO'], 
        default='ACTIVO'
    )
    
    # Información adicional
    foto_url = URLField()
    fecha_registro = DateTimeField(default=datetime.now)
    activo = BooleanField(default=True)
    
    def set_password(self, raw_password):
        """Hashea y establece la contraseña del estudiante"""
        self.validar_password(raw_password)
        self.password = make_password(raw_password)
        self.fecha_cambio_password = datetime.now()
        self.debe_cambiar_password = False
        self.intentos_fallidos = "0"
        self.bloqueado_hasta = None
    
    def check_password(self, raw_password):
        """Verifica la contraseña"""
        return check_password(raw_password, self.password)
    
    def validar_password(self, password):
        """Valida requisitos de seguridad de la contraseña"""
        errores = []
        
        if len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres")
        
        if not re.search(r"[A-Z]", password):
            errores.append("Debe contener al menos una letra mayúscula")
        
        if not re.search(r"[a-z]", password):
            errores.append("Debe contener al menos una letra minúscula")
        
        if not re.search(r"\d", password):
            errores.append("Debe contener al menos un número")
        
        if errores:
            raise ValidationError(errores)


class RegistroAcceso(Document):
    """Modelo para registrar ingresos y salidas de estudiantes"""
    
    # Relación con estudiante
    estudiante = fields.ReferenceField(Usuario, required=True)
    
    # Información del acceso
    tipo_acceso = fields.StringField(
        required=True,
        choices=['INGRESO', 'SALIDA'],
        default='INGRESO'
    )
    fecha_hora = fields.DateTimeField(required=True, default=datetime.now)
    
    # Ubicación del acceso
    ubicacion = fields.StringField(
        required=True,
        choices=[
            'ENTRADA_PRINCIPAL',
            'ENTRADA_BIBLIOTECA', 
            'ENTRADA_CAFETERIA',
            'ENTRADA_PARQUEADERO'
        ],
        default='ENTRADA_PRINCIPAL'
    )
    
    # Método de identificación
    metodo_identificacion = fields.StringField(
        choices=['TARJETA_RFID', 'CODIGO_QR', 'BIOMETRICO', 'MANUAL'],
        default='TARJETA_RFID'
    )
    
    # Información adicional
    dispositivo_id = fields.StringField(max_length=50)  # ID del dispositivo que registró
    observaciones = fields.StringField(max_length=500)
    autorizado_por = fields.StringField(max_length=100)  # En caso de acceso manual
    
    # Estado del registro
    procesado = fields.BooleanField(default=True)
    


class SesionAcceso(EmbeddedDocument):
    
    ingreso = fields.DateTimeField(required=True)
    salida = fields.DateTimeField()
    duracion_minutos = fields.IntField()



class ResumenDiario(Document):
    """Modelo para almacenar resúmenes diarios de acceso"""
    
    fecha = fields.DateTimeField(required=True)
    estudiante = fields.ReferenceField(Usuario, required=True)
    
    # Estadísticas del día
    total_ingresos = fields.IntField(default=0)
    total_salidas = fields.IntField(default=0)
    tiempo_total_minutos = fields.IntField(default=0)
    primera_entrada = fields.DateTimeField()
    ultima_salida = fields.DateTimeField()
    
    # Sesiones del día
    sesiones = fields.ListField(fields.EmbeddedDocumentField(SesionAcceso))
    
    # Ubicaciones visitadas
    ubicaciones_visitadas = fields.ListField(fields.StringField())
    
    meta = {
        'collection': 'resumenes_diarios',
        'indexes': [
            'fecha',
            'estudiante',
            ('estudiante', 'fecha')
        ]
    }
    