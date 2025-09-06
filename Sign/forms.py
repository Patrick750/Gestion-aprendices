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
            'id':'nombres',
            'required':'true'
        })
    )
    
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'apellidos',
            'required':'true'
        })
    )
    
    documento = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-input',
            'type':'text',
            'id':'documento',
            'required':'true'
        })
    )
        
    
   
