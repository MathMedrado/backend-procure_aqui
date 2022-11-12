# Generated by Django 4.1.1 on 2022-09-22 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_historicprice_price_delete_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicprice',
            old_name='creation_date_historic_price',
            new_name='alteration_date',
        ),
        migrations.RenameField(
            model_name='historicprice',
            old_name='price_historic',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='historicprice',
            name='update_date_historic_price',
        ),
        migrations.AlterField(
            model_name='historicprice',
            name='supermarket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.supermarket'),
        ),
    ]