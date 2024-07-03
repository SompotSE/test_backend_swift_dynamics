from rest_framework import serializers
from .models import School, Student, ClassRoom, Teacher, HomeRoom


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.SerializerMethodField()
    teachers_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ('school_id', 'name_th', 'name_en', 'address', 'classrooms_count', 'teachers_count', 'students_count')

    def get_classrooms_count(self, obj):
        return ClassRoom.objects.filter(school_id=obj).count()

    def get_teachers_count(self, obj):
        return Teacher.objects.filter(school_id=obj).count()

    def get_students_count(self, obj):
        return Student.objects.filter(school_id=obj).count()
    
class ClassRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ClassRoomDetailSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    teachers_list = serializers.SerializerMethodField()
    students_list = serializers.SerializerMethodField()

    class Meta:
        model = ClassRoom
        fields = ('class_room_id', 'number_year', 'slash', 'school', 'teachers_list', 'students_list')

    def get_teachers_list(self, obj):
        queryset = HomeRoom.objects.filter(class_room_id=obj)
        home_room = HomeRoomSerializer(queryset, many=True).data
        teachers_list = []
        for th in home_room:
            teachers_list.append(th['teacher'])
        return teachers_list
    
    def get_students_list(self, obj):
        queryset = Student.objects.filter(class_room_id=obj)
        return StudentSerializer(queryset, many=True).data


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherDetailSerializer(serializers.ModelSerializer):
    class_room_list = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('teacher_id', 'first_name', 'last_name', 'gender', 'class_room_list',)
    
    def get_class_room_list(self, obj):
        queryset = HomeRoom.objects.filter(teacher_id=obj)
        home_room = HomeRoomSerializer(queryset, many=True).data
        class_room_list = []
        for th in home_room:
            class_room_list.append(th['class_room'])
        return class_room_list

class HomeRoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeRoom
        fields = '__all__'

class HomeRoomSerializer(serializers.ModelSerializer):
    class_room = ClassRoomCreateSerializer()
    teacher = TeacherCreateSerializer()
    class Meta:
        model = HomeRoom
        fields = '__all__'

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class_room = ClassRoomCreateSerializer()
    school = SchoolSerializer()
    class Meta:
        model = Student
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    class_room = ClassRoomCreateSerializer()

    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'gender', 'class_room',)