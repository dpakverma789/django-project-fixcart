from django.shortcuts import render, redirect
from .models import RepairRequest, RepairRequestImage

def home(request):
    return render(request, 'fixcart_app/index.html')

def about(request):
    return render(request, 'fixcart_app/about.html')

def thankyou(request):
    return render(request, 'fixcart_app/thankyou.html')

def order(request):
    if request.method == "POST":
        repair_request = RepairRequest.objects.create(
            name=request.POST.get("name"),
            category=request.POST.get("category"),
            problem_description=request.POST.get("problem_description"),
            pickup_address=request.POST.get("pickup_address"),
            contact_number=request.POST.get("contact_number"),
            pickup_map_location=request.POST.get("pickup_map_location"),
        )
        images = request.FILES.getlist("device_images")
        for img in images:
            RepairRequestImage.objects.create(repair_request=repair_request,image=img)
        return redirect("thankyou")
    return render(request, 'fixcart_app/order.html')

def contact(request):
    return render(request, "fixcart_app/contact.html")
