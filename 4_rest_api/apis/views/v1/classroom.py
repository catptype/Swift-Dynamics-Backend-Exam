from rest_framework import viewsets
from apis.models import Classroom
from apis.serializers import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomWriteSerializer
from apis.filters import ClassroomFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all().select_related('school').prefetch_related('teachers', 'students')
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        # POST, PUT, PATCH
        if self.action in ['create', 'update', 'partial_update']:
            return ClassroomWriteSerializer
        
        # GET /{id}/
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
            
        # GET /
        return ClassroomListSerializer
