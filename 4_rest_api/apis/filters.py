from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter
from .models import School, Classroom, Teacher, Student

class SchoolFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains', label='School name')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(FilterSet):
    school = NumberFilter(field_name='school__id', label='School ID' )

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(FilterSet):
    school = NumberFilter(
        field_name='classrooms__school__id', 
        distinct=True,
        label='School ID' 
    )
    
    classroom = NumberFilter(
        field_name='classrooms__id', 
        distinct=True,
        label='Classroom ID'
    )
    firstname = CharFilter(lookup_expr='icontains', label='First name')
    lastname = CharFilter(lookup_expr='icontains', label='Last name')
    gender = ChoiceFilter(choices=Teacher.GENDER_CHOICES)

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']

class StudentFilter(FilterSet):
    school = NumberFilter(field_name='classroom__school__id', label='School ID')
    classroom = NumberFilter(field_name='classroom__id', label='Classroom ID')
    firstname = CharFilter(lookup_expr='icontains', label='First name')
    lastname = CharFilter(lookup_expr='icontains', label='Last name')
    gender = ChoiceFilter(choices=Student.GENDER_CHOICES)

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'firstname', 'lastname', 'gender']