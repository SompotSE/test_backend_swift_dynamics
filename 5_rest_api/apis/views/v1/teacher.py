from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apis.models import Teacher, HomeRoom
from apis.serializers import TeacherCreateSerializer, HomeRoomSerializer, HomeRoomCreateSerializer, TeacherDetailSerializer
from apis.filters import TeacherFilter, TeacherIdFilter
from apis.utility.base_response import success_response, error_response, exception_response

class TeacherAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = HomeRoom.objects.select_related('teacher', 'class_room')
        if request.query_params:
            filtered_queryset = TeacherFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = HomeRoomSerializer(queryset, many=True)
        teacher = []
        for th in serializer.data:
            teacher.append(th['teacher'])
        return success_response(teacher)

    def post(self, request):
        serializer = TeacherCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Save Data Success.")
        return error_response(status.HTTP_400_BAD_REQUEST, serializer.errors, None)

class TeacherToRoomAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        teacher_to_room = HomeRoom.objects.filter(**request.data).count()
        if teacher_to_room > 0:
            return error_response(status.HTTP_400_BAD_REQUEST, "The teacher is already in this room.", None)
        serializer = HomeRoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Save Data Success.")
        return error_response(status.HTTP_400_BAD_REQUEST, serializer.errors, None)

class TeacherDetailAPIView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['teacher_id']
    def get(self, request):
        queryset = Teacher.objects.all()
        if request.query_params:
            filtered_queryset = TeacherIdFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = TeacherDetailSerializer(queryset, many=True)
        return success_response(serializer.data)
    
class TeacherGetByIdView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, id):
        try:
            queryset = Teacher.objects.select_related('school').get(teacher_id=id)
            serializer = TeacherCreateSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response("Update Teacher Success")
        except Teacher.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "Teacher not found", None)
        except Exception as e:
            return exception_response(str(e))
    
    def delete(self, request, id):
        try:
            queryset = Teacher.objects.get(teacher_id=id)
            queryset.delete()
            return success_response("Delete Teacher Success")
        except Teacher.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "Teacher not found", None)
        except Exception as e:
            return exception_response(str(e))
        
class HomeRoomGetByIdView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, id):
        try:
            teacher_to_room = HomeRoom.objects.filter(**request.data).count()
            if teacher_to_room > 0:
                return error_response(status.HTTP_400_BAD_REQUEST, "The teacher is already in this room.", None)
            queryset = HomeRoom.objects.get(home_room_id=id)
            serializer = HomeRoomCreateSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response("Update HomeRoom Success")
        except HomeRoom.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "HomeRoom not found", None)
        except Exception as e:
            return exception_response(str(e))
    
    def delete(self, request, id):
        try:
            queryset = HomeRoom.objects.get(home_room_id=id)
            queryset.delete()
            return success_response("Delete HomeRoom Success")
        except HomeRoom.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "HomeRoom not found", None)
        except Exception as e:
            return exception_response(str(e))