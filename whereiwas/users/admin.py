from django.contrib import admin
from .models import Users, Countries, Articles, Comments

# Register your models here.

admin.site.register(Users)
admin.site.register(Countries)
admin.site.register(Articles)
admin.site.register(Comments)
