from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Logo, Skills, Project, Experience,Contact

admin.site.register(Logo)
admin.site.register(Skills)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Contact)