from django.shortcuts import render
from django.http import HttpResponse
from . import models

def main_page(request):
    return HttpResponse("Main")


def about_me(request):
    return HttpResponse("About me")


def toolbox(request):
    return HttpResponse("Toolbox")


def news(request):
    return HttpResponse("News")


def reviews(request):
    return HttpResponse("Reviews")


def contacts(request):
    return HttpResponse("Contacts")