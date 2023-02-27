from django.contrib import admin
from manag.models import Contact
from manag.models import Doctor
from manag.models import Patient

# Register your models here.
admin.site.register(Contact)
admin.site.register(Doctor)
admin.site.register(Patient)
