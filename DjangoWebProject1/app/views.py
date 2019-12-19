"""
Definition of views.
"""
import datetime

from django.shortcuts import render
from django.http import HttpRequest
import app.forms
from app.models import Quest, QuestAns, Answer


def home(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/result.html',
        {
            'quest': {"Quest": Quest.objects.all()},
            'answer': Answer.objects.all()
        }
    )


def news(request, quest_id):
    return render(request, "app/result.html", {"quest": Quest.objects.filter(id=quest_id)})


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/about.html',
        {
            'quest': {"Quest": Quest.objects.all()},
            'QuestAns': {"QuestAns": QuestAns.objects.all()},
            'form': app.forms.SelectAnswer
        }
    )


def answer(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        for item in Answer.objects.all():
            if item.user == request.POST.get("name"):
                return render(
                    request,
                    'app/contact.html',
                    {

                    }
                )

        for i in range(1, 14):
            quest = Answer.objects.model()
            quest.id = Answer.objects.count()
            quest.group = request.POST.get("group")
            quest.user = request.POST.get("name")
            quest.time = datetime.datetime.now()
            quest.quest_num = str(i)
            quest.answer_num = request.POST.get("ans_" + str(i))
            quest.save()

        return render(
            request,
            'app/about.html',
            {
                'quest': {"Quest": Quest.objects.all()},
                'QuestAns': {"QuestAns": QuestAns.objects.all()},
                'form': app.forms.SelectAnswer
            }
        )
