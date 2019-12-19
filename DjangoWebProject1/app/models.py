"""
Definition of models.
"""

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from redactor.fields import RedactorField
from .middleware import get_current_user
from ckeditor.fields import RichTextField


# Create your models here.

class UserNews(models.Model):
    class Meta:
        db_table = 'user_news'

    art_title = models.CharField(default="", max_length=254)
    art_text = RichTextField(default='`')
    art_date = models.DateTimeField(default=now)
    art_likes = models.IntegerField(default=0)
    art_author = models.CharField(default=get_current_user(), max_length=254)
    art_active = models.BooleanField(default=False)


class Likes(models.Model):
    class Meta:
        db_table = 'likes'

    status = models.BooleanField(default=True)
    title = models.ForeignKey(UserNews)
    user = models.ForeignKey(User, default=get_current_user())


class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(
        verbose_name=u'Text',
        # for example, if you downloaded the 'table' plugin:
        redactor_options={'plugins': ['table']}
    )


class SignUpModel(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True


class Quest(models.Model):
    class Meta:
        db_table = 'quest'

    quest = models.CharField(max_length=150, verbose_name=u'Title')


class QuestAns(models.Model):
    class Meta:
        db_table = 'quest_ans'

    answer = models.CharField(max_length=150, verbose_name=u'Title')
    answer_num = models.IntegerField()
    quest_num = models.IntegerField()


class Answer(models.Model):
    class Meta:
        db_table = 'answer'

    user = models.CharField(max_length=150, verbose_name=u'Title')
    group = models.CharField(max_length=150, verbose_name=u'Title')
    answer_num = models.IntegerField()
    quest_num = models.IntegerField()
    time = models.DateTimeField()
