from rest_framework import serializers
from apis.models.GeneralRegisterModels import StudentEnrollment, GeneralRegister, Incomes


class GeneralRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralRegister
        fields = "__all__"


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = "__all__"


class IncomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incomes
        fields = "__all__"
