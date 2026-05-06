from django.contrib import admin
from .models import School, Classroom, Teacher, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'address')
    search_fields = ('name', 'abbreviation')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('school', 'grade', 'section')
    list_filter = ('school', 'grade')
    search_fields = ('school__name', 'grade')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'gender')
    list_filter = ('gender',)
    search_fields = ('firstname', 'lastname')
    filter_horizontal = ('classrooms',)  # ช่วยให้เลือกห้องเรียนได้ง่ายขึ้นมาก

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'gender', 'classroom')
    list_filter = ('gender', 'classroom__school')
    search_fields = ('firstname', 'lastname')