from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    # Si vous avez un formulaire de connexion personnalisé, vous pouvez également le spécifier ici.
    # form_class = CustomLoginForm
