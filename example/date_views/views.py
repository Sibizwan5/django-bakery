from django.shortcuts import render
from .models import Article
from bakery.views import (
    BuildableArchiveIndexView,
    BuildableYearArchiveView,
    BuildableMonthArchiveView,
    BuildableWeekArchiveView,
    BuildableDayArchiveView,
    BuildableTodayArchiveView,
    BuildableDateDetailView
)


class MyIndexView(BuildableArchiveIndexView):
    model = Article
    date_field = 'pub_date'
    #allow_future = True
    #paginate_by = 2


class MyYearArchiveView(BuildableYearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    #year_format = "%y"
    #allow_future = True


class MyMonthArchiveView(BuildableMonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    #allow_future = True
