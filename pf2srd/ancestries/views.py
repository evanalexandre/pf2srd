from django.shortcuts import get_object_or_404, render
import json

with open('ancestries/data/ancestries.json') as data:
    ancestries = json.load(data)

def index(request):
    return render(request, 'ancestries/index.html', ancestries)

def detail(request, ancestry):
    for item in ancestries['ancestries']:
        item['active'] = False
    ancestry = next(i for i in ancestries['ancestries'] if i['name'] == ancestry)
    ancestry['active'] = True
    return render(request, 'ancestries/index.html', ancestries)