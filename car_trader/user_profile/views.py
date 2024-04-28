# user_profile views.py
from django.views.generic import UpdateView
from django.shortcuts import render, redirect,  get_object_or_404
from django.views import generic as views
from django.views import View
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import get_user_model
from .models import CustomUser
from ..ads.models import Ad
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import  RegistrationForm
from django.http import HttpResponseRedirect

UserModel = get_user_model()


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "profile.html"
    model = CustomUser
    slug_field = "slug"
    slug_url_kwarg = "user_slug"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs.get(self.slug_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_ads = Ad.objects.filter(user=self.object)
        context["user_ads"] = user_ads
        return context


class IndexView(View):
    def get(self, request, *args, **kwargs):
        user_slug = request.user.slug if request.user.is_authenticated else None
        latest_ads = Ad.objects.order_by("-id")[:10]
        context = {
            "user_slug": user_slug,
            "latest_ads": latest_ads,
        }
        return render(request, "index.html", context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "profile-edit.html"
    fields = ["phone_number", "region"]

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"user_slug": self.object.slug})


class RegistrationView(views.CreateView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy("index")

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class CustomLogoutView(LogoutView):
    template_name = "index.html"



class SearchView(View):
    def get(self, request, *args, **kwargs):
        fields = [
            "brand",
            "model",
            "engine",
            "gearbox",
            "coupe_type",
            "wheel",
            "color",
            "region",
        ]

        ads = Ad.objects.all()

        for field in fields:
            value = request.GET.get(field)
            if value:
                ads = ads.filter(**{f"{field}__icontains": value})

        context = {"ads": ads}
        return render(request, "search.html", context)
