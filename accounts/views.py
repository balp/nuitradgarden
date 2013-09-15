# Create your views here.
from django.shortcuts import render

def profile(request):
    context = { 'user': request.user }
    return render(request, 'accounts/profile.html', context)