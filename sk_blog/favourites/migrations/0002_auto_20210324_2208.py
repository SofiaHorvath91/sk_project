# Generated by Django 2.1.2 on 2021-03-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='book',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
