from django.shortcuts import render,redirect
from django.views import View
from .forms import PageForm

class IndexView(View):
    def get(self,request):
        return render(request,"bbs/index.html")

class PageCreateView(View):
    def get(self,request):
        form = PageForm()
        return render(request,"bbs/page_form.html",{"form":form})

    def post(self,request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bbs:index")
        return render(request,"bbs/page_form.html",{"form":form})
            


index = IndexView.as_view()
page_create = PageCreateView.as_view()