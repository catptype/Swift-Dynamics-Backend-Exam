from django.db.models import Count
from rest_framework import viewsets

from apis.models import School
from apis.serializers import SchoolListSerializer, SchoolDetailSerializer, SchoolWriteSerializer
from apis.filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.annotate(
        classroom_count=Count('classrooms', distinct=True),
        teacher_count=Count('classrooms__teachers', distinct=True),
        student_count=Count('classrooms__students', distinct=True)
    )

    filterset_class = SchoolFilter

    def get_serializer_class(self):
        # POST, PUT, PATCH
        if self.action in ['create', 'update', 'partial_update']:
            return SchoolWriteSerializer
        
        # GET /{id}/
        if self.action == 'retrieve':
            return SchoolDetailSerializer
            
        # GET /
        return SchoolListSerializer