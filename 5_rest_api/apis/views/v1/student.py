from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apis.models import Student
from apis.serializers import StudentSerializer, StudentCreateSerializer, StudentDetailSerializer
from apis.filters import StudentFilter, StudentIdFilter
from apis.utility.base_response import success_response, error_response, exception_response

class StudentAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Student.objects.select_related('school', 'class_room')
        if request.query_params:
            filtered_queryset = StudentFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = StudentSerializer(queryset, many=True)
        return success_response(serializer.data)

    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Save Data Success.")
        return error_response(status.HTTP_400_BAD_REQUEST, serializer.errors, None)

class StudentDetailAPIView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_id']
    def get(self, request):
        queryset = Student.objects.all()
        if request.query_params:
            filtered_queryset = StudentIdFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = StudentDetailSerializer(queryset, many=True)
        return success_response(serializer.data)
    
class StudentGetByIdView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, id):
        try:
            queryset = Student.objects.select_related('school', 'class_room').get(student_id=id)
            serializer = StudentCreateSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response("Update Student Success")
        except Student.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "Student not found", None)
        except Exception as e:
            return exception_response(str(e))
    
    def delete(self, request, id):
        try:
            queryset = Student.objects.get(student_id=id)
            queryset.delete()
            return success_response("Delete Student Success")
        except Student.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "Student not found", None)
        except Exception as e:
            return exception_response(str(e))