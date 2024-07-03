from django_filters import rest_framework as filters

from apis.models import School, ClassRoom, Student, Teacher

class SchoolFilter(filters.FilterSet):
    name_th = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name_th']

class SchoolIdFilter(filters.FilterSet):
    school_id = filters.CharFilter(lookup_expr='icontains')
    name_th = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['school_id', 'name_th']

class ClassRoomFilter(filters.FilterSet):
    school_id = filters.NumberFilter(field_name='school__school_id', lookup_expr='exact')
    class Meta:
        model = ClassRoom
        fields = ('school_id',)

class ClassRoomIdFilter(filters.FilterSet):
    class_room_id = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ClassRoom
        fields = ['class_room_id']

class TeacherFilter(filters.FilterSet):
    school_id = filters.NumberFilter(field_name='teacher__school__school_id', lookup_expr='exact')
    class_room_id = filters.NumberFilter(field_name='class_room__class_room_id', lookup_expr='exact')
    first_name =filters.NumberFilter(field_name='teacher__first_name', lookup_expr='exact')
    last_name = filters.NumberFilter(field_name='teacher__last_name', lookup_expr='exact')
    gender = filters.NumberFilter(field_name='teacher__gender', lookup_expr='exact')
    class Meta:
        model = Teacher
        fields = ('school_id', 'class_room_id', 'first_name', 'last_name', 'gender',)

class TeacherIdFilter(filters.FilterSet):
    teacher_id = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Teacher
        fields = ['teacher_id']

class StudentFilter(filters.FilterSet):
    school_id = filters.NumberFilter(field_name='school__school_id', lookup_expr='exact')
    class_room_id = filters.NumberFilter(field_name='class_room__class_room_id', lookup_expr='exact')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    gender = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ('school_id', 'class_room_id', 'first_name', 'last_name', 'gender',)

class StudentIdFilter(filters.FilterSet):
    student_id = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ['student_id']