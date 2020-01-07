from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import TemplateView, UpdateView
from random_word import RandomWords

from coreapp.models import UserDetails


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
        except user_details.DoesNotExist:
            # Generating new random word
            r = RandomWords()
            weigh_word = r.get_random_word()
            context['random_word'] = weigh_word

            # Generating slug
            UserDetails.objects.create(user=self.request.user, weigh_word=weigh_word,
                                       slug=slugify(self.request.user.email))

        context['slug'] = user_details.slug

        return context


class UserData(UpdateView):
    template_name = 'user_details.html'
    model = UserDetails
    fields = [
        'weigh_photo', 'body_photo',
        'weight', 'height'
    ]
    success_url = '/initial-weigh/details/data-received/'


class DataReceived(TemplateView):
    template_name = 'data_received.html'