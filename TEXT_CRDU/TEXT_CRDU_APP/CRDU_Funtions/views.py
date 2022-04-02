from django.shortcuts import render
from .models import Words


def Homepage(request, *args, **kwargs):
    words = Words.objects.all()
    return render(request=request,
                  template_name="index.html",
                  context={'words': words})

def add_word(request, word):
    word_obj = Words.objects.create(word=word)
    word_obj.save()
    return Homepage(request)

def update_word(request, pre_word_id, new_word):
    word_obj = Words.objects.get(pk=int(pre_word_id))
    word_obj.word = new_word
    word_obj.save()
    return Homepage(request)



def dlt_word(request, word_id):
    Words.objects.get(pk=int(word_id)).delete()
    return Homepage(request)