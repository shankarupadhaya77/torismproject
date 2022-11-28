from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import *
from .models import *
from .forms import *


class ClientMixin(object):
    def get_context_data(self, **kwargs):
        print("It should be just after middleware")
        context = super().get_context_data(**kwargs)
        context['allcategory'] = Category.objects.all()

        return context


class ClientGetBlogListView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.order_by('-id')
        jsondata = serializers.serialize('json', blogs)
        return HttpResponse(jsondata)


class ClientBaseView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clientbase.html"


class ClientHomeView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clienthome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = ImageSlider.objects.all()
        context['blogs'] = Blog.objects.order_by('-id')
        return context


class ClientAboutView(ClientMixin, TemplateView):
    template_name = "clienttemplates/clientabout.html"


class ClientBlogDetailView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientblogdetail.html"
    model = Blog
    context_object_name = "blog"


class ClientCategoryDetalView(ClientMixin, DetailView):
    template_name = "clienttemplates/clientcategorydetail.html"
    model = Category
    context_object_name = "category"


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/feed/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return Blog.objects.order_by('-id')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.details

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('ntpapp:clientblogdetail', args=[item.pk])
