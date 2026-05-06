from django.db import models
from django.core.validators import MinValueValidator

class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=50, verbose_name='Abbr.')
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    GRADE_CHOICES = [
        ('A1', 'อนุบาล 1'), ('A2', 'อนุบาล 2'), ('A3', 'อนุบาล 3'),
        ('B1', 'ประถม 1'), ('B2', 'ประถม 2'), ('B3', 'ประถม 3'),
        ('B4', 'ประถม 4'), ('B5', 'ประถม 5'), ('B6', 'ประถม 6'),
        ('C1', 'มัธยม 1'), ('C2', 'มัธยม 2'), ('C3', 'มัธยม 3'),
        ('C4', 'มัธยม 4'), ('C5', 'มัธยม 5'), ('C6', 'มัธยม 6'),
    ]

    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    section = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms') # Override name school.classroom_set -> school.classrooms

    def __str__(self):
        return f"{self.get_grade_display()}/{self.section}"

    class Meta:
        unique_together = ['school', 'grade', 'section']

class Teacher(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    classrooms = models.ManyToManyField(Classroom, related_name='teachers') # Override name classrooms.teacher_set -> classrooms.teachers

    def __str__(self):
        title = "Mr." if self.gender == "M" else "Miss."
        return f"{title} {self.firstname} {self.lastname}"

    class Meta:
        unique_together = ['firstname', 'lastname']

class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)

    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students') # Override name classoom.student_set -> classroom.students

    def __str__(self):
        title = "Mr." if self.gender == "M" else "Miss."
        return f"{title} {self.firstname} {self.lastname}"
    
    class Meta:
        unique_together = ['firstname', 'lastname']