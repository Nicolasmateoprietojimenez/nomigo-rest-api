# Generated by Django 5.0.6 on 2024-08-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_rol', models.CharField(max_length=50)),
                ('permisos', models.TextField()),
            ],
        ),
    ]
