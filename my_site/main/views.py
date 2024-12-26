from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")


def tables(request):
    return render(request, "main/tables.html")



def regi(request):
    return render(request, "main/regi.html")