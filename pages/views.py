from django.http import HttpResponse

def homePageView(request):
    """Home Page View"""
    return HttpResponse("Hello World!")


# Create your views here.
