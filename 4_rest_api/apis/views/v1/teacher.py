from rest_framework import viewsets
from apis.models import Teacher
from apis.serializers import TeacherListSerializer, TeacherDetailSerializer, TeacherWriteSerializer
from apis.filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().prefetch_related('classrooms', 'classrooms__school')
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        # 1. ถ้าเป็นการเขียนข้อมูล (POST, PUT, PATCH)
        if self.action in ['create', 'update', 'partial_update']:
            return TeacherWriteSerializer
        
        # 2. ถ้าเป็นการดูข้อมูลเดี่ยว (GET /{id}/)
        if self.action == 'retrieve':
            return TeacherDetailSerializer
            
        # 3. ถ้าเป็นการดูรายการ (GET /)
        return TeacherListSerializer
