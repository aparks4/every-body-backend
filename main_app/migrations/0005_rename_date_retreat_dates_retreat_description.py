# Generated by Django 4.2.4 on 2023-08-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_retreat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retreat',
            old_name='date',
            new_name='dates',
        ),
        migrations.AddField(
            model_name='retreat',
            name='description',
            field=models.TextField(max_length=2500, null=True),
        ),
    ]
