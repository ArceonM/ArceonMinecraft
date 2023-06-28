from django.shortcuts import render,redirect

def home(request):
    """указывает главную страничку сайта"""
    return render(request, "forum2/home.html", {})

def not_work(request):
    return render(request,"forum2/not_work.html")
