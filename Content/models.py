from django.db import models
from ckeditor.fields import RichTextField
import datetime


class ImageContent(models.Model):
    image = models.ImageField(upload_to='static/images')
    caption = models.TextField(null=True, blank=True)

    #	image_type = models.TextField(default='normal')

    def __unicode__(self):
        return self.caption

    def __str__(self):
        return self.caption.encode('utf-8')


class FileContent(models.Model):
    file_field = models.FileField(upload_to='static')
    description = models.TextField()

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description.encode('utf-8')


class News(models.Model):
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='static/images')
    images = models.ManyToManyField(ImageContent, null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    summary = RichTextField()
    body = RichTextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title.encode('utf-8')


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='static/images')
    images = models.ManyToManyField(ImageContent, null=True, blank=True)
    summary = RichTextField()
    body = RichTextField()
    author = models.CharField(max_length=100)
    audience = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='static', null=True, blank=True)
    video = models.FileField(upload_to='static', null=True, blank=True)
    where = RichTextField()
    when = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title.encode('utf-8')


class Grad(models.Model):
    name = models.CharField(max_length=100)
    #	grad_image = models.ImageField(upload_to='static/images')
    row = models.IntegerField()
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    country_rank = models.IntegerField(null=True, blank=True)
    state_rank = models.IntegerField(null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    acc_major = models.CharField(max_length=100)
    year = models.IntegerField()
    results = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name.encode('utf-8')


class Advisor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(ImageContent)
    licence = RichTextField()
    tel = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.TextField()

    def __unicode__(self):
        return self.name


    def __str__(self):
        return self.name.encode('utf-8')


class Office(models.Model):
    tel = models.CharField(max_length=100)
    address = models.TextField()
    available_times = models.TextField()

    def __unicode__(self):
        return self.address

    def __str__(self):
        return self.address.encode('utf-8')


class PsyContent(models.Model):
    title = models.CharField(max_length=100)
    image = models.ForeignKey(ImageContent)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    summary = RichTextField()
    body = RichTextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title.encode('utf-8')


class Interview(models.Model):
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='static/images')
    date = models.DateTimeField()
    grad = models.ForeignKey(Grad)
    interviewer = models.CharField(max_length=100, null=True, blank=True)
    header = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)


class EduContent(models.Model):
    title = models.CharField(max_length=100)
    image = models.ForeignKey(ImageContent, null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    summary = RichTextField()
    body = RichTextField()
    author = models.CharField(max_length=100)
    files = models.ManyToManyField(FileContent, null=True, blank=True)

    def __str__(self):
        return self.title.encode('utf-8')


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.question.encode('utf-8')


class Announcement(models.Model):
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    title = models.TextField()
    body = RichTextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title.encode('utf-8')


class Class(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
