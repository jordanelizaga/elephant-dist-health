from django.shortcuts import render

# Create your views here.

def pharmacist(request):
    user = ''
    html = 'pharmacist.html'
    context = { 'user': user }
    return render(request, html, context)