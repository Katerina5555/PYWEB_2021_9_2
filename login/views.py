from django.views import View
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render


class LoginIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "login/index.html")
