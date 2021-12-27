from django.shortcuts import render
from django.views import generic
from django.views import View as BaseView

# Create your views here.

class HomePageView(BaseView):
    template_name = "main/index.html"
    def get(self, request, *args, **kwargs):
        return render(request, "main/index.html", {"happy":"is_not_to_be_true"})
