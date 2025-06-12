from django.contrib import admin
from .models import Mainservice, Subservicename, OurClient, Career, Enquiries


class MainserviceAdmin(admin.ModelAdmin):
    list_display = ('user','main_service_name', 'created_at')

admin.site.register(Mainservice, MainserviceAdmin)


class SubserviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'main_service_name', 'service_name', 'created_at')

admin.site.register(Subservicename, SubserviceAdmin)


class OurClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'client_logo', 'created_at')

admin.site.register(OurClient, OurClientAdmin)


class CareerAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'job_description', 'job_post_date', 'is_active')

admin.site.register(Career, CareerAdmin)


admin.site.register(Enquiries)