# I have created this file -Ankur
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, "index.html")


def analyze(request):
	djtext = request.POST.get('text', 'default')

	removepunc = request.POST.get('removepunc', 'off')
	fullcaps = request.POST.get('fullcaps', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	extraspaceremover = request.POST.get('extraspaceremover', 'off')

	params = {'purpose': '', 'analyzed_text': djtext}
	if removepunc == "on":
		punctuations = ''':()-[]{};:'"\,<>./?@#$%^&*_~'''
		params['analyzed_text'] = ''
		for char in djtext:
			if char not in punctuations:
				params['analyzed_text'] += char
		params['purpose'] += 'Removed Punctuations '
		djtext= params['analyzed_text']

	if fullcaps == "on":
		params['analyzed_text'] = ''
		for char in djtext:
			params['analyzed_text'] += char.upper()
		params['purpose'] += 'Changed to Uppercase '
		djtext= params['analyzed_text']

	if newlineremover == "on":
		params['analyzed_text'] = ''
		for char in djtext:
			if char != '\n' and char !='\r':
				params['analyzed_text'] += char
		params['purpose'] += 'Removed NewLines '
		djtext = params['analyzed_text']

	if extraspaceremover == "on":
		params['analyzed_text'] = ''
		c = None
		for char in djtext:
			if char == ' ' and c == ' ':
				continue
			c = char
			params['analyzed_text'] += char
		params['purpose'] += 'Removed Extra Spaces '

	return render(request, 'analyze.html', params)



"""
def capfirst(request):
	return HttpResponse("capitalize first")


def newlineremove(request):
	return HttpResponse("new line remover")


def spaceremove(request):
	return HttpResponse("space remover")


def charcount(request):
	return HttpResponse("character count")
"""
