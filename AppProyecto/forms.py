from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from AppProyecto.models import Productos

class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita la Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Ingrese su contraseña actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Ingrese una nueva contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita la nueva contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class FormularioNuevoProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('usuario', 'titulo', 'producto', 'marca', 'descripcion', 'precio', 'telefono', 'email', 'imagen_del_producto')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class ActualizacionProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('titulo', 'producto', 'marca', 'descripcion','precio', 'telefono', 'email', 'imagen_del_producto')

        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }