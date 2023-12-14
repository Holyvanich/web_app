from django.contrib import admin
from .models import Client, Employee, Account, Work

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id_account', 'doc_name', 'doc_type','doc_date', 'id_client')
    search_fields=('id_account','doc_name','doc_type','doc_date','id_client')

class ClientAdmin(admin.ModelAdmin):
    list_display=('id_client', 'first_name', 'last_name', 'patronymic', 'date_birth',
                  'id_passport', 'gender', 'phone_number')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id_employee', 'first_name', 'last_name', 'patronymic', 'date_birth',
                  'id_passport', 'gender', 'phone_number', 'position', 'date_employment', 'date_dismissal')


class WorkAdmin(admin.ModelAdmin):
    
    def my_Employee(self, obj):
        return f'{obj.employee.id_employee} {obj.employee.last_name}'
    def my_Documents(self, obj):
        return f'{obj.documents.id_work} {obj.documents.doc_name}'
    def my_phone(self, obj):
        return f'{obj.phone_number}'

    my_Employee.short_description = 'Сотрудник'
    my_phone.short_description = 'Телефон'
    my_Documents.short_description = 'Документ'

    list_display = ('id_work', 'work_status', 'id_employee',)
    search_fields=('id_employee__id_employee','id_employee__last_name')
    list_editable=('work_status',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Work, WorkAdmin)