from django.shortcuts import render
from mysite.models import POST
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def homepage(request):
    posts = POST.objects.all()
    now = datetime.now()
    return render (request, 'index.html',locals())

def showpost(request, slug):
    POST = POST.objects.get(slug=slug)
    #select * from post where slug=%slug
    return render(request,'post.html',locals())


    
'''
def homepage(request):
    posts = POST.objects.all() #select * from post
    post_list = list( )
    for counter,post in enumerate(posts):
        post_list.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_list)
'''