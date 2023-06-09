from rest_framework import serializers
from . import models
from django.contrib.flatpages.models import FlatPage
from django.core.mail import send_mail
from django.conf import settings

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'password', 'email', 'qualification', 'mobile_no', 'skills', 'profile_img', 'teacher_courses', 'skill_list', 'total_teacher_courses', 'facebook_url', 'twitter_url', 'instagram_url', 'website_url', 'otp_digit', 'verify_status']
        depth = 1

    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

    def create(self, validate_data):
        email=self.validated_data['email']
        otp_digit=self.validated_data['otp_digit']
        instance=super(TeacherSerializer, self).create(validate_data)

        subject = 'Welcome to Course Portal'
        message = f"Hello, \n\nWelcome to course portal. \n\nYour OTP for registration is {otp_digit}. \n\nThank you for connecting with us. \n\n\nBest Regards,\nCourse Portal."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ayushimehta9515@gmail.com']
        send_mail( subject, message, email_from, recipient_list )

        return instance

    


class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_courses', 'total_teacher_students']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description', 'total_courses']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'featured_img', 'techs', 'course_chapters', 'related_videos', 'tech_list', 'total_enrolled_students', 'course_rating', 'course_views']
        
    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chapter
        fields = ['id', 'course', 'title', 'description', 'video', 'remarks']

    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'full_name', 'email', 'password', 'username', 'interested_categories', 'profile_img', 'otp_digit', 'verify_status']


    def __init__(self, *args, **kwargs):
        super(StudentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

    def create(self, validate_data):
        email=self.validated_data['email']
        otp_digit=self.validated_data['otp_digit']
        instance=super(StudentSerializer, self).create(validate_data)

        subject = 'Welcome to Course Portal'
        message = f"Hello, \n\nWelcome to course portal. \n\nYour OTP for registration is {otp_digit}. \n\nThank you for connecting with us. \n\n\nBest Regards,\nCourse Portal."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ayushimehta9515@gmail.com']
        send_mail( subject, message, email_from, recipient_list )

        return instance

    
class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentCourseEnrollment
        fields = ['id', 'course', 'student', 'enrolled_time']
    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth = 2

# class StudentCourseEnrollCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.StudentCourseEnrollment
#         fields = ['id', 'course', 'student', 'enrolled_time']


class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentFavoriteCourse
        fields=['id','course','student','status']
    def __init__(self, *args, **kwargs):
        super(StudentFavoriteCourseSerializer,self).__init__(*args, **kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth=2

class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseRating
        fields = ['id', 'course', 'student', 'rating', 'reviews', 'review_time']
    
    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class StudentAssignemntSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentAssignemnt
        fields = ['id', 'teacher', 'student', 'title', 'detail', 'student_status','add_time']

    def __init__(self, *args, **kwargs):
        super(StudentAssignemntSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class StudentDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=['enrolled_courses', 'favorite_courses', 'complete_assignments', 'pending_assignment']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Notification
        fields=['teacher', 'student', 'notif_subject', 'notif_for', 'notif_created_time', 'notifread_status']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['id', 'teacher', 'title', 'detail', 'assign_status', 'add_time']

    def __init__(self, *args, **kwargs):
        super(QuizSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestions
        fields = ['id', 'quiz', 'questions', 'ans1', 'ans2', 'ans3', 'ans4', 'right_ans']

    def __init__(self, *args, **kwargs):
        super(QuestionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseQuiz
        fields = ['id', 'teacher', 'course', 'quiz', 'add_time']
    def __init__(self, *args, **kwargs):
        super(CourseQuizSerializer, self).__init__(*args, **kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class AttemptQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttemptQuiz
        fields = ['id', 'student', 'question', 'right_ans', 'add_time', 'quiz']
    def __init__(self, *args, **kwargs):
        super(AttemptQuizSerializer, self).__init__(*args, **kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method == 'GET':
            self.Meta.depth = 2

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyMaterial
        fields = ['id', 'course', 'title', 'description', 'upload', 'remarks']

    def __init__(self, *args, **kwargs):
        super(StudyMaterialSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ['question', 'answer']

class FlatPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlatPage
        fields = ['id', 'title', 'content', 'url']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Contact
        fields = ['id', 'full_name', 'email', 'query_txt']

class TeacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TeacherStudentChat
        fields = ['id', 'teacher', 'student', 'msg_txt', 'msg_from', 'msg_time']
    
    def to_representation(self, instance):
        representation = super(TeacherStudentChatSerializer, self).to_representation(instance)
        representation['msg_time'] = instance.msg_time.strftime("%Y-%m-%d %H:%M")
        return representation
