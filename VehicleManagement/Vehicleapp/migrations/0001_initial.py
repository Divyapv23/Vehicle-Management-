# Generated by Django 4.2.1 on 2023-08-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('v_type', models.CharField(
                    choices=[('Two', 'Two Wheeler'), ('Three', 'Three Wheeler'), ('Four', 'Four Wheeler')],
                    max_length=10)),
                ('model', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]