# Generated by Django 3.1.5 on 2021-03-15 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='User',
            new_name='user',
        ),
    ]
