from django.shortcuts import render
from .models import Contact,Gallery,Blog,Books
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =ContactForm
    success_url = "/"
 
    def form_valid(self,form):
      form.save()
      return super().form_valid(form)


def index_view(request):
 return render(request,'index.html')

def about_view(request):
 return render(request,'about.html')



def portfolio_view(request):
 return render(request, 'portfolio.html')



def Gallery_view(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery":gallery,
    }

    return render(request, 'Gallery.html',context)


def blog_view(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, 'blog.html', context)

def books_view(request):
    books =Books.objects.all()
    context = {
        "books" : books,
    }
    return render(request, 'books.html',context=context)
