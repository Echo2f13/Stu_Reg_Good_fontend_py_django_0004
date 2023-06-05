from django.contrib import admin
from .models import StudentData, CourseData, RegisteredData

admin.site.register(StudentData)
admin.site.register(CourseData)
admin.site.register(RegisteredData)
