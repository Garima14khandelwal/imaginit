from django.contrib import admin
from .models import UploadFile
from .models import UserProfile

admin.site.register(UploadFile)
admin.site.register(UserProfile)
