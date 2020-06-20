from django.contrib import admin

from .models import User, GlossaryUser

admin.site.register(User)
admin.site.register(GlossaryUser)
