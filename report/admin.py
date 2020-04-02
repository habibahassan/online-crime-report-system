from django.contrib import admin
from .models import CaseStatus,Complaint,Fir,CopStatus,CaseClose

admin.site.register(CaseStatus)
admin.site.register(Complaint)
admin.site.register(Fir)
admin.site.register(CopStatus)
admin.site.register(CaseClose)