# views.py
from django.views.generic import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
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
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import AdForm, RegistrationForm, AdEditForm
from .models import Ad
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


class CustomCreateView(CreateView):
    """
    Custom CreateView to ensure consistency in inheritance.
    """

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"user_slug": self.request.user.slug})


class CustomUpdateView(UpdateView):
    """
    Custom UpdateView to ensure consistency in inheritance.
    """

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


class ViewAd(DetailView):
    model = Ad
    template_name = "ad.html"
    context_object_name = "ad"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        context["is_owner"] = ad.user == self.request.user
        return context