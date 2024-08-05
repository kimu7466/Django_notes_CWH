from django.shortcuts import render

# def index(request):
#     params = {"name":"imroz","age":25}
#     return render (request, "index.html", params)

def index(request):
    return render (request, "index.html")

def removepunc(request):
    djtext = request.GET.get("text","default")
    return render (request, "results.html", {"djtext":djtext})
