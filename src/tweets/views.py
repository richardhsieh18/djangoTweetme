from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    #success_url = '/tweet/create/'

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    #success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy('tweet:list')

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet, pk=pk)
        #Tweet.objects.get(id=pk)
        return obj

class TweetListView(ListView):
    
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context
    


def tweet_detail_view(request, pk=None): # pk == id
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj,
        "testdata": obj
    }
    return render(request, "tweets/detail_view.html", context)