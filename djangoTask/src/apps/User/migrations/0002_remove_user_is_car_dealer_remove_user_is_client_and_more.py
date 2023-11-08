# Generated by Django 4.2.7 on 2023-11-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_car_dealer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_supplier',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('none', 'NONE'), ('client', 'CLIENT'), ('car_dealer', 'CAR_DEALER'), ('supplier', 'SUPPLIER')], default='none', max_length=10),
        ),
    ]