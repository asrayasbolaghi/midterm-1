from django.shortcuts import render
from django.http import HttpResponse
from .models import Services , Services_two , FQA , Pros , Prices , Testimonials

def home(request):
    services = Services.objects.filter(status = True)
    services_two = Services_two.objects.filter(status = True)
    pros = Pros.objects.filter(status = True)
    prices = Prices.objects.filter(status = True)
    testimonials = Testimonials.objects.all()
    fqa = FQA.objects.all()
    context={
        'services':services,
        'services_two': services_two,
        'pros':pros,
        'prices':prices,
        'testimonials':testimonials,
        'fqa':fqa,

             }
    
    return render(request , 'root/index.html' , context=context)
   