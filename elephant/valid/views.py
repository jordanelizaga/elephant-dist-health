from django.shortcuts import render, redirect

# Create your views here.

def valid(request):
    user = ''
    html = 'valid.html'
    context = {}

    if 'patient' in request.POST:
        user += 'Patient'
    elif 'hc' in request.POST:
        user += 'Pharmacist' 
    elif 'getPatientRecord' in request.POST: 
        return redirect('patient')
    elif 'getPharmacistRecord' in request.POST: 
        return redirect('pharmacist')
    context = { 'user': user }
    return render(request, html, context)