from django.views import View
from django.shortcuts import render
from django.http.response import HttpResponse


class HomeView(View):
    def get(self, request):
        return HttpResponse('welcome to home')
