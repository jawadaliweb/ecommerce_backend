# Generated by Django 4.1.1 on 2022-10-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custmer_id',
            new_name='custmer',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
