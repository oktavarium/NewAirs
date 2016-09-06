from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from main.forms import ReviewForm, EmailForm
from main.models import Review, AboutMe
from newairs import settings

class MainView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['form'] = EmailForm()
        context['reviews'] = Review.objects.filter(to_main=True).order_by('-created_date')[:2]
        #context['copyright'] = AboutMe.objects.filter(user_field="copyright").values()[0]["user_data"]
        return context

    def post(self, request):
        if request.is_ajax():
            form = EmailForm(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                    'New message from site by {0} [{1}]'.format(request.POST["user_name"],
                                                                request.POST["user_email"]),
                    request.POST["user_text"],
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
                max_age = 365 * 24 * 60 * 60  # one year
                response = JsonResponse({'result': 'OK'}, status=200)
                response.set_cookie('email_sent', 'true', max_age=max_age)
                return response
            else:
                return JsonResponse(form.errors, status=400)


def about_me(request):
    return HttpResponse("About me")


def toolbox(request):
    return HttpResponse("Toolbox")


def news(request):
    return HttpResponse("News")


class ReviewView(ListView):
    model = Review
    template_name = "main/rev_cell.html"
    context_object_name = "reviews"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

    def get_queryset(self):
        return Review.objects.filter(confirmed=True).order_by('-created_date')

    def post(self, request):
        if request.is_ajax():
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                max_age = 365 * 24 * 60 * 60  # one year
                response = JsonResponse({'result': 'OK'}, status=200)
                response.set_cookie('review_posted', 'true', max_age=max_age)
                return response
            else:
                return JsonResponse(form.errors, status=400)

    def get(self, request, **kwargs):
        if request.is_ajax():
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            return render(request, "main/reviews_content.html", context)
        return super(ReviewView, self).get(request, **kwargs)


def contacts(request):
    return HttpResponse("Contacts")


