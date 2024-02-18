from django.urls import path
from .views import (TermDataView,
                    ClassScheduleView,
                    AddcourseView,
                    RemoveCourseView,
                    GetCoursesView,
                    GetScheduleView,)

urlpatterns = [
    path('term/', TermDataView.as_view(), name='term-api'),
    path('class/', ClassScheduleView.as_view(), name='class-api'),
    path('add-course/', AddcourseView.as_view(), name='add-course-api'),
    path('remove-course/', RemoveCourseView.as_view(), name='remove-course-api'),
    path('get-courses/', GetCoursesView.as_view(), name='get-courses-api'),
    path('get-schedule/', GetScheduleView.as_view(), name='get-schedule-api'),
]
