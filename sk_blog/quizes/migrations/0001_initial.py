# Generated by Django 3.1.1 on 2021-03-30 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('correct', models.BooleanField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('answer1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer1', to='quizes.answer')),
                ('answer2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer2', to='quizes.answer')),
                ('answer3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer3', to='quizes.answer')),
                ('answer4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer4', to='quizes.answer')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('questions', models.ManyToManyField(related_name='questions', to='quizes.Question')),
            ],
        ),
    ]
