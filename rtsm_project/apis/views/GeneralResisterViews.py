from rest_framework.response import Response
from apis.models.GeneralRegisterModels import GeneralRegister, StudentEnrollment, Incomes
from apis.serializers.GeneralResisterSerializer import GeneralRegisterSerializer, StudentEnrollmentSerializer, IncomesSerializer
from rest_framework.views import APIView


class ListGeneralRegister(APIView):
    def get(self, request):
        entries = GeneralRegister.objects.all()
        serializer = GeneralRegisterSerializer(entries, many=True)
        return Response(serializer.data)


class GeneralRegisterDetailView(APIView):
    def get(self, request, pk):
        entries = GeneralRegister.objects.get(id=pk)
        serializer = GeneralRegisterSerializer(entries, many=False)
        return Response(serializer.data)


class CreateGeneralRegister(APIView):
    def post(self, request):
        serializer = GeneralRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class UpdateGeneralRegister(APIView):
    def post(self, request, pk):
        entry = GeneralRegister.objects.get(id=pk)
        serializer = GeneralRegisterSerializer(
            instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DeleteGeneralRegister(APIView):
    def post(self, request, pk):
        # entry = GeneralRegister.objects.get(id=pk)
        entry_instance = GeneralRegister.objects.get(id=pk)
        entry_instance.delete()
        return Response('Deleted')
