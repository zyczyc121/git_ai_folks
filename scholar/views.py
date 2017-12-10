from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from scholar.models import Scholar

def index(request):
    return HttpResponse("Scholar Index Here")
# Create your views here.


def field_rank(request, field = 'data mining'):
    field_dict = {'artificial intellgience': '人工智能', 'machine learning': '机器学习', 'data mining': '数据挖掘', 'computer networking': '计算机网络', 'natural language processing': 'NLP', 'computer graphics': '计算机图形', 'multimedia': '多媒体', 'web-information search': '网络搜索', 'system': '计算机系统', 'database': '数据库', 'security': '计算机安全', 'human-computern interaction': '人机交互', 'software engineering': '软件工程', 'theory': '计算机理论'}
    context = {'scholars': Scholar.objects.filter(classification = field).order_by("rank"), 'listing': field_dict[field]}
    return render(request, 'scholar/list.html', context)

def tag_search(request, tag_name):
    context = {'scholars': Scholar.objects.filter(tag__title__startswith = tag_name), 'listing': "标签: " + tag_name}
    return render(request, 'scholar/list.html', context)

def profile(request, scholar_pk):
    scholar = get_object_or_404(Scholar, id = scholar_pk)
    return render(request, "scholar/index.html", {
        'scholar': scholar,    
    })

def search(request):
    if request.GET.get('search_name'):
        if request.GET['search_name'] != ' ' or request.GET['search_name'] != '.':
            context = {'scholars': Scholar.objects.filter(name__contains = request.GET['search_name']) | Scholar.objects.filter(affiliation__contains = request.GET['search_name']), 'listing': "搜索: " + request.GET['search_name']}
        else:
            context = {}
    else:
        context = {}
    return render(request, 'scholar/list.html', context)

def sort(request):
    context = request.path
    return HttpResponse(context)

def scholar_json(request, scholar_pk):
    data = Scholar.objects.get(id = scholar_pk).focus
    return JsonResponse(data)
