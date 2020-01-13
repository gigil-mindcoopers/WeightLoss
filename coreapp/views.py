from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import TemplateView, UpdateView, CreateView
from random_word import RandomWords

from coreapp.models import UserDetails, MyFittness


class Home(TemplateView):
    template_name = 'home.html'


class InitialWeigh(TemplateView):
    template_name = 'initial_weight.html'


class WeighInstruction(TemplateView):
    template_name = 'weight_instruction.html'


class WeighWord(TemplateView):
    template_name = 'weight_word.html'

    def get_context_data(self, **kwargs):
        context = super(WeighWord, self).get_context_data()
        try:
            # Get existing random words
            user_details = UserDetails.objects.get(user=self.request.user)
            context['random_word'] = user_details.weigh_word
            context['slug'] = user_details.slug
        except UserDetails.DoesNotExist:
            # Generating new random word
            r = RandomWords()
            weigh_word = r.get_random_word()
            context['random_word'] = weigh_word

            # Generating slug
            UserDetails.objects.create(user=self.request.user, weigh_word=weigh_word,
                                       slug=slugify(self.request.user.email))
            context['slug'] = slugify(self.request.user.email)


        return context


class UserData(CreateView):
    template_name = 'user_details.html'
    model = MyFittness
    fields = [
        'weigh_photo', 'body_photo',
        'weight', 'height', 'user'
    ]
    success_url = '/initial-weigh/details/data-received/'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user
        form.save()
        print("save")
    #     # Saving user details
    #     weight = form.cleaned_data['weight']
    #     height = form.cleaned_data['height']
    #     weigh_word = form.cleaned_data['height']
    #     weigh_photo = form.cleaned_data['height']
    #     body_photo = form.cleaned_data['height']
    #     # UserDetails.objects.create()
        return HttpResponseRedirect(reverse('coreapp:data_received'))


class DataReceived(TemplateView):
    template_name = 'data_received.html'