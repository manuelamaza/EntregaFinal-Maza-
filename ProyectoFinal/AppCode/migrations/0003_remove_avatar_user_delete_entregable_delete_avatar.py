# Generated by Django 4.2.6 on 2023-10-23 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCode', '0002_rename_entreglable_entregable_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
