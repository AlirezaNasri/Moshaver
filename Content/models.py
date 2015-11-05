from django.db import models

class ImageContent(models.Model):
	image = models.ImageField(upload_to='')
	caption = models.TextField(null=True, blank=True)

class FileContent(models.Model):
	file_field = models.FileField(upload_to='')
	description = models.TextField()

class News(models.Model):
	title = models.CharField(max_length=100)
	title_image = models.ImageField(upload_to='')
	images = models.ManyToManyField(ImageContent, null=True, blank=True)
	pub_date = models.DateTimeField(auto_now=True)
	summary = models.TextField()
	body = models.TextField()
	author = models.CharField(max_length=100)

class Workshop(models.Model):
	title = models.CharField(max_length=100)
	title_image = models.ImageField(upload_to='')
	images = models.ManyToManyField(ImageContent)
	summary = models.TextField()
	body = models.TextField()
	author = models.CharField(max_length=100)
	audience = models.TextField()
	audio = models.FileField(upload_to='')
	video = models.FileField(upload_to='')
	where = models.TextField()
	when = models.DateTimeField()

class Grad(models.Model):
	name = models.CharField(max_length=100)
	image = models.ForeignKey(ImageContent)
	country_rank = models.IntegerField()
	state_rank = models.IntegerField()
	major = models.CharField(max_length=100)
	acc_major = models.CharField(max_length=100)
	year = models.IntegerField()
	results = models.ImageField(upload_to='')
	city = models.CharField(max_length=100)
	school = models.CharField(max_length=100)

class Advisor(models.Model):
	name = models.CharField(max_length=100)
	image = models.ForeignKey(ImageContent)
	licence = models.TextField()
	tel = models.CharField(max_length=100)
	email = models.EmailField()
	position = models.TextField()

class Office(models.Model):
	tel = models.CharField(max_length=100)
	address = models.TextField()
	available_times = models.TextField()

class PsyContent(models.Model):
	title = models.CharField(max_length=100)
	image = models.ForeignKey(ImageContent)
	pub_date = models.DateTimeField(auto_now=True)
	summary = models.TextField()
	body = models.TextField()
	author = models.CharField(max_length=100)

class Interview(models.Model):
	question = models.TextField()
	answer = models.TextField()
	image = models.ImageField(upload_to='')
	date = models.DateTimeField()
	grad = models.ForeignKey(Grad)
	interviewer = models.CharField(max_length=100)
	header = models.TextField()
	footer = models.TextField()

class EduContent(models.Model):
	title = models.CharField(max_length=100)
	image = models.ForeignKey(ImageContent)
	pub_date = models.DateTimeField(auto_now=True)
	summary = models.TextField()
	body = models.TextField()
	author = models.CharField(max_length=100)
	files = models.ManyToManyField(FileContent)
