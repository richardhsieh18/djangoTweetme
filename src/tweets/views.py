from django.shortcuts import render

from .models import Tweet

# Create your views here.

def tweet_detail_view(request, id=2):
    obj = Tweet.objects.get(id=id)
    print(obj)
    context = {
        "object": obj,
        "testdata": obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    querySet = Tweet.objects.all()
    print(querySet)
    for obj in querySet:
        print(obj.content)
    context = {
        "object_list": querySet
    }
    return render(request, "tweets/list_view.html", context)