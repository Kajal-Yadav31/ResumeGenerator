from django.db import models
from accounts.models import Account

# Create your models here.
state_choices = (
    ("Andhra Pradesh", "AndhraPradesh"),
    ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ",
                                               "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"),
    ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,
                             blank=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)

    locality = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=100, choices=state_choices, null=True)
    Pin_code = models.CharField(max_length=6, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True)
    Github_link = models.URLField(max_length=200, blank=True)
    About = models.TextField(max_length=700, null=True)

    school_name = models.CharField(max_length=100, null=True)
    scholl_location = models.CharField(max_length=100, null=True)
    College = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=400, null=True)
    project = models.TextField(max_length=300, null=True)
    Work_experience = models.TextField(max_length=500, null=True, blank=True)
    skills = models.TextField(max_length=500, null=True)
    Interest = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(
        upload_to='profilepic', default="pic.jpg", blank=True, null=True)
    certificate = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.first_name} Profile'
