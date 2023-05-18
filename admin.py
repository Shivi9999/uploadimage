from django.contrib import admin

# Register your models here.
from .models import * 
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name','image_filename',)  # Display the filename in the admin list view

    def image_filename(self, obj):
        return obj.images.name  # Assuming your file field is named 'image'

    image_filename.short_description = 'Image Name'  # Set a custom column header

admin.site.register(Multiple, YourModelAdmin)