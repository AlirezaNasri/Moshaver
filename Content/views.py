from django.shortcuts import render, redirect
from Content.models import News, Workshop, PsyContent, Interview, EduContent, ImageContent, FAQ, Grad, Advisor


def get_context(news=[0, 4], psy=[0, 4], edu=[0, 4], work=[0, 1]):
	news = News.objects.all().order_by('-pub_date')[news[0]:news[1]]
	psy_contents = PsyContent.objects.all().order_by('-pub_date')[psy[0]:psy[1]]
	edu_contents = EduContent.objects.all().order_by('-pub_date')[edu[0]:edu[1]]
	workshops = Workshop.objects.all().order_by('-when')[work[0]:work[1]]
	billboards = ImageContent.objects.filter(caption='billboard')
	faqs = FAQ.objects.all()[:4]

	return {
		"news": news, 
		"psy_contents": psy_contents, 
		"edu_contents": edu_contents, 
		"workshops": workshops,
		"billboards": billboards,
		"FAQ": faqs,
	}

def home_page(req):
	context = get_context()
	return render(req, 'home_page.html', context)

def get_all_workshops(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(work=[page * 10 - 10, page * 10])
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'all_workshops.html', context)

def get_all_psys(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(psy=[page * 10 - 10, page * 10])
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'all_psys.html', context)	

def get_all_news(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(news=[page * 10 - 10, page * 10])
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'all_news.html', context)

def get_all_edus(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(edu=[page * 10 - 10, page * 10])
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'all_edus.html', context)

def get_all_faqs(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context()
	context['FAQ'] = FAQ.objects.all()[page * 10 - 10: page * 10]
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'FAQ.html', context)

def get_news(req, id):
	id = int(id)
	context = get_context()
	try:
		context['single_news'] = News.objects.get(id=id)
	except:
		return redirect(req, '/news/')
	return render(req, 'single_news.html', context)

def get_edu(req, id):
	id = int(id)
	context = get_context()
	try:
		context['single_edu'] = EduContent.objects.get(id=1)
	except:
		return redirect(req, '/edu/')
	return render(req, 'single_edu.html', context)

def get_workshop(req, id):
	id = int(id)
	context = get_context()
	try:
		context['single_workshop'] = Workshop.objects.get(id=id)
	except:
		return redirect(req, '/workshops/')
	return render(req, 'single_workshop.html', context)

def get_psy(req, id):
	id = int(id)
	context = get_context()
	try:
		context['single_psy'] = PsyContent.objects.get(id=id)
	except:
		return redirect(req, '/psychology/')
	return render(req, 'single_psy.html', context)	

def get_all_advisors(req):
	context = get_context()
	context['advisors'] = Advisor.objects.all()
	return render(req, 'all_advisors.html', context)	

def get_all_grads(req):
	context = get_context()
	context['grads'] = Grad.objects.all()
	return render(req, 'all_grads.html', context)		

def get_gallery(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context()
	context['gallery'] = ImageContent.objects.filter(caption='gallery')[page * 10 - 10: page * 10]
	context['next_page'] = page + 1
	context['prev_page'] = page - 1
	return render(req, 'gallery.html', context)	
