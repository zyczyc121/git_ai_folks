from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from scholar.models import Scholar, Collection

def index(request):
    return HttpResponse("Scholar Index Here")
# Create your views here.


def field_rank(request, field = 'data mining', order_by = 'rank', order = 'asc'):
    field_dict = {'artificial intellgience': '人工智能', 'machine learning': '机器学习', 'data mining': '数据挖掘', 'computer networking': '计算机网络', 'natural language processing': 'NLP', 'computer graphics': '计算机图形', 'multimedia': '多媒体', 'web-information search': '网络搜索', 'system': '计算机系统', 'database': '数据库', 'security': '计算机安全', 'human-computern interaction': '人机交互', 'software engineering': '软件工程', 'theory': '计算机理论'}

    context = {order_by: True, order: True}
    if order == 'desc':
        order_by = '-' + order_by
    context['scholars'] = Scholar.objects.filter(classification = field).order_by(order_by)    
    context['listing'] = field_dict[field]
    context['data_set'] = 'field/' + field

    return render(request, 'scholar/list.html', context)

def tag_search(request, tag_name, order_by = 'rank', order = 'asc'):

    context = {order_by: True, order: True}
    if order == 'desc':
        order_by = '-' + order_by
    context['scholars'] = Scholar.objects.filter(tag__title__startswith = tag_name).order_by(order_by)
    context['listing'] = "标签: " + tag_name
    context['data_set'] = 'tag/' + tag_name

    return render(request, 'scholar/list.html', context)

def my_collection(request, col_id, order_by = 'rank', order = 'asc'):
    context = {order_by: True, order: True}
    if order == 'desc':
        order_by = '-' + order_by
    context['scholars'] = Scholar.objects.filter(collection = col_id).order_by(order_by)
    context['listing'] = '我的人才库: ' + Collection.objects.get(pk = col_id).name
    context['data_set'] = 'my_collection/' + col_id
    
    return render(request, 'scholar/list.html', context)

def profile(request, scholar_pk):
    scholar = get_object_or_404(Scholar, id = scholar_pk)
    return render(request, "scholar/index.html", {
        'scholar': scholar,
    })

def search(request, name = None, order_by = 'rank', order = 'asc'):
    if request.GET.get('search_name'):
        search_name = request.GET.get('search_name')
    else:
        search_name = name

    context = {order_by: True, order: True}
    if search_name != ' ' and search_name != '.':
        if order == 'desc':
            order_by = '-' + order_by
        scho = Scholar.objects.filter(name__contains = search_name) | Scholar.objects.filter(affiliation__contains = search_name)
        context['scholars'] = scho.order_by(order_by)

    context['listing'] = "搜索: " + search_name
    context['data_set'] = 'search/' + search_name
    return render(request, 'scholar/list.html', context)

def sort(request, var):
    var = var.split('/')
    function = var[0]
    content = var[1]
    if function == 'field':
        return field_rank(request, content, str(request.GET.get('orderKey')), str(request.GET.get('order')))
    elif function == 'tag':
        return tag_search(request, content, str(request.GET.get('orderKey')), str(request.GET.get('order')))
    elif function == 'search':
        return search(request, content, str(request.GET.get('orderKey')), str(request.GET.get('order')))
    elif function == 'my_collection':
        return my_collection(request, content, str(request.GET.get('orderKey')), str(request.GET.get('order')))

def scholar_focus_json(request, scholar_pk):
    data = Scholar.objects.get(id = scholar_pk).focus
    return JsonResponse(data)

def scholar_statistics_json(request, scholar_pk):
    data = Scholar.objects.get(id = scholar_pk).statistics
    return JsonResponse(data)

def collection_create(request, name):
    c = Collection(name = name, user = request.user)
    c.save()
    return JsonResponse({'msg': 'success'})


def collection_rename(request, col_id, name):
    c = Collection.objects.get(id = col_id)
    c.name = name
    c.save()
    return JsonResponse({'msg': 'success'})


def collection_delete(request, col_id):
    c = Collection.objects.filter(id = col_id).delete()
    return JsonResponse({'msg': 'success'})

def collection_add_scholar(request, col_id, scholar_pk):
    s = Scholar.objects.get(id = scholar_pk)
    Collection.objects.get(id = col_id).scholar.add(s)
    return JsonResponse({'msg': 'success'})

def collection_remove_scholar(request, col_id, scholar_pk):
    s = Scholar.objects.get(id = scholar_pk)
    Collection.objects.get(id = col_id).scholar.remove(s)
    return JsonResponse({'msg': 'success'})

