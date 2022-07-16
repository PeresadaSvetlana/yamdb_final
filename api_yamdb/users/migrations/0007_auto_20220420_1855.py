# Generated by Django 2.2.16 on 2022-04-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220420_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'user'), ('ADMIN', 'admin'), ('MODERATOR', 'moderator')], default='user', max_length=10),
        ),
    ]
