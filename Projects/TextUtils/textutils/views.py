from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render (request, "index.html")

def analyze(request):
    djtext = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc","off") # on off
    uppercase = request.GET.get("uppercase","off") # on off
    newlineremove = request.GET.get("newlineremove","off") # on off
    spaceremove = request.GET.get("spaceremove","off") # on off
    charcount = request.GET.get("charcount","off") # on off
    purpose = "None"
    result = "N/A"
    count = 0
        
    if removepunc =="on":
        purpose = "Remove Punctuations. "
        puncs = """`~!@#$%^&*_+\\|:;"',<.>/?=+-"""
        result = ""
        for ch in djtext:
            if not ch in puncs:
                result += ch
        djtext = result

    if uppercase =="on":
        purpose += "Upper Case. "
        result = ""
        for ch in djtext:
                result += ch.upper()
        djtext = result
        
    if newlineremove =="on":
        purpose += "New Line Remove. "
        result = ""
        for ch in djtext:
            if not ch == "\n":
                result += ch
        djtext = result
        
    if spaceremove =="on":
        purpose += "Extra Space Remove. "
        result = ""
        for index, ch in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " ") :
                result += ch
        djtext = result
    if charcount =="on":
        purpose += "character Counter. "
        res = ""
        for ch in djtext:
            if not (ch == "\n"):
                res += ch
        djtext = result

        count = len(res)
        
    context = {
        "result":result,
        "purpose":purpose,
        "count":count
    }
    return render (request, "results.html", context)