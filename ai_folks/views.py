from django.shortcuts import render
from scholar.models import Scholar


def index(request):
    context = {'scholars': Scholar.objects.filter(classification = 'artificial intellgience').order_by("rank")}
    context['asc'] = True
    context['rank'] = True
    context['data_set'] = 'field/artificial intellgience'
    return render(request, "ai_index.html", context)
