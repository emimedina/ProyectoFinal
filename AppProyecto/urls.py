from django import views
from django.urls import path, include
from AppProyecto import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', views.Registro.as_view(), name='registro'),
    path('editarPerfil/', views.UsuarioEdicion.as_view(), name='editar perfil'),
    path('passwordCambio/', views.CambioPassword.as_view(), name='cambiar password'),
    path('sobreNosotros/', views.sobreNosotros, name='sobre nosotros'),
  

    path('productos', views.productos, name='Productos'),

    path('productoCreacion/', views.ProductoCreacion.as_view(), name='nuevo'),

    path('listaZapatillasDeportivas/', views.ZapatillasDeportivasLista.as_view(), name='zapatillas deportivas'),
    path('zapatillasDeportivasDetalle/<int:pk>/', views.ZapatillasDeportivasDetalle.as_view(), name='zapatillas deportivas detalle'),
    path('zapatillasDeportivasEdicion/<int:pk>/', views.ZapatillasDeportivasUpdate.as_view(), name='zapatillas deportivas edicion'),
    path('zapatillasDeportivasEliminar/<int:pk>/', views.ZapatillasDeportivasDelete.as_view(), name='zapatillas deportivas eliminar'),

    path('listaZapatillasUrbanas/', views.ZapatillasUrbanasLista.as_view(), name='zapatillas urbanas'),
    path('zapatillasUrbanasDetalle/<int:pk>/', views.ZapatillasUrbanasDetalle.as_view(), name='zapatillas urbanas detalle'),
    path('zapatillasUrbanasEdicion/<int:pk>/', views.ZapatillasUrbanasUpdate.as_view(), name='zapatillas urbanas edicion'),
    path('zapatillasUrbanasEliminar/<int:pk>/', views.ZapatillasUrbanasDelete.as_view(), name='zapatillas urbanas eliminar'),

    path('listaBotas/', views.BotasLista.as_view(), name='botas'),
    path('botasDetalle/int:pk/', views.BotasDetalle.as_view(), name='botas detalle'),
    path('botasEdicion/int:pk/', views.BotasUpdate.as_view(), name='botas edicion'),
    path('botasEliminar/int:pk/', views.BotasDelete.as_view(), name='botas eliminar'),

    path('listaTacos/', views.TacosLista.as_view(), name='tacos'),
    path('tacosDetalle/<int:pk>/', views.TacosDetalle.as_view(), name='tacos detalle'),
    path('tacosEdicion/<int:pk>/', views.TacosUpdate.as_view(), name='tacos edicion'),
    path('tacosEliminar/<int:pk>/', views.TacosDelete.as_view(), name='tacos eliminar'),


]   

