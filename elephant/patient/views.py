from django.shortcuts import render

# Create your views here.

def patient(request):
    user = ''
    html = 'patient.html'
    context = { 'user': user }
    return render(request, html, context)