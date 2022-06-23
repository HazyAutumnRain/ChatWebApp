from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.
def default_view(request):
    return render(request, "base/home.html")

class CustomLoginView(LoginView):
    template_name: str = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user: bool = True

    def get_success_url(self) -> str:
        return reverse_lazy("home")

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(CustomLoginView, self).get(*args, **kwargs)
    

class CustomRegisterView(FormView):
    template_name: str = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(CustomRegisterView, self).get(*args, **kwargs)