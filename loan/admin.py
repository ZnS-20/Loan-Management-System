from django.contrib import admin
from .models import LoanTypes, BasicDetails, SalaryTypes, documents
# Register your models here.
# admin.site.register(LoanTypes)
# admin.site.register(BasicDetails)
admin.site.register(SalaryTypes)
# admin.site.register(documents)


@admin.register(LoanTypes)
class LoanTypeView(admin.ModelAdmin):
    list_display = ('type', 'down_payment', 'interest_rate')


@admin.register(BasicDetails)
class BasicDetailView(admin.ModelAdmin):
    list_display = ('id', 'Username', 'loan_type')

    def Username(self, obj):
        return obj.user.user.username


@admin.register(documents)
class DocumentView(admin.ModelAdmin):
    list_display = ('id', 'loan_id_id', 'document_type')
