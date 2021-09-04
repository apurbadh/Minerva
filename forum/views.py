import course
from django.shortcuts import redirect, render
from course.models import Course, User
from .decorators import is_enrolled
from .models import Question, Answer

# Create your views here.
def forum(req, id):
    if req.method == "POST":
        question = req.POST["question"]
        course = Course.objects.get(id=id)
        question = Question.objects.create(question=question, quser=req.user, course=course)
        question.save()
        return redirect('/forum/' + str(id))
    questions = Question.objects.all().filter(course=Course.objects.get(id=id))
    context = {
        "questions" : questions
    }
    return render(req, "forum/index.html", context)

def answers(req, id):
    try:
        question = Question.objects.get(id=id)
        answers = question.answer.all()
    except:
        question = None
        answers = None
    context = {
        "question": question,
        "answers":answers
    }
    return render(req, "forum/answer.html", context)