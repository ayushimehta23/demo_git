from django.db import models
from django.core import serializers
from django.core.mail import send_mail

# Teacher Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    profile_img = models.ImageField(upload_to = 'teacher_profile_imgs/', null=True, blank=True)
    skills = models.TextField()
    verify_status=models.BooleanField(default=False)
    otp_digit=models.CharField(max_length=10,null=True, blank=True)
    

    facebook_url=models.URLField(null=True, blank=True)
    twitter_url=models.URLField(null=True, blank=True)
    instagram_url=models.URLField(null=True, blank=True)
    website_url=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "1. Teacher"

    def skill_list(self):
        skill_list=self.skills.split(',')
        return skill_list

    # Total Teacher Courses
    def total_teacher_courses(self):
        total_courses=Course.objects.filter(teacher=self).count()
        return total_courses
    
    # Total Teacher Students
    def total_teacher_students(self):
        total_students=StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_students



# Course Category Model
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2. Course Categories"

    # Total Course of this category
    def total_courses(self):
        return Course.objects.filter(category=self).count()


    def __str__(self):
        return self.title

# Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE,related_name='category_courses')
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_courses')
    title = models.CharField(max_length=150)
    description = models.TextField()
    featured_img = models.ImageField(upload_to = 'course imgs/', null=True)
    techs = models.TextField(null=True)
    course_views= models.BigIntegerField(default=0)
    class Meta:
        verbose_name_plural = "3. Course"

    def related_videos(self):
        related_videos = Course.objects.filter(techs__icontains=self.techs)
        return serializers.serialize('json',related_videos)

    def tech_list(self):
        tech_list=self.techs.split(',')
        return tech_list
    
    def total_enrolled_students(self):
        total_enrolled_students=StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_students

    def course_rating(self):
        course_rating=CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']


    def __str__(self):
        return self.title

# Chapter Model
class Chapter(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to = 'chapter_videos/', null=True)
    remarks = models.TextField(null=True)
    class Meta:
        verbose_name_plural = "4. Chapters"

    def __str__(self):
        return self.title

# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100,blank=True, null=True)
    username = models.CharField(max_length=200)
    interested_categories = models.TextField()
    profile_img = models.ImageField(upload_to = 'student_profile_imgs/', null=True, blank=True)
    verify_status=models.BooleanField(default=False)
    otp_digit=models.CharField(max_length=10,null=True, blank=True)
    
   
    def __str__(self):
        return self.full_name

    def enrolled_courses(self):
        enrolled_courses=StudentCourseEnrollment.objects.filter(student=self).count()
        return enrolled_courses
    
    def favorite_courses(self):
        favorite_courses=StudentFavoriteCourse.objects.filter(student=self).count()
        return favorite_courses

    def complete_assignments(self):
        complete_assignments=StudentAssignemnt.objects.filter(student=self,student_status=True).count()
        return complete_assignments
       

    def pending_assignment(self):
        pending_assignment=StudentAssignemnt.objects.filter(student=self,student_status=False).count()
        return pending_assignment

    class Meta:
        verbose_name_plural = "5. Student"

# Student Course Enrollment
class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='enrolled_courses')
    student= models.ForeignKey(Student,on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="6. Enrolled Courses"

    def __str__(self):
        return f"{self.course}-{self.student}"

# Student Favorite Course
class StudentFavoriteCourse(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="7. Student Favorite Courses"

    def __str__(self):
        return f"{self.course}-{self.student}"

# Course Rating and Reviews
class CourseRating(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    review_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"

    class Meta:
        verbose_name_plural="8. Course Ratings"

class StudentAssignemnt(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    student_status=models.BooleanField(default=False, null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher} - {self.student}"

    class Meta:
        verbose_name_plural="9. Student Assignments"

# Notification Model
class Notification(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    notif_subject=models.CharField(max_length=200, verbose_name="Notification Subject",null=True)
    notif_for=models.CharField(max_length=200, verbose_name="Notification For")
    notif_created_time=models.DateTimeField(auto_now_add=True)
    notifread_status=models.BooleanField(default=False,verbose_name="Notification Status")

    class Meta:
        verbose_name_plural="10. Notification"

# Quiz Model
class Quiz(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    class Meta:
        verbose_name_plural="11. Quiz"

    def __str__(self):
        return f"{self.title}"

    

# Quiz Questions Model
class QuizQuestions(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    questions=models.CharField(max_length=200)
    ans1=models.CharField(max_length=200)
    ans2=models.CharField(max_length=200)
    ans3=models.CharField(max_length=200)
    ans4=models.CharField(max_length=200)
    right_ans=models.CharField(max_length=200)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="12. Quiz Questions"

    def __str__(self):
        return f"{self.questions} - {self.quiz}"

# Add Quiz to Course
class CourseQuiz(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="13. Course Quiz"

    def __str__(self):
        return f"{self.teacher} - {self.course} - {self.quiz}"

# Attempt Quiz Question by Student
class AttemptQuiz(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,null=True)
    right_ans=models.CharField(max_length=200, null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="14. Attempted Question"

    def __str__(self):
        return f"{self.student} - {self.quiz}"

# Study Material Model
class StudyMaterial(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    upload = models.FileField(upload_to = 'study_materials/', null=True)
    remarks = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "15. Course Study Materials"

    def __str__(self):
        return f"{self.course} - {self.title}"

# FAQ Model
class FAQ(models.Model):
    question=models.CharField(max_length=300)
    answer=models.TextField()

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name_plural = "16. FAQ"

class Contact(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    query_txt=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.query_txt

    class Meta:
        verbose_name_plural = "17. Contact Queries"

# Messages
class TeacherStudentChat(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    msg_txt=models.TextField()
    msg_from=models.CharField(max_length=100)
    msg_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "18. Teacher Student Messages"




