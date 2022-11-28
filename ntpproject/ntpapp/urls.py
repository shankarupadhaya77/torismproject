from django.urls import path
from .views import *


app_name = "ntpapp"
urlpatterns = [
    path('base_layout/', ClientBaseView.as_view(), name="clientbase"),
    path('get-blogs/', ClientGetBlogListView.as_view(), name="clientgetbloglist"),

    path('', ClientHomeView.as_view(), name="clienthome"),
    path('about/', ClientAboutView.as_view(), name="clientabout"),
    path('blog/<int:pk>/detail/', ClientBlogDetailView.as_view(),
         name="clientblogdetail"),
    path('category/<int:pk>/detail/', ClientCategoryDetalView.as_view(),
         name="clientcategorydetail"),


    path('feed/', LatestEntriesFeed()),

]
