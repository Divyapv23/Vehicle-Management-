# Generated by Django 4.2.1 on 2023-08-03 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicleapp', '0003_adminlogin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
