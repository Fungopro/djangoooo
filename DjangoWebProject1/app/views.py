"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import redirect, render_to_response
from django.views.generic import TemplateView
import app.forms
from app.models import UserNews, Likes, Quest, QuestAns
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
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


@login_required()
def addnews(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        art = UserNews.objects.model()
        art.art_active = False
        art.art_author = request.user.username
        art.art_date = datetime.now()
        art.art_likes = 0
        art.art_text = request.POST.get("art_text")
        art.art_title = request.POST.get("art_title")
        art.save()

    return render(
        request,
        'app/addNews.html',
        {
            'form': app.forms.NewNews,
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def signup(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        user = User.objects.create_user(request.POST.get("username"), request.POST.get('email'),
                                        request.POST.get('password'))
        user.is_staff = False
        user.save()
    return render(
        request,
        'app/signup.html',
        {
            'form': app.forms.SignUpForm,
            'title': 'Registration',
            'year': datetime.now().year,
        }
    )
