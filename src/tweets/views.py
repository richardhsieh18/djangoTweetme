from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet

# Create your views here.

class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()
    #model = Tweet

    def get_object(self):
        Tweet.objects.get(id=2)

class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()
    #model = Tweet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


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