# Generated by Django 4.2.7 on 2023-12-13 03:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('resumen', models.CharField(max_length=200, null=True)),
                ('imagenes', models.ImageField(upload_to='noticias')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('cant_vistas', models.IntegerField(default=0)),
            ],
        ),
    ]
