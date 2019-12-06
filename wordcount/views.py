from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text=request.GET['fulltext']
    wordlist=text.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #uppdate
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    return render(request, 'count.html', {'worddictionary':worddictionary})
