from django.db import models


class RepairRequest(models.Model):

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20,choices=[("mobile", "Mobile"),("laptop", "Laptop"),("other", "Other")])
    problem_description = models.TextField()
    pickup_address = models.TextField()
    contact_number = models.CharField(max_length=15)
    pickup_map_location = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20,
        choices=[("pending", "Pending"),("picked", "Picked"),("repairing", "Repairing"),("completed", "Completed")],
        default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category}"


class RepairRequestImage(models.Model):

    repair_request = models.ForeignKey(RepairRequest,related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="repair_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.repair_request.name}"