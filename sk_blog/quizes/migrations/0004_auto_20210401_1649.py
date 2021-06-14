# Generated by Django 2.1.2 on 2021-04-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_auto_20210330_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer4',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(related_name='answers', to='quizes.Answer'),
        ),
    ]
