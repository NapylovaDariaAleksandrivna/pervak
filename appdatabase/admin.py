from django.contrib import admin

# Register your models here.
from .models import User, Data,Feedback

admin.site.register(User)
admin.site.register(Data)
admin.site.register(Feedback)