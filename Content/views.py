from django.shortcuts import render, redirect
from Content.models import News, Workshop, PsyContent, Interview, EduContent, ImageContent


def get_context(news=[0, 4], psy=[0, 4], edu=[0, 4], work=[0, 1]):
	news = News.objects.all().order_by('-pub_date')[news[0]:news[1]]
	psy_contents = PsyContent.objects.all().order_by('-pub_date')[psy[0]:psy[1]]
	edu_contents = EduContent.objects.all().order_by('-pub_date')[edu[0]:edu[1]]
	workshops = Workshop.objects.all().order_by('-when')[work[0]:work[1]]
	billboards = ImageContent.objects.filter(caption='billboard').order_by('-pub_date')

	return {
		"news": news, 
		"psy_contents": psy_contents, 
		"edu_contents": edu_contents, 
		"workshops": workshops,
		"billboards": billboards,
	}

def home_page(req):
	context = get_context()
	return render(req, 'home_page.html', context)

def get_all_workshops(req, page=1):
	context = get_context(work=[page * 10 - 10, page * 10])
	return render(req, 'all_workshops.html', context)

def get_all_psys(req, page=1):
	context = get_context(psy=[page * 10 - 10, page * 10])
	return render(req, 'all_psys.html', context)	

def get_all_news(req, page=1):
	context = get_context(news=[page * 10 - 10, page * 10])
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'all_news.html', context)

def get_all_edus(req, page=1):
	context = get_context(edu=[page * 10 - 10, page * 10])
	return render(req, 'all_edus.html', context)

def get_news(req, id):
	context = get_context()
	try:
		context['single_news'] = News.objects.get(id=id)
	except:
		return redirect(req, '/news')
	return render(req, 'single_news.html', context)
