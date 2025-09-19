from django.shortcuts import render,redirect
from . forms import user, aprendices
from . models import Usuario
from django.views.decorators.csrf import csrf_protect
from django.db import transaction
# Create your views here.

@transaction.atomic
@csrf_protect
def admin_sign(request):
    form = user()
    formulario = {
        'nombre':form['nombre'],
        'apellido':form['apellido'],
        'correo':form['correo'],
        'documento':form['documento'],
        'contraseña':form['contraseña'],
        'confirmacion_contraseña':form['confirmacion_contraseña']
    }
    if request.method == 'GET':
        return render(request, 'sign.html',formulario)
    else:
        valores = user(request.POST) 
        if valores.is_valid():
            print("✅Formulario valido")
            try:
                documento =  valores.cleaned_data["documento"].strip()
                contraseña =  valores.cleaned_data["contraseña"].strip()
                confirmacion_contraseña =  valores.cleaned_data["confirmacion_contraseña"].strip()

                if contraseña == confirmacion_contraseña:
                    with transaction.atomic():
                        if Usuario.objects(numero_documento=documento).first() is not None:
                            formulario['error'] = 'El aprendiz ya se encuentra registrado' 
                            return render(request, 'sign.html', formulario)
                        
                        estudiante = Usuario()
                        estudiante.numero_documento = documento
                        estudiante.nombres = valores.cleaned_data["nombre"].strip()
                        estudiante.apellidos = valores.cleaned_data["apellido"].strip()
                        estudiante.email = valores.cleaned_data["correo"].lower().strip()
                        estudiante.codigo_estudiante = documento.strip()
                        estudiante.rol = 'ADMINISTRADOR'
                        estudiante.set_password(contraseña)
                        estudiante.save()
                        print("✅Estudiante registrado:", estudiante.nombres) 
                        return redirect('home')
                else:
                    formulario['error'] = 'Las contraseñas deben coincidir'  
                    return render(request, 'sign.html',formulario)
                authenticated_user = authenticate(
                    request,
                    documento=documento,
                    contraseña=contraseña
                )

                if authenticated_user:
                    print(f"🔑 Autenticación exitosa para: {documento}")
                    login(request, authenticated_user)
                    print(f"🚀 Redirigiendo al dashboard...")
                    return redirect('/index')
                else:
                    print(f"❌ Error en autenticación automática")
                    return redirect('/log_in')
            except Exception as e:
                print(e)
                formulario['error'] = 'Error al registrar el estudiante'
                return render(request, 'sign.html',formulario)


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

@transaction.atomic
def gention_aprendices(request):
    informacion = Usuario.objects.filter(rol="APRENDIZ")
    usuarios = aprendices()
    contexto = {
                'nombres':usuarios['nombres'],
                'apellidos':usuarios['apellidos'],
                'documento':usuarios['documento'],
                'tipo_documento':usuarios['tipo_documento'],
                'formaciones':usuarios['formacion'],
                'ficha':usuarios['ficha'],
                'telefono':usuarios['telefono'],
                'email':usuarios['email'],
                'estado':usuarios['estado'],
                'datos':informacion
    }
    if request.method == 'POST':
        datos = aprendices(request.POST)
        if datos.is_valid():
            print('✅Formulario validado')
            try:
                documento = datos.cleaned_data["documento"].strip()
                if Usuario.objects(numero_documento=documento).first() is not None:
                    contexto['error'] = 'El aprendiz ya existe'
                    return render(request, 'lista_aprendices.html',contexto)
                registro = Usuario()
                registro.numero_documento = documento
                registro.tipo_documento = datos.cleaned_data["tipo_documento"]
                registro.nombres = datos.cleaned_data["nombres"].strip()
                registro.apellidos = datos.cleaned_data["apellidos"].strip()
                registro.email = datos.cleaned_data["email"].lower().strip()
                registro.telefono = datos.cleaned_data["telefono"].strip()
                registro.codigo_estudiante = documento
                registro.formacion = datos.cleaned_data["formacion"]
                registro.ficha = datos.cleaned_data["ficha"].strip()
                registro.save()
                print('✅Aprendiz registrado')
                return render(request,"lista_aprendices.html",contexto)
            except Exception as e:
                    print(f'❌ Error al guardar aprendiz: {e}')
        else:
            print('❌Formulario no valido')
            contexto['datos'] = informacion
            return render(request, "lista_aprendices.html",contexto)
    else:
        if len(informacion) == 0:
            contexto['cantidad'] = 0
            contexto['datos'] = informacion
            contexto['vacio'] = 'No hay aprendices registrados'
            return render(request, "lista_aprendices.html", contexto)
        else:
            return render(request, "lista_aprendices.html",contexto)

def eliminar(request, documento):
    if request.method != 'POST':
        return redirect('eliminar_aprendiz')
    try:
        aprendiz = Usuario.objects(numero_documento = documento)
        if aprendiz:
            aprendiz.delete()
    except Exception as e:
        print(e)
    return redirect('list_aprendises')


def editar_aprendiz(request, documento):
    if request.method != 'POST':
        return redirect('editar_aprendiz')
    
    form = aprendices(request.POST)
    if form.is_valid():
        print('✅ Formulario valido')
        try:
            aprendiz = Usuario.objects.get(numero_documento = documento)
            aprendiz.tipo_documento = form.cleaned_data['tipo_documento']
            aprendiz.nombres = form.cleaned_data['nombres']
            aprendiz.apellidos = form.cleaned_data['apellidos']
            aprendiz.email = form.cleaned_data['email']
            aprendiz.telefono = form.cleaned_data['telefono']
            aprendiz.formacion = form.cleaned_data['formacion']
            aprendiz.ficha = form.cleaned_data['ficha']
            aprendiz.estado = form.cleaned_data['estado']
            aprendiz.save()
            print(f'✅ edicion exitosa {aprendiz.nombres}')
            return redirect('list_aprendises')
        except Exception as e:
            print(f'❌Error al editar {e}')
    