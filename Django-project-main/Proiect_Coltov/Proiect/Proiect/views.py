from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from courses.models import Course, Enrollment
from django.contrib.auth import logout

class DeleteUserView(LoginRequiredMixin, View):
    template_name = "delete_account.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = request.user
        logout(request)   
        user.delete()     

        return redirect("home")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
    

class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, self.template_name, {
                "error": "Invalid username or password"
            })
    

class SignupView(View):
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        username = request.POST.get("username")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return render(request, self.template_name, {
                "form": form,
                "error": "Username already taken"
            })

        if User.objects.filter(email__iexact=email).exists():
            return render(request, self.template_name, {
                "form": form,
                "error": "Email already in use"
            })

        if form.is_valid():
            user = form.save()

            
            send_mail(
                subject='Welcome to Colțov Academy!',
                message=f'Hi {user.username}, thanks for signing up!',
                from_email='noreply@coltov.com',  
                recipient_list=[user.email],
                fail_silently=False,
            )
            

            return redirect('login')

        return render(request, self.template_name, {"form": form})


class ProfileView(LoginRequiredMixin, View):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name)


class ExploreView(LoginRequiredMixin, View):
    template_name = "CoursesList.html"

    def get(self, request):
        enrolled_courses = Enrollment.objects.filter(
            student=request.user
        ).values_list('course_id', flat=True)
        
        courses = Course.objects.exclude(
            id__in=enrolled_courses
        ).exclude(
            instructor=request.user
        ).order_by('-created_at')

        return render(request, self.template_name, {'courses': courses})

class DeleteUserView(LoginRequiredMixin, View):
    template_name = "delete_account.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = request.user
        logout(request)   
        user.delete()     

        return redirect("home")