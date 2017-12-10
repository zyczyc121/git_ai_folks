from django.shortcuts import render
from scholar.models import Scholar


def index(request):
    context = {'scholars': Scholar.objects.filter(classification = 'artificial intellgience').order_by("rank")}
    return render(request, "ai_index.html", context)
