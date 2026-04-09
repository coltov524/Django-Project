from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Course, Enrollment
from .forms import CourseForm, EnrollmentForm
from django.views.generic import DetailView 
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail 

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'create_course.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class EnrollView(LoginRequiredMixin, View):

    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        return render(request, 'enroll.html', {'course': course})

    def post(self, request, slug):
        course = get_object_or_404(Course, slug=slug)

        if course.instructor == request.user:
            return HttpResponseForbidden("You cannot enroll in your own course.")

        if Enrollment.objects.filter(student=request.user, course=course).exists():
            return HttpResponseForbidden("You are already enrolled in this course.")

        Enrollment.objects.create(
            student=request.user,
            course=course,
            
        )
        
        send_mail(
                subject='Enrollment',
                message=f'Hi {request.user.username}, You enrolled in a new course!',
                from_email='noreply@coltov.com',  
                recipient_list=[request.user.email],
                fail_silently=False,
            )
        
        return redirect('course_view', slug=course.slug)

class CourseDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        course = get_object_or_404(Course, slug=slug)
        is_instructor = course.instructor == request.user
        is_enrolled = Enrollment.objects.filter(course=course, student=request.user).exists()

        if not (is_instructor or is_enrolled):
            return HttpResponseForbidden("You do not have permission to view this course.")

        return render(request, 'viewcourse.html', {'course': course})
    
class BoughtCoursesView(LoginRequiredMixin, View):
    template_name = "bought_courses.html"

    def get(self, request):
        enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
        
        courses = Course.objects.filter(id__in=enrolled_courses).order_by('-created_at')

        return render(request, self.template_name, {'courses': courses})

class SellingCoursesView(LoginRequiredMixin, View):
    template_name = "selling_courses.html"

    def get(self, request):
        courses = Course.objects.filter(instructor=request.user).order_by('-created_at')
        
        return render(request, self.template_name, {'courses': courses})
    
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin



class EditCourseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'edit.html'

    def form_valid(self, form):
        if 'materials' in self.request.FILES:
            old_file = self.get_object().materials
            if old_file:
                old_file.delete(save=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('selling')

    def test_func(self):
        course = self.get_object()
        return course.instructor == self.request.user


class DeleteCourseView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'delete.html'
    success_url = reverse_lazy('selling')

    def test_func(self):
        course = self.get_object()
        return course.instructor == self.request.user