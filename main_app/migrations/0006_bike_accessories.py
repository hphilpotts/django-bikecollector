# Generated by Django 4.1.1 on 2022-09-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_item_accessory_kit'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='accessories',
            field=models.ManyToManyField(to='main_app.accessory'),
        ),
    ]