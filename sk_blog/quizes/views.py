from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import login_required
from .models import Answer
from .models import Question
from .models import Quiz
from .models import QuizSerializer
from .models import Result


@login_required
def quiz_create_view(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']

        if name and description:
            user = request.user
            quiz = Quiz.objects.create(name=name, description=description, author=user)
            quiz.save()
            return redirect('quizes:list')
        else:
            context = {'errorMsg': 'None of the fields should be empty'}
            return render(request, 'quizes/create.html', context=context)
    else:
        return render(request, 'quizes/create.html')


def quiz_list_view(request):
    quizes = Quiz.objects.all()
    context = {'quizes': quizes}
    return render(request, 'quizes/list.html', context=context)


@login_required
def quiz_detail_view(request, quizname):
    name = quizname.replace("%20", " ")
    quiz = Quiz.objects.filter(name=name).first()
    context = {'quiz': quiz}
    return render(request, 'quizes/detail.html', context=context)


@login_required
def quiz_delete_view(request, quizname):
    name = quizname.replace("%20", " ")
    quiz = Quiz.objects.filter(name=name).first()
    if request.method == "POST" and quiz:
        quiz.delete()
        return redirect('quizes:list')
    else:
        return render(request, 'quizes/delete_quiz.html')


@login_required
def quiz_update_view(request, quizname):
    name = quizname.replace("%20", " ")
    quiz = Quiz.objects.filter(name=name).first()
    context = {'quiz': quiz}
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']

        if name and description:
            quiz.name = name
            quiz.description = description
            quiz.save()
            return redirect('quizes:list')
        else:
            context['errorMsg'] = 'None of the fields should be empty'
            return render(request, 'quizes/update_quiz.html', context=context)
    else:
        return render(request, 'quizes/update_quiz.html', context=context)


@login_required
def quiz_question_view(request, quizname):
    name = quizname.replace("%20", " ")
    context = {}
    quiz = Quiz.objects.filter(name=name).first()
    context['quizname'] = quiz.name
    if request.method == "POST":
        number = request.POST['number']
        question = request.POST['question']

        if number and question:
            user = request.user
            question = Question.objects.create(number=number, question=question, quiz=name, author=user)
            quiz.questions.add(question)
            quiz.save()
            return redirect('quizes:detail', quizname=name)
        else:
            context['errorMsg'] = 'Your title and content cannot be empty'
            return render(request, 'quizes/question.html', context=context)
    else:
        return render(request, 'quizes/question.html', context=context)


@login_required
def quiz_question_delete_view(request, quizname, questionID):
    name = quizname.replace("%20", " ")
    quiz = Quiz.objects.filter(name=name).first()
    context = {'quiz': quiz}
    question = quiz.questions.filter(number=questionID).first()
    if request.method == "POST":
        question.delete()
        return redirect('quizes:detail', quizname=quiz.name)
    else:
        return render(request, 'quizes/delete_question.html', context=context)


@login_required
def quiz_question_update_view(request, quizname, questionID):
    name = quizname.replace("%20", " ")
    context = {}
    quiz = Quiz.objects.filter(name=name).first()
    question = quiz.questions.filter(number=questionID).first()
    context['question'] = question
    if request.method == "POST":
        number = request.POST['number']
        questiontxt = request.POST['question']

        if number and questiontxt:
            question.number = number
            question.question = questiontxt
            question.save()
            return redirect('quizes:detail', quizname=quiz.name)
        else:
            context['errorMsg'] = 'Your title and content cannot be empty'
            return render(request, 'quizes/update_question.html', context=context)
    else:
        return render(request, 'quizes/update_question.html', context=context)


@login_required
def quiz_answer_view(request, quizname, questionID):
    name = quizname.replace("%20", " ")
    context = {}
    quiz = Quiz.objects.filter(name=name).first()
    question = quiz.questions.filter(number=questionID).first()
    context['question'] = question
    if request.method == "POST":
        answertxt = request.POST['answer']
        number = request.POST['number']
        correct = request.POST.get('correct', '') == 'on'

        if answertxt and number:
            user = request.user
            answer = Answer.objects.create(number=number, answer=answertxt, correct=correct, author=user)
            question.answers.add(answer)
            question.save()
            return redirect('quizes:detail', quizname=name)
        else:
            context['errorMsg'] = 'Your title and content cannot be empty'
            return render(request, 'quizes/answer.html', context=context)
    else:
        return render(request, 'quizes/answer.html', context=context)


@login_required
def quiz_answer_delete_view(request, quizname, questionID, answerID):
    name = quizname.replace("%20", " ")
    quiz = Quiz.objects.filter(name=name).first()
    context = {'quiz': quiz}
    question = quiz.questions.filter(number=questionID).first()
    answer = question.answers.filter(number=answerID).first()
    if request.method == "POST":
        answer.delete()
        return redirect('quizes:detail', quizname=quiz.name)
    else:
        return render(request, 'quizes/delete_answer.html', context=context)


@login_required
def quiz_answer_update_view(request, quizname, questionID, answerID):
    name = quizname.replace("%20", " ")
    context = {}
    quiz = Quiz.objects.filter(name=name).first()
    question = quiz.questions.filter(number=questionID).first()
    answer = question.answers.filter(number=answerID).first()
    context['quiz'] = quiz.name
    context['answer'] = answer
    if request.method == "POST":
        answertxt = request.POST['answer']
        number = request.POST['number']
        correct = request.POST.get('correct', '') == 'on'

        if answertxt and number:
            answer.number = number
            answer.answer = answertxt
            answer.correct = correct
            answer.save()
            return redirect('quizes:detail', quizname=quiz.name)
        else:
            context['errorMsg'] = 'Your title and content cannot be empty'
            return render(request, 'quizes/update_answer.html', context=context)
    else:
        return render(request, 'quizes/update_answer.html', context=context)


@login_required
def quiz_play_view(request, quizname):
    name = quizname.replace("%20", " ")
    context = {}
    quiz = Quiz.objects.filter(name=name).first()
    quiz_pic = quiz.name.lower()
    serializer = QuizSerializer(quiz)
    data = JSONRenderer().render(serializer.data)
    context['quiz_pic'] = quiz_pic
    context['quiz'] = quiz
    context['quiz_json'] = data.decode()

    if request.method == "POST":
        user = request.user
        maxpoint = request.POST['result-maxpoint']
        result = request.POST['result-result']
        comment = request.POST['result-comment']

        result = Result.objects.create(quiz=quiz.name, maxpoint=maxpoint, result=result, comment=comment, player=user)
        return redirect('quizes:result', id=result.id)
    else:
        return render(request, 'quizes/play.html', context=context)


@login_required
def quiz_result_view(request, id):
    context = {}
    result = Result.objects.filter(id=id).first()
    context['result'] = result
    context['quiz_pic'] = result.quiz.lower()
    return render(request, 'quizes/result.html', context=context)


@login_required
def quiz_result_delete_view(request, id):
    result = Result.objects.filter(id=id).first()
    if request.method == "POST":
        result.delete()
        return redirect('accounts:results', username=result.player)
    else:
        return render(request, 'quizes/delete_result.html')



