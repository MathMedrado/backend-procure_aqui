# Generated by Django 4.1 on 2022-10-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_user_birth_date_user_city_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
