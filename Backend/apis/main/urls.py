from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Teacher
    path('teacher', views.TeacherList.as_view()),
    path('teacher/dashboard/<int:pk>/', views.TeacherDashboard.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view()),
    path('teacher-update-password/<int:teacher_id>/',views.teacher_update_password),
    path('teacher-login', views.teacher_login),
    path('popular-teachers/', views.TeacherList.as_view()),
  
    # Category
    path('category/', views.CategoryList.as_view()),

    # Course
     path('course/', views.CourseList.as_view()),
     path('popular-courses/', views.CourseRatingList.as_view()),
     path('update-view/<int:course_id>', views.update_view),

    # Course Detail
    path('course/<int:pk>', views.CourseDetailView.as_view()), 

    # Specific Course Chapter
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()), 

    # Specific Chapter
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),

    # Teacher Courses
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),

    # Course Detail
    path('teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),

    # Student Testimonial
    path('student-testimonial/', views.CourseRatingList.as_view()),

   # Student
    path('student/', views.StudentList.as_view()),
    path('student/update-password/<int:student_id>/',views.student_update_password),
    path('student/<int:pk>/',views.StudentDetail.as_view()),
    path('student/dashboard/<int:pk>/', views.StudentDashboard.as_view()),
    path('student-login', views.student_login),
    path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),
    path('fetch-all-enrolled-students/<int:teacher_id>', views.EnrolledStudentList.as_view()),
    path('fetch-enrolled-students/<int:course_id>', views.EnrolledStudentList.as_view()),
    path('fetch-enrolled-courses/<int:student_id>', views.EnrolledStudentList.as_view()),
    path('course-rating/', views.CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),
    path('student-add-favorite-course/', views.StudentFavoriteCourseList.as_view()),
    path('student-remove-favorite-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),
    path('fetch-favorite-status/<int:student_id>/<int:course_id>', views.fetch_favorite_status),
    path('fetch-favorite-courses/<int:student_id>', views.StudentFavoriteCourseList.as_view()),
    path('student-assignment/<int:teacher_id>/<int:student_id>',views.AssignmentList.as_view()),
    path('update-assignment/<int:pk>',views.UpdateAssignment.as_view()),
    path('my-assignments/<int:student_id>',views.MyAssignmentList.as_view()),
    path('student/fetch-all-notifications/<int:student_id>/',views.NotificationList.as_view()),
    path('save-notification/',views.NotificationList.as_view()),
    path('send-message/<int:teacher_id>/<int:student_id>',views.save_teacher_student_msg),
    path('send-group-message/<int:teacher_id>',views.save_teacher_student_group_msg),
 
    path('send-group-message-from-student/<int:student_id>',views.save_teacher_student_group_msg_from_student),

    path('get-messages/<int:teacher_id>/<int:student_id>',views.MessageList.as_view()),
    
    # Quiz Start
    path('quiz/', views.QuizList.as_view()),
    path('teacher-quiz/<int:teacher_id>', views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),
    path('quiz/<int:pk>', views.QuizDetailView.as_view()),
    path('quiz-questions/<int:quiz_id>', views.QuizQuestionList.as_view()), 
    path('quiz-questions/<int:quiz_id>/<int:limit>', views.QuizQuestionList.as_view()), 
    path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>', views.fetch_quiz_assign_status), 
    path('quiz-assign-course/', views.CourseQuizList.as_view()), 
    path('fetch-assigned-quiz/<int:course_id>',views.CourseQuizList.as_view()),
    path('attempt-quiz/', views.AttemptQuizList.as_view()),
    path('quiz-questions/<int:quiz_id>/next-question/<int:question_id>', views.QuizQuestionList.as_view()),
    path('fetch-quiz-attempt-status/<int:quiz_id>/<int:student_id>', views.fetch_quiz_attempt_status),  

    # Study Materials
    path('study-materials/<int:course_id>', views.StudyMaterialList.as_view()), 
    path('study-material/<int:pk>', views.StudyMaterialDetailView.as_view()), 
    path('user/study-materials/<int:course_id>', views.StudyMaterialList.as_view()), 
    path('attempted-quiz/<int:quiz_id>', views.AttemptQuizList.as_view()), 
    path('fetch-quiz-result/<int:quiz_id>/<int:student_id>', views.fetch_quiz_result_status), 

    path('faq/', views.FAQList.as_view()),

    path('contact/', views.ContactList.as_view()),

    path('fetch-my-teachers/<int:studentId>', views.MyTeacherList.as_view()),

    path('teacher-forgot-password/',views.teacher_forgot_password),
    path('teacher-change-password/<int:teacher_id>/',views.teacher_change_password),

    path('student-forgot-password/',views.student_forgot_password),
    path('student-change-password/<int:student_id>/',views.student_change_password),

    path('verify-teacher/<int:teacher_id>/',views.verify_teacher_via_otp),

    path('verify-student/<int:student_id>/',views.verify_student_via_otp),


   

    
]
