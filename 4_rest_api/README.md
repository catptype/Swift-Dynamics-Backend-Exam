# README

## Run ครั้งแรกเท่านั้น

1. สร้าง Database `python manage.py migrate`
    > ไม่ต้องรัน `python manage.py makemigrations`
2. สร้าง account admin `python manage.py createsuperuser`
    > ถ้าไม่สร้าง Admin จะติดปัญหาเข้าใช้งานระบบไม่ได้ เพราะค่า `DEFAULT_PERMISSION_CLASSES` ใน settings.py ที่ตั้งไว้ `rest_framework.permissions.IsAuthenticated` เราสามารถข้ามส่วนนี้ได้โดยการเปลี่ยนค่าเป็น `rest_framework.permissions.AllowAny`

## เข้าใช้งานจริง

1. เปิด Server ด้วย developer mode `python manage.py runserver`
2. API ทั้งหมด
    - ดูรายการ API ทั้งหมด: http://127.0.0.1:8000/api/v1/ 
        > รองรับ `GET`
    
    - โรงเรียน: http://127.0.0.1:8000/api/v1/schools/
        > รองรับ `GET` `POST`
    
    - โรงเรียน (Detail): http://127.0.0.1:8000/api/v1/schools/{id}/
        > รองรับ `GET` `PUT` `PACTCH` `DELETE`
    
    - ห้องเรียน: http://127.0.0.1:8000/api/v1/classrooms/
        > รองรับ `GET` `POST`
    
    - ห้องเรียน (Detail): http://127.0.0.1:8000/api/v1/classrooms/{id}/
        > รองรับ `GET` `PUT` `PACTCH` `DELETE`
    
    - ครู: http://127.0.0.1:8000/api/v1/teachers/
        > รองรับ `GET` `POST`
    
    - ครู (Detail): http://127.0.0.1:8000/api/v1/teachers/{id}/
        > รองรับ `GET` `PUT` `PACTCH` `DELETE`
    
    - นักเรียน: http://127.0.0.1:8000/api/v1/students/
        > รองรับ `GET` `PUT`
    
    - นักเรียน (Detail): http://127.0.0.1:8000/api/v1/students/{id}/
        > รองรับ `GET` `PUT` `PACTCH` `DELETE`

3. Header สำคัญที่ควรใช้ในการยิง API
    ```json
    {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    ```

4. Authorization
    ```json
    {
        "type": "Basic Auth",
        "username": "username",
        "password": "password",
    }
    ```
    > ทำกรณี `DEFAULT_PERMISSION_CLASSES` ใน settings.py ที่ตั้งไว้ `rest_framework.permissions.IsAuthenticated`

5. Body Payload สำหรับยิง API เพื่อการสร้างและแก้ไขด้วย `POST` `PUT` `PACTCH` `DELETE` ให้ดู data field ในไฟล์ `serializers.py` ที่เป็น Class `XXXXWriteSerializer` หรือสามารถใช้ผ่าน Web UI ของ Django REST Framework ได้โดยตรง