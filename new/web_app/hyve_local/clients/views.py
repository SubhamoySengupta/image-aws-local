from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django_socketio import events


# Create your views here.
def home(request):
	template = get_template('index.html')
	html = template.render(Context({'name': 'MAIN'}))
	return HttpResponse(html)


def show(request):
	template = get_template('cli_1.html')
	html = template.render(Context({'name': 'CLI-1'}))
	return HttpResponse(html)


def d(request):
	template = get_template('cli_2.html')
	html = template.render(Context({'name': 'CLI-2'}))
	return HttpResponse(html)


def check(request):
	obj = dict(s='ss', d='dddd', f='f')
	return JsonResponse(obj)
