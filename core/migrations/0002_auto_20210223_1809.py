# Generated by Django 3.1.6 on 2021-02-23 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['name']},
        ),
    ]
