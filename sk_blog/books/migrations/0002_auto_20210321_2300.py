# Generated by Django 2.1.2 on 2021-03-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
