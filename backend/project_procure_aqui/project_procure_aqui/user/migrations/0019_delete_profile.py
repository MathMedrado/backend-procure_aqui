# Generated by Django 4.1 on 2022-10-15 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_alter_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]