# Generated by Django 3.2.7 on 2021-11-09 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notesmodel',
            old_name='description',
            new_name='body',
        ),
    ]
