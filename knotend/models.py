from django.contrib.auth.models import User
from django.db import models

COURSES_TAG = [
    ('SY', 'Superyachts'),
    ('OS', 'Offshore'),
    ('SS', 'Safety and Security'),
    ('SG', 'Surveying'),
    ('SP', 'Shipping'),
    ('BR', 'Building and Repair'),
]


class Courses(models.Model):
    title = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to='images', blank=False)
    price = models.CharField(max_length=20, default='3500')
    tag = models.CharField(max_length=20, choices=COURSES_TAG, default='SS')
    duration = models.CharField(max_length=20, default='30')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    rzr_pay_id = models.CharField(max_length=20, default='N/A')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to='images', blank=False)
    description = models.CharField(max_length=255, blank=False)
    datetime = models.DateField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

