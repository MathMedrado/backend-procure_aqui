# Generated by Django 4.1 on 2022-10-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_is_active_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='campo_qualquer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
