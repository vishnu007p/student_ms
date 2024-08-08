"""
URL configuration for student_management_system app.

"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('studentreg',views.studentreg, name='studentreg'),
    path('studentlogin',views.studentlogin, name='studentlogin'),
    path('coursedetails',views.coursedetails, name='coursedetails'),
    path('course/<str:coursename>/', views.coursestudent, name='coursestudent')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
