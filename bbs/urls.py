from django.urls import path
from . import views


app_name = "bbs"
urlpatterns = [
    path("",views.index,name="index"),
    path("page/create/", views.page_create, name="page_create"),
]