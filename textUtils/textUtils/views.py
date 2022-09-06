#i have created this file - Udit
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name' : 'harry', 'place' : 'mars'}
    return render(request, 'index.html', params)
    # return HttpResponse('<a href = "https://leetcode.com/problemset/all"> click here </a><br><a href = "https://www.facebook.com/"> click here </a>')
def analyze(request):
    djText = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunc','off')
    fullCaps = request.POST.get('fullCaps','off')
    newLineRemove = request.POST.get('newLineRemove','off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover','off')
    # countCharacter = request.GET.get('countCharacter','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    purposes = []
    if removePunc == 'on':
        for char in djText:
            if char not in punctuations and removePunc == 'on':
                analyzed = analyzed + char
        djText = analyzed
        analyzed = ""
        purposes.append('Remove Punctuations')
    if fullCaps == 'on':
        for char in djText:
            analyzed = analyzed + char.upper()
        djText = analyzed
        analyzed = ""
        purposes.append('Changed to Uppercase')

    if newLineRemove == 'on':
        for char in djText:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djText = analyzed
        analyzed = ""
        purposes.append('removed new lines')

    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djText):
            if djText[index] != ' ':
                analyzed += char
        djText = analyzed
        analyzed = ""
        purposes.append('removing extra space')

    # if countCharacter == 'on':
    #     count = 0
    #     for index in enumerate(djText):
    #         count += 1

    params = {'purpose' : purposes, 'analyzed_text' : djText}
    return render(request, 'analyze.html' , params)


