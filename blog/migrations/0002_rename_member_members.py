# Generated by Django 4.0.5 on 2022-07-06 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='member',
            new_name='Members',
        ),
    ]
