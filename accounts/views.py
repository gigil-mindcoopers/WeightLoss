from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accounts.forms import SignUpForm
from django.views.generic import TemplateView


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('accounts:signup_success'))
    else:

        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class SignupSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'signup_confirm.html'
