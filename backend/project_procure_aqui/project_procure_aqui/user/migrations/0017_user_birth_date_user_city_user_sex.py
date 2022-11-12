# Generated by Django 4.1 on 2022-10-06 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_is_visible'),
        ('user', '0016_user_campo_qualquer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[('masculine', 'Masculino'), ('feminine', 'feminino'), ('other', 'outro')], max_length=20, null=True),
        ),
    ]
