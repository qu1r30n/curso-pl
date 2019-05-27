# Generated by Django 2.2.1 on 2019-05-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('cumpleaños', models.DateField(blank=True, null=True)),
                ('chequeo', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
