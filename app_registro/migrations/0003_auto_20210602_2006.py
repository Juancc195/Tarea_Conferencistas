# Generated by Django 3.2.3 on 2021-06-03 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0002_conferencia_fecha_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('experiencia', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='conferencia',
            name='conferencista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_registro.conferencista'),
        ),
    ]
