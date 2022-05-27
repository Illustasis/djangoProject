from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from System.models import *
import json


@csrf_exempt
def detail(request):
    if request.method == 'GET':
        book_id = request.GET.get('book_id')  # 获取图书ID
        user_id = request.GET.get('user_id')  # 获取用户ID
        book = Book.objects.get(book_id=book_id)
        users = Collect.objects.filter(resource_id=book_id).filter(column=1)  # 查询关注此书的用户
        users_id = []
        for user in users:
            uid = int(user.user_id)
            users_id.append(uid)
        # 生成关注用户ID列表(int数据类型)
        if user_id in users_id:  # 查找该用户是否在列表内，在则返回已关注，否则返回未关注
            return JsonResponse(
                {'成功': 200,
                 'book_id': book.book_id, 'name': book.name, 'image': book.image, 'author': book.author,
                 'press': book.press, 'introduction': book.introduction, 'score': book.score, 'heat': book.heat,
                 '已关注': 400})
        else:
            return JsonResponse(
                {'成功': 200,
                 'book_id': book.book_id, 'name': book.name, 'image': book.image, 'author': book.author,
                 'press': book.press, 'introduction': book.introduction, 'score': book.score, 'heat': book.heat,
                 '未关注': 300})

    else:
        return JsonResponse({'失败，请求方式错误': 100})


@csrf_exempt
def hot_article(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        articles = Article.objects.filter(columm=1).filter(article_id=book_id).order_by('-heat')
        article_list = []
        for article in articles:
            article_list.append(article)
        article_json = json.dumps({'value': article_list}, ensure_ascii=False)
        return JsonResponse({'成功': 200}, article_json)
    else:
        return JsonResponse({'失败，请求方式错误': 100})


@csrf_exempt
def new_article(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        articles = Article.objects.filter(columm=1).filter(article_id=book_id).order_by('-date')
        # 不确定这里是从早到晚排序还是从晚到早排序，测试时如果遇到相反的可以把order_by后面括号内的'-date'改成'date'
        article_list = []
        for article in articles:
            article_list.append(article)
        article_json = json.dumps({'value': article_list}, ensure_ascii=False)
        return JsonResponse({'成功': 200}, article_json)
    else:
        return JsonResponse({'失败，请求方式错误': 100})
