from django.contrib import admin
from django.urls import path
from blog import views

handler404 = 'blog.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Homepage
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('faq/', views.faq, name='faq'),  # FAQ page
    path('feature/', views.feature, name='feature'),  # Feature page
    path('team/', views.team, name='team'),  # Team page
    path('service/', views.service, name='service'),  # Service page
    path('testimonial/', views.testimonial, name='testimonial'),  # Testimonial page
    path('project/', views.project, name='project'),  # Project page
]