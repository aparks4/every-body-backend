# Generated by Django 4.1.1 on 2023-04-02 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='img',
            new_name='image',
        ),
    ]
