# Generated by Django 3.1.1 on 2021-04-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0004_auto_20210401_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
