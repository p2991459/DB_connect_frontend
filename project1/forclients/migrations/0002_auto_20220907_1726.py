# Generated by Django 3.2.15 on 2022-09-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forclients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Client_name',
        ),
    ]