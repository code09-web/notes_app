# Generated by Django 3.2.7 on 2021-11-09 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20211109_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notesmodel',
            old_name='post_author',
            new_name='owner',
        ),
    ]