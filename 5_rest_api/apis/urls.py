from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolAPIView, SchoolDetailAPIView, SchoolGetByIdView
from apis.views.v1.classroom import ClassRoomAPIView, ClassRoomGetByIdView, ClassRoomDetailAPIView
from apis.views.v1.student import StudentAPIView, StudentGetByIdView, StudentDetailAPIView
from apis.views.v1.teacher import TeacherAPIView, TeacherToRoomAPIView, TeacherDetailAPIView, TeacherGetByIdView, HomeRoomGetByIdView

router = DefaultRouter()
# router.register(r'school', school.School, basename='School')
# router.register('school', school.School)

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    # path('v1/', include(api_v1_urls)),
    path('v1/school', SchoolAPIView.as_view()),
    path('v1/school/detail', SchoolDetailAPIView.as_view()),
    path('v1/school/id=<str:id>', SchoolGetByIdView.as_view()),

    path('v1/classroom', ClassRoomAPIView.as_view()),
    path('v1/classroom/detail', ClassRoomDetailAPIView.as_view()),
    path('v1/classroom/id=<str:id>', ClassRoomGetByIdView.as_view()),

    path('v1/student', StudentAPIView.as_view()),
    path('v1/student/detail', StudentDetailAPIView.as_view()),
    path('v1/student/id=<str:id>', StudentGetByIdView.as_view()),

    path('v1/teacher', TeacherAPIView.as_view()),
    path('v1/teacher/detail', TeacherDetailAPIView.as_view()),
    path('v1/teacher/to/room', TeacherToRoomAPIView.as_view()),
    path('v1/teacher/id=<str:id>', TeacherGetByIdView.as_view()),
    path('v1/homeroom/id=<str:id>', HomeRoomGetByIdView.as_view()),
]
