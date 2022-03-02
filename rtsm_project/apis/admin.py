from django.contrib import admin
from apis.models.GeneralRegisterModels import GeneralRegister, StudentEnrollment, Incomes, IncomeTypes
from apis.models.ExpensesModel import Expenses, ExpensesTypes, UploadStaffDocsModel, SalaryModel, StaffModel, \
    DesignationModel, RoleModel

admin.site.register(GeneralRegister)
admin.site.register(StudentEnrollment)
admin.site.register(Incomes)
admin.site.register(IncomeTypes)
admin.site.register(Expenses)
admin.site.register(ExpensesTypes)
admin.site.register(UploadStaffDocsModel)
admin.site.register(SalaryModel)
admin.site.register(StaffModel)
admin.site.register(DesignationModel)
admin.site.register(RoleModel)
