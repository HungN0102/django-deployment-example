from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello, Im from views.py and first_app/index.html'}
    return render(request, 'first_app/index.html', context=my_dict)

def index2(request):
    return HttpResponse("Hello World! Part 2")

def MTV(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/testing_mtv.html', context=date_dict)

def relative_url(request):
    return render(request, 'first_app/testing_relative_urls.html', context = {})