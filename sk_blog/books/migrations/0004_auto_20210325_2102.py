# Generated by Django 3.1.1 on 2021-03-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
