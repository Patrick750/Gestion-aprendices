from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class EmailBackend(ModelBackend):
    def authenticate(self, request=None, documento=None, contraseña=None, **kwargs):
        try:
            user = Usuario.objects.get(numero_documento=documento)
            if user.check_password(contraseña):
                return user
        except Usuario.DoesNotExist:
            print(f"❌ No existe")
            return None

