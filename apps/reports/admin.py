from django.contrib import admin
from .models.report import Report
# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'report_date', 'generated_by', 'device')
    search_fields = ('report_type', 'generated_by__username', "device__device_name")
    list_filter = ('report_type', 'device')
    ordering = ('-report_date',)
    list_per_page = 20
    list_editable = ('generated_by','device',)