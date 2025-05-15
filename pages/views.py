from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from pages.models import Order,Contact
from pages.forms import OrderForm,ContactForm

# Create your views here.
def home_viwe(request):
    return render(request,template_name='base/Home.html')

def about_viwe(request):
    return render(request,template_name='base/About.html')


def chatbot_viwe(request):
    return render(request,template_name='base/Chat_Bot.html')






class CreatOrder(CreateView):
    template_name='base/Home.html'
    success_url=reverse_lazy("base:home")
    model=Order
    form_class=OrderForm
    
    
class CreatContact(CreateView):
    template_name='base/Contact.html'
    success_url=reverse_lazy("base:contact")
    model=Contact
    form_class=ContactForm
    