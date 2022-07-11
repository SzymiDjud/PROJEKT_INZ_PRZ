from django.contrib import admin
from announcements.models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test)
admin.site.register(Test2)