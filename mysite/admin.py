from django.contrib import admin
from mysite.models import POST
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')
    
admin.site.register(POST,PostAdmin)