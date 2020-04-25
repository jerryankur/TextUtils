# I have created this file -Ankur
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	return render(request, "index.html")


def analyze(request):
	djtext = request.GET.get('text', 'default')

	removepunc = request.GET.get('removepunc', 'off')
	fullcaps = request.GET.get('fullcaps', 'off')
	newlineremover = request.GET.get('newlineremover', 'off')
	extraspaceremover = request.GET.get('extraspaceremover', 'off')

	if removepunc == "on":
		punctuations = ''':()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ''
		for char in djtext:
			if char not in punctuations:
				analyzed += char
		params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
		return render(request, 'analyze.html', params)

	elif fullcaps == "on":
		analyzed = ''
		for char in djtext:
			analyzed += char.upper()
		params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
		return render(request, 'analyze.html', params)

	elif newlineremover == "on":
		analyzed = ''
		for char in djtext:
			if char != '\n':
				analyzed += char
		params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
		return render(request, 'analyze.html', params)

	elif extraspaceremover == "on":
		analyzed = ''
		c = None
		for char in djtext:
			if char == ' ' and c == ' ':
				continue
			c = char
			analyzed += char
		params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
		return render(request, 'analyze.html', params)

	else:
		return HttpResponse("Error")


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
