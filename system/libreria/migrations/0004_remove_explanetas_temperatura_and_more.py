# Generated by Django 4.1 on 2022-10-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_remove_explanetas_masa_remove_explanetas_radio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explanetas',
            name='temperatura',
        ),
        migrations.AddField(
            model_name='explanetas',
            name='constelacion',
            field=models.CharField(default=1, max_length=100, verbose_name='Constelación'),
            preserve_default=False,
        ),
    ]
