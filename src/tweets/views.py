from django.shortcuts import render

# Create your views here.

def tweet_detail_view(request, id=2):
    return render(request, "tweets/tweet_detail_view.html", {})

def tweet_list_view(request, id=2):
    return render(request, "tweets/list_view.html", {})