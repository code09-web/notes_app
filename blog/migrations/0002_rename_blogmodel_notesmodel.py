# Generated by Django 3.2.7 on 2021-11-10 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogModel',
            new_name='NotesModel',
        ),
    ]
