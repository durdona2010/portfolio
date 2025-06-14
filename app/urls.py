from django .urls import path
from .views import home_view,about_view,blog_view,ContactFormView,portfolio_view,resume_view,singleblog_view,singleprojectdark_view

urlpatterns = [
path('',home_view , name='home-page'),
path('about/',about_view , name='about-page'),
path('blog/',blog_view , name='blog-page'),
path('contact/', ContactFormView.as_view(), name='contact-page'),
path('portfolio/',portfolio_view , name='portfolio-page'),
path('resume/',resume_view , name='resume-page'),
path('singleblog/',singleblog_view , name='singleblog-page'),
path('singleprojectdark/',singleprojectdark_view , name='singleprojectdark-page')
]