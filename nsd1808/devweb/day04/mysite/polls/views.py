from django.shortcuts import render, HttpResponse

def index(request):
    # 形参request名称随便定义，但是必须提供，用户的请求将作为实参传入
    # return HttpResponse('<h1>投票首页</h1>')
    return render(request, 'index.html')
