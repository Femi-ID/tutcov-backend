from django.urls import path
from .views import QuestionListApiView, ListStudentEnrollment, QuestionDetailAPIView, CourseQuestions, QuestionResponseCreateAPIView,EnrollStudentAPIView


urlpatterns = [
    path("questions/all/", QuestionListApiView.as_view(), name="all-questions"),
    path("questions/<str:session>/<str:course_slug>/", QuestionResponseCreateAPIView.as_view(), name="quiz"),
    path("my-courses/", ListStudentEnrollment.as_view(), name="my-enrollments"),
    path("enroll/<str:course_slug>/", EnrollStudentAPIView.as_view(), name="enroll-course"),
    path("<uuid:uuid>/", QuestionDetailAPIView.as_view(), name='single-question'),
    path("<str:session>/<str:course_code>/", CourseQuestions.as_view(), name="course-questions"), 

]