from django.contrib import admin
from . import models

admin.site.site_header = "Course Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Course, CourseAdmin)