from django.shortcuts import render
from .dboperation import *
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *
# Create your views here.
import datetime

def test(request):
    context          = {}
    list = get_news()
    people = get_papers('all')
    return render(request, 'people2.html', context)
    return HttpResponse(str(people))

def index(request):
    context          = {}
    context['banner'] = get_banner()
    context['upcoming'] = get_upcomming(5) #填写显示最近的几个
    context['news'] = get_news(5) #填写显示最近的几个
    context['type']="index"
    return render(request, 'index.html', context)

def seminar_list_web(request):
    year = request.GET.get('year')
    if(year==None):year = datetime.datetime.now().year
    context          = {}
    context['year'] = year
    context['list'] = get_seminar(year)
    context['type'] = "seminar"
    context['year_list']=[i for i in range(2021,datetime.datetime.now().year+1)]

    return render(request, 'events-list.html', context)

def news_list_web(request):
    year = request.GET.get('year')
    if(year==None):year = datetime.datetime.now().year
    context          = {}
    context['year'] = year
    context['list'] = get_allnews(year)
    context['type'] = "news"
    context['year_list']=[i for i in range(2021,datetime.datetime.now().year+1)]

    return render(request, 'events-list.html', context)
def seminar_web(request,id):
    context          = {}
    context['seminar']=get_detail_seminar(id)
    return render(request, 'blogpost.html', context)
def news_web(request,id):
    context          = {}
    context['seminar']=get_detail_news(id)
    return render(request, 'blogpost.html', context)

def people_list_web(request):
    context          = {}
    context['people']=get_people_list()
    return render(request, 'people_list.html', context)
def people_web(request,name):
    context=get_people(name)
    return render(request, 'people2.html', context)

def theme_list_web(request):
    context={}
    context['list']=get_theme_list()
    context['type']="themes"
    return render(request, 'theme_list.html', context)
def theme_web(request,id):
    context={}
    context['data']=get_theme(id)
    context['type']="themes"
    return render(request, 'theme.html', context)

def conference_list_web(request):
    context={}
    context['list']=get_conference_list()
    context['type']="conferences"
    return render(request, 'theme_list.html', context)
def conference_web(request,id):
    context={}
    context['data']=get_conference(id)
    context['type']="conferences"
    return render(request, 'theme.html', context)

def papers_web(request):
    context={}
    context['data']=get_papers_cate()
    context['type']="papers"
    context['list']=True
    return render(request, 'paper.html', context)

def papers_list_web(request,categroy_name):
    context={}
    context['data']=get_papers(categroy_name)
    context['type']="papers"

    return render(request, 'paper.html', context)
def about_web(request):
    context={}
    context['data']=get_about()
    context['type']="about"
    return render(request, 'single_page.html', context)