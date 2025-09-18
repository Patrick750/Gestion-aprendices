from django import forms

class user(forms.Form):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'nombre',
            'placeholder':'Nombre'
        })
    )    
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'apellido',
            'placeholder':'Apellido'
        })
    )    
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-input',
            'type':'mail',
            'id':'correo',
            'placeholder':'Correo'
        })
    )    
    documento = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'documento',
            'placeholder':'Documento'
        })
    ) 
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'type':'password',
            'id':'contraseña',
            'placeholder':'••••••••••'
        })
    ) 
    confirmacion_contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-input',
            'type':'password',
            'id':'confirmacion_contraseña',
            'placeholder':'••••••••••'
        })
    ) 

class aprendices(forms.Form):
    nombres = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'nombres'
        })
    )
    
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'apellidos'
        })
    )
    
    documento = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'documento'
        })
    )
    
    opciones_identicaion = [
        ('', 'Tipo de documento'),
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería')
    ]
    tipo_documento = forms.ChoiceField(
        choices=opciones_identicaion,
        widget=forms.Select(attrs={
            'class':'form-select',
            'id':'tipoDocumento'
        })
    )
          
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'tel',
            'id':'telefono'
        })
    )  
          
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-input',
            'type':'email',
            'id':'email'
        })
    )  

    opciones_formaciones = [
        ('', 'Selecciona la formacion'),
        ('ADSO','Análisis y Desarrollo de Software'),
        ('GESTION_EMPRESARIAL', 'Gestión Empresarial'),
        ('MERCADEO', 'Mercadeo y Publicidad'),
        ('CONTABILIDAD', 'Contabilidad y Finanzas'),
        ('SISTEMAS', 'Técnico en Sistemas')
    ]

    formacion = forms.ChoiceField(
        choices=opciones_formaciones,
        widget=forms.Select(attrs={
            'class':'form-select',
            'id':'programa'
        })
    )
              
    ficha = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'ficha'
        })
    )  
         




    
   
