from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def joinus(request):
    return render(request, 'joinus.html')


def review(request):
    return render(request, 'review.html')


def single(request):
    return render(request, 'single.html')
