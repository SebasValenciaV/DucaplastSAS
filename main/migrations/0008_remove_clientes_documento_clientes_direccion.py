# Generated by Django 4.2.10 on 2024-03-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='documento',
        ),
        migrations.AddField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(default='', max_length=200),
        ),
    ]
