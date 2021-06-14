from django.db import models
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class Answer(models.Model):
    number = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    correct = models.BooleanField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pass


class AnswerSerializer(serializers.ModelSerializer):
    users = UniqueValidator(queryset=User.objects.all())

    class Meta:
        model = Answer
        fields = '__all__'
        depth = 1


class Question(models.Model):
    quiz = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answer, related_name='answers', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pass


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    users = UniqueValidator(queryset=User.objects.all())

    class Meta:
        model = Question
        fields = '__all__'
        depth = 2


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    users = UniqueValidator(queryset=User.objects.all())

    class Meta:
        model = Quiz
        fields = '__all__'
        depth = 2


class Result(models.Model):
    quiz = models.CharField(max_length=255, blank=True, null=True)
    maxpoint = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)