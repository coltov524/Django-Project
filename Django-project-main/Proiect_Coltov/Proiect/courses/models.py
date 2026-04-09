from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import random
import string

def generate_code(length=16):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    materials = models.FileField(upload_to='courses/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            while True:
                slug = generate_code()
                if not Course.objects.filter(slug=slug).exists():
                    self.slug = slug
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Course: {self.title} - Instructor: {self.instructor.username}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Enrollment: {self.student.username} - {self.course.title}"

