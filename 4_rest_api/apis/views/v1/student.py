from rest_framework import viewsets
from apis.models import Student
from apis.serializers import StudentListSerializer, StudentDetailSerializer, StudentWriteSerializer
from apis.filters import StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def get_serializer_class(self):
        # POST, PUT, PATCH
        if self.action in ['create', 'update', 'partial_update']:
            return StudentWriteSerializer
        
        # GET /{id}/
        if self.action == 'retrieve':
            return StudentDetailSerializer
            
        # GET /
        return StudentListSerializer