from django.contrib import admin
from .models import SavingPlan, StreamCategory, Stream


# Register your models here.
class SavingPlanAdmin(admin.ModelAdmin):
    list_display = ("target_account", "create_time","current_amount", "allowed_withdraw_date")

class StreamCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "create_date")

class StreamAdmin(admin.ModelAdmin):
    list_display = ("name", "amount")

admin.site.register(SavingPlan, SavingPlanAdmin)
admin.site.register(StreamCategory, StreamCategoryAdmin)
admin.site.register(Stream, StreamAdmin)