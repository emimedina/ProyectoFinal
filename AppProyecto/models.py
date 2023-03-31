from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Productos(models.Model):
    productoSeleccion = (
      ('zapatillas deportivas','Zapatillas Deportivas'),
      ('zapatillas urbanas', 'Zapatillas Urbanas'),
      ('botas', 'Botas'),
      ('tacos', 'Tacos'),
   
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #almacena la relacion entre el objeto y el usuario que lo crea
    titulo = models.CharField(max_length=200)
    producto = models.CharField(max_length=30, choices=productoSeleccion, default='zapatillas deportivas')
    marca = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefono = models.IntegerField()
    email = models.EmailField()
    imagen_del_producto = models.ImageField(upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
