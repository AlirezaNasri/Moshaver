from django.shortcuts import render
from Content.models import News, Workshop, PsyContent, Interview, EduContent


def get_context(news=[0, 4], psy=[0, 4], edu=[0, 4], work=[0, 1]):
	news = News.objects.all().order_by('-pub_date')[news[0]:news[1]]
	psyContents = PsyContent.objects.all().order_by('-pub_date')[psy[0]:psy[1]]
	eduContents = EduContent.objects.all().order_by('-pub_date')[edu[0]:edu[1]]
	workshops = Workshop.objects.all().order_by('-when')[work[0]:work[1]]

	return {
		"news": news, 
		"psyContents": psyContents, 
		"eduContents": eduContents, 
		"workshops": workshops,
	}

def home_page(req):
	context = get_context()
	return render(req, 'main1.html', context)

def get_all_workshops(req, page=1):
	context = get_context(work=[page * 10 - 10, page * 10])
	return render(req, 'all_workshops.html', context)

def get_all_psys(req, page=1):
	context = get_context(psy=[page * 10 - 10, page * 10])
	return render(req, 'all_psys.html', context)	

def get_all_news(req, page=1):
	context = get_context(news=[page * 10 - 10, page * 10])
	return render(req, 'all_news.html', context)

def get_all_edus(req, page=1):
	context = get_context(edu=[page * 10 - 10, page * 10])
	return render(req, 'all_edus.html', context)

