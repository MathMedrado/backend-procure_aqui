# Generated by Django 4.1 on 2022-10-11 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%d/%m/%Y'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_visible',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='supermarket',
            field=models.ManyToManyField(null=True, to='product.supermarket'),
        ),
    ]
