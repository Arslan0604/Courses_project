from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authentication import Authentication
from .authentication import CustomAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        
class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']


# Create your models here.


