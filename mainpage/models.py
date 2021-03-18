from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
# Create your models here.

from django.db import models
from uuslug import slugify


def seminar_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'seminar/seminar_{0}/{1}'.format(instance.date_add, filename)


class seminar(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=20,blank=True)
    people = models.CharField(verbose_name="人名",max_length=20,blank=True)
    date = models.DateTimeField(null=True,blank=True)
    location = models.CharField(max_length=20,blank=True)
    #details=models.TextField(blank=True)
    content = RichTextUploadingField(blank=True)
    slides = models.FileField(upload_to=seminar_directory_path,blank=True)
    video = models.FileField(upload_to=seminar_directory_path,blank=True)
    date_add = models.DateField(auto_now_add=True)
    #url = models.URLField(default='/seminar/{0}'.format(id))
    def __str__(self): 
        return str(self.topic)

def people_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'people/img/{0}/{1}'.format(instance.url, filename)
from django.template.defaultfilters import slugify

class people(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,blank=True)
    img = models.FileField(upload_to=people_directory_path,blank=True)
    identity = models.CharField(max_length=20,blank=True)
    introduction = models.CharField(max_length=20,blank=True)
    contact = RichTextUploadingField(blank=True)
    home = RichTextUploadingField(blank=True)
    cv = RichTextUploadingField(blank=True)
    pub = RichTextUploadingField(blank=True)
    pre = RichTextUploadingField(blank=True)
    awards = RichTextUploadingField(blank=True)
    classes= RichTextUploadingField(blank=True)
    links = RichTextUploadingField(blank=True)

    url = models.SlugField(max_length=64,editable=False,blank=True,primary_key=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(people, self).save(*args, **kwargs)


    def __str__(self): 
        return str(self.name)
class people_priority(models.Model):
    priority = models.IntegerField()
    show = models.BooleanField()
    people = models.OneToOneField("people", on_delete=models.CASCADE)
    def __str__(self): 
        return str(self.people.name)

class news(models.Model):
    topic = models.CharField(max_length=20,blank=True)
    date_add = models.DateField(auto_now_add=True)
    date = models.DateTimeField(default=datetime.now())
    date_change = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True)
    def __str__(self): 
        return str(self.topic)

class conferences(models.Model):
    topic = models.CharField(max_length=20,blank=True)
    date_add = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True)
    def __str__(self): 
        return str(self.topic)
class themes(models.Model):
    topic = models.CharField(max_length=20,blank=True)
    date_add = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True)
    def __str__(self): 
        return str(self.topic)

def banner_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'banner/banner_{0}/{1}'.format(instance.date_add, filename)
class banner(models.Model):
    img = models.FileField(upload_to=banner_directory_path,blank=True)
    date_add = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=20,blank=True)
    content = models.CharField(max_length=20,blank=True)
    priority = models.IntegerField()
    def __str__(self): 
        return str(self.priority)
def paper_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'paper/paper_{0}/{1}'.format(filename,instance.date_add)
class papers(models.Model):
    name = models.CharField(max_length=20,blank=True)
    date = models.DateTimeField(default=datetime.now())
    content = RichTextUploadingField(blank=True)
    paper_file = models.FileField(upload_to=paper_directory_path,blank=True)
    papers_categroy = models.ManyToManyField("papers_categroy")
    def __str__(self): 
        return str(self.name)


class about(models.Model):
    date_add = models.DateField(auto_now_add=True)
    date_change = models.DateField(auto_now=True)
    content = RichTextUploadingField(blank=True)

class papers_categroy(models.Model):
    categroy_name=models.CharField(max_length=20,blank=True)
    def __str__(self): 
        return str(self.categroy_name)
