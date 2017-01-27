from django.contrib import admin
from .models import CountrUsers, Countries, Articles, Comments
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class CountUserInline(admin.StackedInline):
    model = CountrUsers


class UserAdmin(BaseUserAdmin):
    inlines = (CountUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Countries)
admin.site.register(Articles)
admin.site.register(Comments)
