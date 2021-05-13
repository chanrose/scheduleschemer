from django.urls import path, include
from . import views

app_name = 'ssapp'

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path('curriculum', views.UserCurriculum.as_view(), name='curriculum'),
    path('course', views.UserEnrollCourse.as_view(), name='course'),
    path('<str:pk>/profile', views.DetailProfile.as_view(), name='profile'),
    path('signup', views.Signup.as_view(), name='signup'),

    path('admin/course', views.AdminCourse.as_view(), name="admin_course"),
    path('admin/<str:pk>/course', views.AdminDetailCourse.as_view(), name="admin_class"),
    path('admin/course/update', views.UpdateSchedule, name="update_schedule"),
    path("admin/curriculum", views.AdminCurriculum.as_view(), name="admin_curriculum"),
    path("admin/<int:pk>/curriculum", views.AdminDetailCurriculum.as_view(), name="admin_detail_curriculum"),
    path("admin/<int:curr_id>/curriculum/<str:course_id>/drop", views.drop_course_from_curriculum, name='drop_course_from_curriculum'),


]
