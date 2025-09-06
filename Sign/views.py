from django.shortcuts import render,redirect
from . forms import user, aprendices
from . models import Usuario
from django.views.decorators.csrf import csrf_protect
from django.db import transaction
# Create your views here.

@transaction.atomic
@csrf_protect
def sign(request):
    form = user()
    if request.method == 'GET':
        return render(request, 'sign.html',{
            'nombre':form['nombre'],
            'apellido':form['apellido'],
            'correo':form['correo'],
            'documento':form['documento'],
            'contraseña':form['contraseña'],
            'confirmacion_contraseña':form['confirmacion_contraseña']
        })
    else:
        datos = user(request.POST) 
        if datos.is_valid():
            print("✅Formulario valido")
            try:
                documento =  datos.cleaned_data["documento"].strip()
                contraseña =  datos.cleaned_data["contraseña"].strip()
                confirmacion_contraseña =  datos.cleaned_data["confirmacion_contraseña"].strip()

                if contraseña == confirmacion_contraseña:
                    with transaction.atomic():
                        if Usuario.objects(numero_documento=documento).first() is not None:
                            return render(request, 'sign.html',{
                                'nombre':form['nombre'],
                                'apellido':form['apellido'],
                                'correo':form['correo'],
                                'documento':form['documento'],
                                'contraseña':form['contraseña'],
                                'confirmacion_contraseña':form['confirmacion_contraseña'],
                                'error': 'El aprendiz ya se encuentra registrado'
                            })
                        
                        estudiante = Usuario()
                        estudiante.numero_documento = documento
                        estudiante.nombres = datos.cleaned_data["nombre"].strip()
                        estudiante.apellidos = datos.cleaned_data["apellido"].strip()
                        estudiante.email = datos.cleaned_data["correo"].lower().strip()
                        estudiante.codigo_estudiante = documento.strip()
                        estudiante.formacion = 'Analisis y desarrollo desoftware'
                        estudiante.set_password(contraseña)
                        estudiante.save()
                        print("✅Estudiante registrado:", estudiante.nombres) 
                        return redirect('home')
                else:
                    return render(request, 'sign.html',{
                        'nombre':form['nombre'],
                        'apellido':form['apellido'],
                        'correo':form['correo'],
                        'documento':form['documento'],
                        'contraseña':form['contraseña'],
                        'confirmacion_contraseña':form['confirmacion_contraseña'],
                        'error': 'Las contraseñas deben coincidir'
                    })
                authenticated_user = authenticate(
                    request,
                    documento=documento,
                    contraseña=contraseña
                )

                if authenticated_user:
                    print(f"🔑 Autenticación exitosa para: {documento}")
                    login(request, authenticated_user)
                    messages.success(
                        request, 
                        f'¡Bienvenido {user.nombres}! Tu cuenta ha sido creada exitosamente.'
                    )
                    print(f"🚀 Redirigiendo al dashboard...")
                    return redirect('/index')
                else:
                    print(f"❌ Error en autenticación automática")
                    return redirect('/log_in')
            except Exception as e:
                print(e)
                return render(request, 'sign.html',{
                    'nombre':form['nombre'],
                    'apellido':form['apellido'],
                    'correo':form['correo'],
                    'documento':form['documento'],
                    'contraseña':form['contraseña'],
                    'confirmacion_contraseña':form['confirmacion_contraseña'],
                    'error': 'Error al registrar el estudiante'
                })


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def gention_aprendices(request):
    if request.method == "GET":
        apprentices = aprendices()
        informacion = Usuario.objects.filter(rol="APRENDIZ")
        if len(informacion) == 0:
            return render(request, "lista_aprendices.html",{
                'cantidad': 0,
                'vacio':'No hay aprendices registrados',
                'aprendices':aprendices['nombres']
            })
        else:
            return render(request, "lista_aprendices.html",{
                'datos':informacion,
                'nombres':apprentices['nombres']
            })
