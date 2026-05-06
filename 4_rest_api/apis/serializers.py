from rest_framework import serializers
from .models import School, Classroom, Teacher, Student
################################
###          SCHOOL          ###
################################
class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']

class SchoolDetailSerializer(SchoolListSerializer):
    counter = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'counter']

    def get_counter(self, obj) -> dict:
        return {
            "classroom": getattr(obj, 'classroom_count', 0),
            "teacher": getattr(obj, 'teacher_count', 0),
            "student": getattr(obj, 'student_count', 0)
        }

class SchoolWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'abbreviation', 'address']

################################
###        CLASSROOM         ###
################################    
class ClassroomListSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(source='school.id')
    grade_code = serializers.CharField(source='grade')
    grade_display = serializers.CharField(source='get_grade_display')

    class Meta:
        model = Classroom
        fields = ['id', 'school_id', 'grade_code', 'grade_display', 'section']

class ClassroomDetailSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name')
    grade_display = serializers.CharField(source='get_grade_display')
    teachers = serializers.StringRelatedField(many=True)
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Classroom
        fields = ['id', 'school_name', 'grade_display', 'section', 'teachers', 'students']

class ClassroomWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['grade', 'section', 'school']

################################
###         TEACHER          ###
################################
class TeacherListSerializer(serializers.ModelSerializer):
    classroom_ids = serializers.SerializerMethodField()
    school_ids = serializers.SerializerMethodField()

    def get_classroom_ids(self, obj: Teacher) -> list:
        return list(obj.classrooms.values_list('id', flat=True))

    def get_school_ids(self, obj: Teacher) -> list:
        return list(set(obj.classrooms.values_list('school_id', flat=True)))
    
    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender', 'classroom_ids', 'school_ids']

class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = serializers.SerializerMethodField()

    def get_classrooms(self, obj: Teacher) -> list:
        data = []
        for classroom in obj.classrooms.all():
            school_name = classroom.school.name
            grade_display = classroom.get_grade_display()
            section = classroom.section
            data.append(f"{school_name} {grade_display}/{section}")
        
        return sorted(list(data))

    class Meta:
        model = Teacher
        fields = ['id', 'firstname', 'lastname', 'gender', 'classrooms']

class TeacherWriteSerializer(serializers.ModelSerializer):
    classrooms = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Classroom.objects.all(),
        required=False
    )
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'gender', 'classrooms']

################################
###         STUDENT          ###
################################
class StudentListSerializer(serializers.ModelSerializer):
    classroom_id = serializers.IntegerField(source='classroom.id')
    school_id = serializers.IntegerField(source='classroom.school_id')

    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'gender', 'classroom_id', 'school_id']

class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()

    def get_classroom(self, obj: Student) -> str:
        c = obj.classroom
        return f"{c.school.name} {c.get_grade_display()}/{c.section}"

    class Meta:
        model = Student
        fields = ['id', 'firstname', 'lastname', 'gender', 'classroom']

class StudentWriteSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(
        queryset=Classroom.objects.all(),
        required=False,
        allow_null=True
    )
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'gender', 'classroom']
