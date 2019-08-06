from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet
from .forms import TweetModelForm

# Create your views here.

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = '/tweet/create/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        'form': form
    }
    return render(request, "tweets/create_view.html", context)


class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()
    #model = Tweet

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        #Tweet.objects.get(id=pk)
        return obj

class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()
    #model = Tweet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


def tweet_detail_view(request, pk=None): # pk == id
    #obj = Tweet.objects.get(pk=pk)
    obj = get_object_or_404(Tweet, pk=pk)
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