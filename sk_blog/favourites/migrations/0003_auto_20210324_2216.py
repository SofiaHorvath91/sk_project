# Generated by Django 2.1.2 on 2021-03-24 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0002_auto_20210324_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='book',
            new_name='bookname',
        ),
    ]