# Generated by Django 5.0.2 on 2024-07-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=15)),
                ('position', models.CharField(choices=[('Front-End', 'Front-End'), ('Back-End', 'Back-End'), ('Full_Stack', 'Full Stack')], max_length=20)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]