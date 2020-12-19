from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


# Home page
@xframe_options_exempt
def home(request):
    return render(request, "home.html")
