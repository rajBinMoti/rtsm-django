from django.db import models


class GeneralRegister(models.Model):
    name_of_student = models.CharField(max_length=256)
    father_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=1)
    caste = models.CharField(max_length=256)
    religion = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=256)
    last_institution_attended = models.CharField(max_length=256)
    date_of_admission = models.DateField()
    admitted_in_class = models.IntegerField()
    date_of_removal = models.DateField()
    class_at_time_of_removal = models.IntegerField()
    cause_of_removal = models.CharField(max_length=256)
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.name_of_student.__str__()


class StudentEnrollment(models.Model):
    gr_id = models.ForeignKey('GeneralRegister', on_delete=models.CASCADE)
    current_class = models.IntegerField()
    admission_fees = models.IntegerField()
    guardian_name = models.CharField(max_length=256)
    guardian_contact = models.CharField(max_length=256)
    monthly_fees = models.IntegerField()
    title_of_position = models.CharField(max_length=256)
    title_of_award = models.CharField(max_length=256)
    date_of_award = models.DateField()
    arrears = models.IntegerField()
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.gr_id.__str__()


class IncomeTypes(models.Model):
    title = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.title.__str__()


class Incomes(models.Model):
    se_id = models.ForeignKey('StudentEnrollment', on_delete=models.CASCADE)
    it_id = models.ForeignKey('IncomeTypes', on_delete=models.CASCADE)
    income_date = models.DateField()
    amount = models.IntegerField()
    remarks = models.CharField(max_length=1024)

    def __str__(self):
        return self.amount.__str__()
