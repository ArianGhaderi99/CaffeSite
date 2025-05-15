from accounts.models import User
from accounts.form import LoginForm
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from accounts.form import LoginForm,SignupForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

# Create your views here.
class CustomLoginView(LoginView):
    template_name="accounts/Login.html"
    form_class=LoginForm
    success_url=reverse_lazy("base:home")
    
    
class CustomLogoutView(LogoutView):
    next_page=reverse_lazy("acc:login")
    
    
    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        response= super().dispatch(request, *args, **kwargs)
        messages.success(request,"your logout")
        return response
    
    
    
class CustomSignupView(CreateView):
    form_class=SignupForm
    template_name="accounts/signup.html"
    success_url=reverse_lazy("base:home")
    
    
    
    
    
    
class CustomPasswordRest(PasswordResetView):
    template_name='accounts/reset_password.html'
    email_template_name='accounts/reset_password_email.html'
    subject_template_name='accounts/reset_password_subject.txt'
    success_url=reverse_lazy('acc:reset_password_done')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
class CustomPasswordDone(PasswordResetDoneView):
    template_name="accounts/reset_password_done.html"
    
    
class CustomPasswordConfirm(PasswordResetConfirmView):
    template_name='accounts/reset_password_confirm.html'
    success_url=reverse_lazy('acc:reset_password_complete')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
    
class CustomPasswordComplete(PasswordResetCompleteView):
    template_name='accounts/reset_password_complete.html'