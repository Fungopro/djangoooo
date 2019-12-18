"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
import app.forms
from app.models import Quest, QuestAns, Answer


def home(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'quest': {"Quest": Quest.objects.all()},
            'answer': Answer.objects.all()
        }
    )


def news(request, quest_id):
    return render(request, "app/news.html", {"quest": Quest.objects.filter(id=quest_id)})


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
        for i in range(1, 14):
            quest = Answer.objects.model()
            quest.id = Answer.objects.count()
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
