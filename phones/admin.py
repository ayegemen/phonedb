from django.contrib import admin
from phones.models import Phone, ExtendDate, EmailHistory, SimHistory

class ExtendDateInline(admin.TabularInline):
    model = ExtendDate
    extra = 0
    ordering = ("-date",)

class EmailHistoryInline(admin.TabularInline):
    model = EmailHistory
    extra = 0
    ordering = ("-date",)

class SimHistoryInline(admin.TabularInline):
    model = SimHistory
    extra = 0
    ordering = ("-date",)

class PhoneAdmin(admin.ModelAdmin):
    #fields = ['email', 'imei', 'pin', 'key', 'activation_date', 'phone_model']
    fieldsets = [
        (None, {'fields': ('email', 'imei', 'pin','key', 'phone_model', 'sim', 'branch', 'secure_messaging', 'comment')}),
        ('Date information', {'fields': [('activation_date', 'activation_choice', 'activation_enddate')]}),
    ]
    inlines = [ExtendDateInline, EmailHistoryInline, SimHistoryInline, ]
    list_display = ('email', 'imei', 'pin','sim', 'key', 'activation_and_enddate', 'phone_model', 'extend_dates',)
    list_filter = ['activation_date', 'branch', 'extenddate__date', 'extenddate__extend_branch']
    search_fields = ['email', 'sim', 'emailhistory__email', 'simhistory__sim']


admin.site.register(Phone, PhoneAdmin)