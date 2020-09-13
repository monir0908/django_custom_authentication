from django.conf.urls import url
from . import views
from student.views import StudentRegistration, StudentLoginView


app_name = 'student'
urlpatterns = [
    # register
    url(r'^register/$', StudentRegistration.as_view(), name='register'),
    url(r'^login/$', StudentLoginView.as_view(), name='login'),
]