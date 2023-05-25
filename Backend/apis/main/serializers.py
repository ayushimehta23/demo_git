from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'full_name', 'email', 'qualification', 'mobile_no', 'skills', 'profile_img', 'teacher_courses', 'skill_list', 'total_teacher_courses']
        depth = 1

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_courses', 'total_teacher_students']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'category', 'teacher', 'title', 'description', 'featured_img', 'techs', 'course_chapters', 'related_videos', 'tech_list', 'total_enrolled_students', 'course_rating']
        
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
        fields = ['id', 'full_name', 'email', 'password', 'username', 'interested_categories', 'profile_img']
    
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