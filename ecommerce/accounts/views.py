from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from .models import User
from django.contrib import messages


class UserRegistrationView(View):
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(email=cd["email"], phone_number=cd["phone_number"], full_name=cd["full_name"], password=cd["password"])
            messages.success(request, "You Are Registered  Successfully", extra_tags="success")
            return redirect("home:home")
        return render(request, 'accounts/register.html', {'form': form})