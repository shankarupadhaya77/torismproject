from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import *


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('details',)


admin.site.register(Blog, BlogAdmin)


class FestivalAdmin(SummernoteModelAdmin):
    summernote_fields = ('details',)


admin.site.register(Festival, FestivalAdmin)


class HeritageAdmin(SummernoteModelAdmin):
    summernote_fields = ('details',)


admin.site.register(Heritage, HeritageAdmin)


admin.site.register([ImageSlider, Category])
