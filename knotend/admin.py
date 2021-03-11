from django.contrib import admin

# Register your models here.
from knotend.models import Courses, Blog

admin.site.register(Courses)
admin.site.register(Blog)
