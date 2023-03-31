# Generated by Django 4.0.4 on 2023-03-29 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppProyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'ordering': ['usuario', '-fechaPublicacion']},
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='cantidad_disponible',
            new_name='telefono',
        ),
        migrations.AddField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='fechaPublicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen_del_producto',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AddField(
            model_name='productos',
            name='marca',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='titulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(choices=[('zapatillas deportivas', 'Zapatillas Deportivas'), ('zapatillas urbanas', 'Zapatillas Urbanas'), ('botas', 'Botas'), ('tacos', 'Tacos')], default='zapatillas deportivas', max_length=30),
        ),
    ]
