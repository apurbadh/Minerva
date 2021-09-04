from django.shortcuts import redirect, render
from course.models import Course
from .models import Question, Answer

# Create your views here.
def forum(req, id):
    try:
        course =Course.objects.get(id=id)
        if req.user not in course.users.all() and req.user != course.teacher:
            return redirect("/")
    except:
        return redirect('/')
    if req.method == "POST":
        question = req.POST["question"]
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
        course = question.course.id
        try:
            course =Course.objects.get(id=id)
            if req.user not in course.users.all() and req.user != course.teacher:
                return redirect("/")
        except:
            return redirect('/')
    except:
        question = None
        answers = None
    if req.method == "POST":
        answer = req.POST["answer"]
        obj = Answer.objects.create(user=req.user, answer=answer)
        obj.save()
        question.answer.add(obj)
        question.save()
        return redirect("/forum/question/" + str(id))

    context = {
        "question": question,
        "answers":answers
    }
    return render(req, "forum/answer.html", context)