from django.shortcuts import render, redirect
from Content.models import News, Workshop, PsyContent, Interview, EduContent, ImageContent, FAQ, Grad, Advisor


def get_context(next_page=None, prev_page=None):
	news = News.objects.all().order_by('-pub_date')[:4]
	psy_contents = PsyContent.objects.all().order_by('-pub_date')[:4]
	edu_contents = EduContent.objects.all().order_by('-pub_date')[:4]
	workshops = Workshop.objects.all().order_by('-when')[:4]
	billboards = ImageContent.objects.filter(caption__startswith='billboard')[:5]
	faqs = FAQ.objects.all()[:4]

	return {
		"news": news, 
		"psy_contents": psy_contents, 
		"edu_contents": edu_contents, 
		"workshops": workshops,
		"billboards": billboards,
		"faq": faqs,
		"next_page": next_page,
		"prev_page": prev_page,
	}

def home_page(req):
	context = get_context()
	return render(req, 'home_page.html', context)

def get_all_workshops(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(Workshop.objects.all()) > page * 10 else None, page - 1 if page != 1 else None)
	context['main_workshops'] = Workshop.objects.all().order_by('-when')[page * 10 - 10:page * 10]
	return render(req, 'all_workshops.html', context)

def get_all_psys(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(Workshop.objects.all()) > page * 10 else None, page - 1 if page != 1 else None)	
	context['main_psy_contents'] = PsyContent.objects.all().order_by('-pub_date')[page * 10 - 10:page * 10]
	return render(req, 'all_psys.html', context)	

def get_all_news(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(News.objects.all()) > page * 10 else None, page - 1 if page != 1 else None)
	context['main_news'] = News.objects.all().order_by('-pub_date')[page * 10 - 10:page * 10]
	return render(req, 'all_news.html', context)

def get_all_edus(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(EduContent.objects.all()) > page * 10 else None, page - 1 if page != 1 else None)
	context['main_edu_contents'] = EduContent.objects.all().order_by('-pub_date')[page * 10 - 10:page * 10]
	return render(req, 'all_edus.html', context)

def get_all_faqs(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(FAQ.objects.all()) > page * 10 else None, page - 1 if page != 1 else None)
	context['main_faq'] = FAQ.objects.all()[page * 10 - 10:page * 10]
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
	fields = {}
	for grad in Grad.objects.all():
		if grad.major not in fields:
			fields[grad.major] = []
		fields[grad.major].append(grad)
       	context['fields'] = []
	for field in fields:
		context['fields'].append({
			'name': field,
			'grads': fields[field][:10]
			})
	return render(req, 'all_grads.html', context)		

def get_gallery(req):
	page = 1
	if 'page' in req.GET:
		page = int(req.GET['page'])
	context = get_context(page + 1 if len(ImageContent.objects.filter(caption__startswith='gallery')) > page * 10 else None, page - 1 if page != 1 else None)
	context['gallery'] = ImageContent.objects.filter(caption__startswith='gallery')[page * 10 - 10: page * 10]
	return render(req, 'gallery.html', context)	
