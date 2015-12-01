from braces.views import LoginRequiredMixin
from class_based_auth_views.views import LoginView
from django.contrib.auth.views import login
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from .forms import LoginWithEmailForm


class IndexView(LoginRequiredMixin, TemplateView):
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.request.user.groups.filter(name="analistas").exists():
            return ["layout_analista.html"]
        elif self.request.user.groups.filter(name="clientes").exists():
            return ["layout_cliente.html"]
        else:
            return ["403.html"]


class MyLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginWithEmailForm


# ----------------TEMPLATES OTROS--------------------------
def panelGestraldi(request):
    return render(request, 'otros/gestraldi.html')


def panelDocumentos(request):
    return render(request, 'otros/documentos.html')

    # ----------------TEMPLATES OTROS--------------------------


class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
