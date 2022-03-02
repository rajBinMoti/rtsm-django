from django.db import models


class RoleModel(models.Model):
    title = models.CharField(max_length=256)
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.title.__str__()


class DesignationModel(models.Model):
    title = models.CharField(max_length=256)
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.title.__str__()


class StaffModel(models.Model):
    designation_id = models.ForeignKey("DesignationModel", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=1)
    father_name = models.CharField(max_length=256)
    caste = models.CharField(max_length=256)
    cnic = models.CharField(max_length=256)
    dob = models.DateField()
    qualification = models.CharField(max_length=256)
    date_of_first_appointment = models.DateField()
    contact = models.CharField(max_length=11)
    address = models.CharField(max_length=1024)
    remarks = models.CharField(max_length=1024)


class SalaryModel(models.Model):
    staff_id = models.ForeignKey("StaffModel", on_delete=models.CASCADE)
    designation_id = models.ForeignKey("DesignationModel", on_delete=models.CASCADE)
    salary = models.IntegerField()
    date = models.DateField()
    remarks = models.CharField(max_length=1024)


class ExpensesTypes(models.Model):
    title = models.CharField(max_length=256)
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.title.__str__()


class Expenses(models.Model):
    staff_id = models.ForeignKey("StaffModel", on_delete=models.CASCADE)
    expenses_id = models.ForeignKey("ExpensesTypes", on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()
    remarks = models.CharField(max_length=1024)


class UploadStaffDocsModel(models.Model):
    staff_id = models.ForeignKey("StaffModel", on_delete=models.CASCADE)
    certificate_tile = models.CharField(max_length=256)
    document = models.FileField(upload_to='uploads/')
    remarks = models.CharField(max_length=1024)

