from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from main.forms import ReviewForm
from . import models


def main_page(request):
    return render(request, 'main/home.html', {})


def about_me(request):
    return HttpResponse("About me")


def toolbox(request):
    return HttpResponse("Toolbox")


def news(request):
    return HttpResponse("News")


def reviews(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()

    return render(request, 'main/reviews.html', {"form": form})


def contacts(request):
    return HttpResponse("Contacts")


class ReviewView(FormView):
    template_name = 'main/reviews.html'
    form_class = ReviewForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("BEATCH")
        return super(ReviewView, self).form_valid(form)

