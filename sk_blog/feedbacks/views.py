from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Feedback


@login_required
def feedback_create_view(request):
    context = {}
    if request.method == "POST":
        rating = request.POST.get('rating').split('_')[0]
        description = request.POST.get('rating').split('_')[1]
        content = request.POST['feedback']

        if content or rating:
            user = request.user
            feedback = Feedback.objects.create(rating=rating, description=description, content=content, author=user)
            feedback.save()
            return redirect('feedbacks:created')
        else:
            context['errorMsg'] = 'Feedback or rating should be left'
            return render(request, 'feedbacks/create.html', context=context)
    else:
        return render(request, 'feedbacks/create.html', context=context)


def feedback_created_view(request):
    return render(request, 'feedbacks/created.html')


@login_required
def feedback_delete_view(request, id):
    feedback = Feedback.objects.filter(id=id).first()
    context = {'feedback': feedback}
    if request.method == "POST":
        feedback.delete()
        return redirect('accounts:feedbacks', username=feedback.author)
    else:
        return render(request, 'feedbacks/delete.html', context=context)

