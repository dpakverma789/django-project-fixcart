from django.shortcuts import render, redirect
from .models import RepairRequest

def home(request):
    return render(request, 'fixcart_app/index.html')

def about(request):
    return render(request, 'fixcart_app/about.html')


def contact(request):
    if request.method == "POST":
        RepairRequest.objects.create(
            name=request.POST.get("name"),
            category=request.POST.get("category"),
            problem_description=request.POST.get("problem_description"),
            pickup_address=request.POST.get("pickup_address"),
            contact_number=request.POST.get("contact_number"),
            pickup_map_location=request.POST.get("pickup_map_location"),
        )

        return redirect("contact")

    return render(request, "fixcart_app/contact.html")
