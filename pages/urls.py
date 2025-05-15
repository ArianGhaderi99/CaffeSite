from django.urls import path
from pages import views

app_name='pages'

urlpatterns = [
    path('about/',views.about_viwe,name='about'),
    path('chatbot/',views.chatbot_viwe,name='chatbot'),
    path('contact/',views.CreatContact.as_view(),name='contact'),
    path('',views.CreatOrder.as_view(),name='home'),
]
