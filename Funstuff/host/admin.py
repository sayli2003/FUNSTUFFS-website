from django.contrib import admin
from .models import AddArt

# Register your models here.
class AddForm(admin.ModelAdmin):
    list_display=('title','desp')

admin.site.register(AddArt, AddForm)