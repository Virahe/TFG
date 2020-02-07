from django.shortcuts import render
from .models import Passage


def home(request):
    context = {
        'passages': Passage.objects.all()[:10]
    }
    return render(request, 'logscope/home.html', context)
