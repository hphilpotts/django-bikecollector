# Generated by Django 4.1.1 on 2022-09-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_accessory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessory',
            old_name='item',
            new_name='kit',
        ),
    ]
