from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')  # Reference blog/index.html

def about(request):
    return render(request, 'blog/about.html')  # Reference blog/about.html

def contact(request):
    return render(request, 'blog/contact.html')  # Reference blog/contact.html

def faq(request):
    return render(request, 'blog/faq.html')  # Reference blog/faq.html

def feature(request):
    return render(request, 'blog/feature.html')  # Reference blog/feature.html

def team(request):
    return render(request, 'blog/team.html')  # Reference blog/team.html

def service(request):
    return render(request, 'blog/service.html')  # Reference blog/service.html

def testimonial(request):
    return render(request, 'blog/testimonial.html')  # Reference blog/testimonial.html

def project(request):
    return render(request, 'blog/project.html')  # Reference blog/project.html

def custom_404(request, exception):
    return render(request, 'blog/404.html', status=404)  # Reference blog/404.html