from django.contrib import admin
from .models import Quiz
from .models import Result
from .models import Question
from .models import Answer


admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Quiz)

