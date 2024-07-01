from django.shortcuts import render

# Create your views here.


def reserver_summary(request):
    return render(request, "reserver_summary.html", {})

def reserver_add(request):
    pass

def reserver_delete(request):
    pass

def reserver_update(request):
    pass