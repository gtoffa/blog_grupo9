# Generated by Django 4.2.7 on 2023-12-14 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('Colaborador', 'Colaborador'), ('Miembro', 'Miembro'), ('Superusuario', 'Superusuario')], default='Miembro', max_length=20),
        ),
    ]
