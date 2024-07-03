from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apis.models import ClassRoom
from apis.serializers import ClassRoomSerializer, ClassRoomCreateSerializer, ClassRoomDetailSerializer
from apis.filters import ClassRoomFilter, ClassRoomIdFilter
from apis.utility.base_response import success_response, error_response, exception_response

class ClassRoomAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = ClassRoom.objects.select_related('school')
        if 'school_id' in request.GET:
            filtered_queryset = ClassRoomFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = ClassRoomSerializer(queryset, many=True)
        return success_response(serializer.data)

    def post(self, request):
        serializer = ClassRoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Save Data Success.")
        return error_response(status.HTTP_400_BAD_REQUEST, serializer.errors, None)

class ClassRoomDetailAPIView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['class_room_id']
    def get(self, request):
        queryset = ClassRoom.objects.all()
        if request.query_params:
            filtered_queryset = ClassRoomIdFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = ClassRoomDetailSerializer(queryset, many=True)
        return success_response(serializer.data)
    
class ClassRoomGetByIdView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, id):
        try:
            queryset = ClassRoom.objects.select_related('school').get(class_room_id=id)
            serializer = ClassRoomCreateSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response("Update ClassRoom Success")
        except ClassRoom.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "ClassRoom not found", None)
        except Exception as e:
            return exception_response(str(e))
    
    def delete(self, request, id):
        try:
            queryset = ClassRoom.objects.get(class_room_id=id)
            queryset.delete()
            return success_response("Delete ClassRoom Success")
        except ClassRoom.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "ClassRoom not found", None)
        except Exception as e:
            return exception_response(str(e))