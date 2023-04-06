from django.shortcuts import render,HttpResponse


def home_page(request):
    # return HttpResponse(request, 'Hello django')
    return render(request, 'home.html')