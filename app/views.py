from django.shortcuts import render
from .models import Blog
from hitcount.views import HitCountDetailView
from django.views.generic.edit import FormView
from .form import ContactForm
from .bot import send_message
from django.contrib import messages


# Create your views here.

def home_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def portfolio_view(request):
    return render(request,'portfolio.html')

def resume_view(request):
    return render(request,'resume.html')

def contact_view(request):
    return render(request,'contact.html')

def blog_view(request):
    return render(request,'blog.html')

def singleblog_view(request):
    return render(request,'singleblog.html')

def singleprojectdark_view(request):
    return render(request,'singleprojectdark.html')




# BLOG
def blog_view(request):
    model = Blog.objects.all()
    context = {
        "blogs":model
    }
    return render(request, 'blog.html',context) 

class BlogdetailsView(HitCountDetailView):
    model=Blog
    context_object_name = 'blog'
    template_name='blog-details.html'
    count_hit = True  
    
    


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm  
    success_url = '/contact/'  

    def form_valid(self, form):
        contact = form.save()
        text = f"🆕 Yangi Kontakt:👤 Ism: {contact.firstname}📌 Mavzu: {contact.subject}📝 Xabar: {contact.message}"
        send_message(text)
        messages.success(self.request,  "✅ Xabaringiz muvaffaqiyatli yuborildi!")
        return super().form_valid(form)
