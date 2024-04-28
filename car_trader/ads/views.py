# ads views.py
from django.views.generic import UpdateView, DetailView
from django.shortcuts import render,  redirect
from django.views import generic as views
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import get_user_model
from .forms import AdForm, AdEditForm
from ..ads.models import Ad
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView

UserModel = get_user_model()


class CustomCreateView(CreateView):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"user_slug": self.request.user.slug})


class CustomUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        user_slug = self.object.user.slug
        return reverse("profile", kwargs={"user_slug": user_slug})

    def post(self, request, *args, **kwargs):
        if "delete_ad" in request.POST:
            ad = self.get_object_or_none()
            if ad:
                ad.delete()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return HttpResponseRedirect(self.get_success_url())
        return super().post(request, *args, **kwargs)

    def get_object_or_none(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(queryset, pk=pk) if pk else None


class ViewAd(DetailView):
    model = Ad
    template_name = "ad.html"
    context_object_name = "ad"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        context["is_owner"] = ad.user == self.request.user
        return context


class AdCreateView(LoginRequiredMixin, CustomCreateView):
    model = Ad
    form_class = AdForm
    template_name = "add-ad.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditAdView(LoginRequiredMixin, CustomUpdateView):
    model = Ad
    form_class = AdEditForm
    template_name = "edit-ad.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return reverse("profile", kwargs={"user_slug": self.request.user.slug})

    def post(self, request, *args, **kwargs):
        if "delete_ad" in request.POST:
            ad = self.get_object_or_none()
            if ad:
                ad.delete()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return HttpResponseRedirect(reverse("profile"))
        return super().post(request, *args, **kwargs)

    def get_object_or_none(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(queryset, pk=pk) if pk else None

    def get_initial(self):
        ad_instance = self.get_object()
        initial = super().get_initial()
        for field in ad_instance._meta.fields:
            initial[field.name] = getattr(ad_instance, field.name)
        return initial

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            form.instance.user = self.request.user
        return super().form_valid(form)
