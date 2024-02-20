from django.urls import path

from pages.views import home_view, HomePageView, AboutPageView

urlpatterns = [
    #path('', home_view, name='index'),
    path('', HomePageView.as_view(), name='index'),
    path('about', AboutPageView.as_view(), name='about'),
]
