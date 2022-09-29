# Generated by Django 4.1 on 2022-09-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userandpassword',
            name='nickname',
        ),
        migrations.AddField(
            model_name='userandpassword',
            name='apodo',
            field=models.CharField(default=1, max_length=100, verbose_name='Apodo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='explanetas',
            name='descubrimiento',
            field=models.CharField(max_length=100, verbose_name='Descubrimiento'),
        ),
        migrations.AlterField(
            model_name='explanetas',
            name='masa',
            field=models.CharField(max_length=100, verbose_name='Masa'),
        ),
        migrations.AlterField(
            model_name='explanetas',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='explanetas',
            name='radio',
            field=models.CharField(max_length=100, verbose_name='Radio'),
        ),
        migrations.AlterField(
            model_name='userandpassword',
            name='apellido',
            field=models.CharField(max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='userandpassword',
            name='correo',
            field=models.CharField(max_length=100, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='userandpassword',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
