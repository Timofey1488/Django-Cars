# Generated by Django 4.2.7 on 2023-11-08 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Supplier', '0001_initial'),
        ('CarDealer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardealersupplier',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.supplier'),
        ),
    ]