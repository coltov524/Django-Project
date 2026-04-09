"""
URL configuration for Proiect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from courses.views import CreateCourseView, EnrollView, CourseDetailView, BoughtCoursesView, SellingCoursesView, EditCourseView, DeleteCourseView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path(
    "change_password",
    auth_views.PasswordChangeView.as_view(
        template_name="change_password.html"
        ),
    name="change_password"
    ),
    path(
    "password-changed/",
    auth_views.PasswordChangeDoneView.as_view(
        template_name="password_changed.html"
        ),
    name="password_change_done" 
    ),
    path("explore", views.ExploreView.as_view(), name="explore"),
    path(
    "logout/",
    auth_views.LogoutView.as_view(next_page="home"),
    name="logout"
    ),
    path('create_course/', CreateCourseView.as_view(), name='create_course'),
    path('enroll/', EnrollView.as_view(), name='enroll'),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course_view'),
    path('course/<slug:slug>/enroll/', EnrollView.as_view(), name='enroll_course'),
    path('bought/', BoughtCoursesView.as_view(), name='bought'),
    path('selling/', SellingCoursesView.as_view(), name='selling'),
    path('course/<slug:slug>/edit/', EditCourseView.as_view(), name='edit_course'),
    path('course/<slug:slug>/delete/', DeleteCourseView.as_view(), name='delete_course'),
    path("delete_account/", views.DeleteUserView.as_view(), name="delete_account"), 
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)