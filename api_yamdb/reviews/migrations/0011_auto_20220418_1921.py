# Generated by Django 2.2.16 on 2022-04-18 16:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0010_auto_20220418_1909'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
    ]
