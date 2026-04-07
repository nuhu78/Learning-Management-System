from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('teacher', views.TeacherListCreateView, basename='teacher')
router.register('student', views.StudentListCreateView, basename='student')
router.register('register', views.RegisterView, basename='register')


urlpatterns = [
    path('', include(router.urls)),
   path('login/',views.LoginView.as_view(),name='login'),
]