# Generated by Django 4.2.7 on 2023-12-08 12:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]