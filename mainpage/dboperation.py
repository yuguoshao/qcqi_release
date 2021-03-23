from .models import *
from datetime import datetime
def get_banner():
    list = banner.objects.order_by("priority").all()
    out=[{'img':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    return out

def get_upcomming(many=5):
    list = seminar.objects.filter(date__gt=datetime.now()).order_by("date")[:many]
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'type':'seminar','url':'seminar/'+str(v.id),'year':v.date.strftime('%Y') , 'month_b':v.date.strftime('%b'),'day':v.date.strftime('%d'),'time':v.date.strftime("%I:%M%p"),'people':v.people,'topic':v.topic,'location':v.location} for v in list]
    return out

def get_news(many=5):
    list = news.objects.all().order_by("-date")[:many]
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'url':'news/'+str(v.id),'year':v.date.strftime('%Y') , 'month_b':v.date.strftime('%b'),'day':v.date.strftime('%d'),'time':v.date.strftime("%I:%M%p"),'topic':v.topic,'content':v.content} for v in list]
    return out
def get_class_index(many=5):
    list = classes.objects.all().order_by("-date_add")[:many]
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'url':'Mini-Courses/'+str(v.id),'topic':v.topic,'content':v.content,'people':v.people,'category':v.category,'location':v.location} for v in list]
    return out

def get_seminar(year=2021):
    list = seminar.objects.filter(date__year=year).order_by("date")
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'type':'seminar','url':'seminar/'+str(v.id),'year':v.date.strftime('%Y') , 'month_b':v.date.strftime('%b'),'day':v.date.strftime('%d'),'time':v.date.strftime("%I:%M%p"),'people':v.people,'topic':v.topic,'location':v.location} for v in list]
    return out
def get_class(year=2021):
    list = classes.objects.filter(date_add__year=year).order_by("date_add")
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'type':'Mini-Courses','url':'Mini-Courses/'+str(v.id),'people':v.people,'topic':v.topic,'location':v.location,'category':v.category} for v in list]
    return out

def get_allnews(year=2021):
    list = news.objects.filter(date__year=year).order_by("-date")
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'type':'news','url':'news/'+str(v.id),'year':v.date.strftime('%Y') , 'month_b':v.date.strftime('%b'),'day':v.date.strftime('%d'),'time':v.date.strftime("%I:%M%p"),'topic':v.topic} for v in list]
    return out

def get_detail_seminar(num):
    v = seminar.objects.filter(id=num)[0]
    out={'type':'seminar','id':num,'date':v.date.strftime('%Y-%m-%d') , 'date_add':v.date_add.strftime('%b %d,%Y'),'content':v.content,'time':v.date.strftime("%I:%M%p"),'people':v.people,'topic':v.topic,'location':v.location,'slides':'/media/'+str(v.slides),'video':'/media/'+str(v.video)}
    return out
def get_detail_class(num):
    v = classes.objects.filter(id=num)[0]
    out={'type':'Mini-Courses','id':num, 'date_add':v.date_add.strftime('%b %d,%Y'),'content':v.content,'people':v.people,'topic':v.topic,'location':v.location,'slides':'/media/'+str(v.slides),'video':'/media/'+str(v.video)}
    return out

def get_detail_news(num):
    v = news.objects.filter(id=num)[0]
    out={'type':'news','id':num,'date':v.date.strftime('%Y-%m-%d') , 'date_add':v.date_add.strftime('%b %d,%Y'),'content':v.content,'time':v.date.strftime("%I:%M%p"),'topic':v.topic,'slides':'/media/','video':'/media/'}
    return out
def get_people_list():
    list = people_priority.objects.filter(show=True).order_by("priority")
    out=[{'priority':v.priority,'name':v.people.name,'img':'/media/'+str(v.people.img),'identity':v.people.identity,'introduction':v.people.introduction,'url':v.people.url}for v in list]
    return out
def get_people(name_want):
    v = people.objects.filter(url=name_want)[0]
    out={'name':v.name,'img':'/media/'+str(v.img),'identity':v.identity,'contact':v.contact,'home':v.home,'cv':v.cv,'pub':v.pub,'pre':v.pre,'awards':v.awards,'classes':v.classes,'links':v.links}
    return out

def get_theme_list():
    list = themes.objects.all()
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'url':'themes/'+str(v.id),'topic':v.topic} for v in list]
    return out
def get_theme(num):
    v = themes.objects.filter(id=num)[0]
    out={'type':'themes','id':num,'content':v.content,'topic':v.topic}
    return out

def get_conference_list():
    list = conferences.objects.all()
    #out=[{'year':'media/'+str(v.img) , 'title':v.title,'content':v.content} for v in list]
    out=[{'url':'conferences/'+str(v.id),'topic':v.topic} for v in list]
    return out
def get_conference(num):
    v = conferences.objects.filter(id=num)[0]
    out={'type':'conferences','id':num,'content':v.content,'topic':v.topic}
    return out
def get_papers_cate():
    list = papers_categroy.objects.all()
    out=[{'name':v.categroy_name ,'amount':len(papers.objects.filter(papers_categroy__categroy_name=v.categroy_name))} for v in list]
    return out,len(papers.objects.all())

def get_papers(cate):
    if (cate=="all"):
        lists = papers.objects.all().order_by('date')
    else:
        lists = papers.objects.filter(papers_categroy__categroy_name=cate).order_by('date')
    t=1
    out=[]
    for v in lists:
        out.append({'content':'<p>'+"["+str(t) +"]"+v.content.replace('<p>', '', 1)})
        t=t+1
    out.reverse()
    return out
def get_about():
    v = about.objects.all()[0]
    out={'content':v.content}
    return out

def testa():
    v = banner.objects.all()[0]
    out=v.date_add.strftime('%Y-%m-%d_%H-%M')
    return out
