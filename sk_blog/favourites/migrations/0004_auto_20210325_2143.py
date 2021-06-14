# Generated by Django 2.1.2 on 2021-03-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0003_auto_20210324_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='series',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='favourite',
            name='writer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
