# Generated by Django 4.1.5 on 2023-06-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_alter_factura_cod_despacho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='cod_despacho',
        ),
    ]
