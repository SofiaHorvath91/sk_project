# Generated by Django 3.1.1 on 2021-04-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0005_quiz_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='questions', to='quizes.Question'),
        ),
    ]
