from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apis.models import School
from apis.serializers import SchoolSerializer, SchoolDetailSerializer
from apis.filters import SchoolFilter, SchoolIdFilter
from apis.utility.base_response import success_response, error_response, exception_response

class SchoolAPIView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_th']
    def get(self, request):
        queryset = School.objects.all()
        if request.query_params:
            filtered_queryset = SchoolFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = SchoolSerializer(queryset, many=True)
        return success_response(serializer.data)
    
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Save Data Success.")
        return error_response(status.HTTP_400_BAD_REQUEST, serializer.errors, None)


class SchoolDetailAPIView(APIView):
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['school_id', 'name_th']
    def get(self, request):
        queryset = School.objects.all()
        if request.query_params:
            filtered_queryset = SchoolIdFilter(request.GET, queryset=queryset).qs
            queryset = filtered_queryset
        serializer = SchoolDetailSerializer(queryset, many=True)
        return success_response(serializer.data)


class SchoolGetByIdView(APIView):
    permission_classes = [AllowAny]
    def put(self, request, id):
        try:
            queryset = School.objects.get(school_id=id)
            serializer = SchoolSerializer(queryset, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return success_response("Update School Success")
        except School.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "School not found", None)
        except Exception as e:
            return exception_response(str(e))
    
    def delete(self, request, id):
        try:
            queryset = School.objects.get(school_id=id)
            queryset.delete()
            return success_response("Delete School Success")
        except School.DoesNotExist:
                return error_response(status.HTTP_404_NOT_FOUND, "School not found", None)
        except Exception as e:
            return exception_response(str(e))
    # queryset= School.objects.all()
    # serializer_class = SchoolSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name_th']
    
    # def List(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     print(self.queryset)

    #     return super().create(request, *args, **kwargs)
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     print(self.queryset)

    #     return super().create(request, *args, **kwargs)