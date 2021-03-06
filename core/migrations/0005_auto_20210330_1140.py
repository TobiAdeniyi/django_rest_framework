# Generated by Django 3.1.6 on 2021-03-30 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210225_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.customer'),
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
