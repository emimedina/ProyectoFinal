from django.shortcuts import redirect, render
from AppProyecto.models import Productos
from django.http import HttpResponse
from AppProyecto.forms import FormularioNuevoProducto, ActualizacionProducto, FormularioRegistroUsuario, FormularioEdicion, FormularioCambioPassword
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.



class Inicio(LoginRequiredMixin, TemplateView):  #clase para mostrar el inicio
    template_name = 'inicio.html'

@login_required
def sobreNosotros(request):
    return render(request, 'sobreNosotros.html', {})


class Login(LoginView): #clase para loguear a los usuarios ya registrados
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

class Registro(FormView):   #clase para realizar el registro de usuarios
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):  #con esta funcion si el formulario es valido se guarda en la base de datos
        user2 = form.save()
        return super().form_valid(form)


class UsuarioEdicion(LoginRequiredMixin, UpdateView):  #clase para actualizar el usuario
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):  #con la funcion get_object se obtiene el objeto usuario actual
        return self.request.user  # self.request.user se utiliza para recuperar el usuario actualmente autenticado y se devuelve como el objeto que se va a editar.

class CambioPassword(PasswordChangeView):  #clase para cambiar la contraseña del usuario
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('inicio')


@login_required
def productos(request):
    return render(request, 'productos.html')

#Creacion del producto
class ProductoCreacion(LoginRequiredMixin, CreateView):
    model = Productos
    form_class = FormularioNuevoProducto
    success_url = reverse_lazy('inicio')
    template_name = 'productoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user #establece el campo 'user' del modelo productos con el usuario que esta enviando el formulario, es decir self.request.user
        return super(ProductoCreacion, self).form_valid(form) #valida los datos y luego los guarda(creo)

#ZAPATILLAS DEPORTIVAS

class ZapatillasDeportivasLista(LoginRequiredMixin, ListView):
    context_object_name = 'zapatillasdeportivas'#filtra del atributo producto los objetos que comienzan con la cadena 'zapatillas deportivas'
    queryset = Productos.objects.filter(producto__startswith='zapatillas deportivas')
    template_name = 'listaZapatillasDeportivas.html'
    #login_url = '/login/'

class ZapatillasDeportivasDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'zapatillasdeportivas'
    template_name = 'zapatillasDeportivasDetalle.html'

class ZapatillasDeportivasUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizacionProducto
    success_url = reverse_lazy('zapatillas deportivas')
    context_object_name = 'zapatillasdeportivas'
    template_name = 'zapatillasDeportivasEdicion.html'

class ZapatillasDeportivasDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('zapatillas deportivas')
    context_object_name = 'zapatillasdeportivas'
    template_name = 'ZapatillasDeportivasBorrado.html'

#ZAPATILLAS URBANAS

class ZapatillasUrbanasLista(LoginRequiredMixin, ListView):
    context_object_name = 'zapatillasurbanas'
    queryset = Productos.objects.filter(producto__startswith='zapatillas urbanas')
    template_name = 'listaZapatillasUrbanas.html'
    #login_url = '/login/'

class ZapatillasUrbanasDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'zapatillasurbanas'
    template_name = 'zapatillasUrbanasDetalle.html'

class ZapatillasUrbanasUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizacionProducto
    success_url = reverse_lazy('zapatillas urbanas')
    context_object_name = 'zapatillasurbanas'
    template_name = 'zapatillasUrbanasEdicion.html'

class ZapatillasUrbanasDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('zapatillas urbanas')
    context_object_name = 'zapatillasurbanas'
    template_name = 'ZapatillasUrbanasBorrado.html'

#BOTAS

class BotasLista(LoginRequiredMixin, ListView):
    context_object_name = 'botas'
    queryset = Productos.objects.filter(producto__startswith='botas')
    template_name = 'listaBotas.html'


class BotasDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'botas'
    template_name = 'botasDetalle.html'

class BotasUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizacionProducto
    success_url = reverse_lazy('botas')
    context_object_name = 'botas'
    template_name = 'botasEdicion.html'

class BotasDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('botas')
    context_object_name = 'botas'
    template_name = 'botasBorrado.html'

#TACOS

class TacosLista(LoginRequiredMixin, ListView):
    context_object_name = 'tacos'
    queryset = Productos.objects.filter(producto__startswith='tacos')
    template_name = 'listaTacos.html'

class TacosDetalle(LoginRequiredMixin, DetailView):
    model = Productos
    context_object_name = 'tacos'
    template_name = 'tacosDetalle.html'

class TacosUpdate(LoginRequiredMixin, UpdateView):
    model = Productos
    form_class = ActualizacionProducto
    success_url = reverse_lazy('tacos')
    context_object_name = 'tacos'
    template_name = 'tacosEdicion.html'

class TacosDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('tacos')
    context_object_name = 'tacos'
    template_name = 'tacosBorrado.html'