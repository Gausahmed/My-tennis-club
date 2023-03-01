from django.contrib import admin
from .models import Hello

# admin.site.register(Hello)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname")

admin.site.register(Hello, MemberAdmin)