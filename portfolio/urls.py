from django.urls import path
from .views import index_view,books_view,portfolio_view,about_view,Gallery_view,blog_view,ContactFormView

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('books/',books_view,name='books-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('about/',about_view,name='about-page'),
    path('gallery/',Gallery_view,name='gallery-page'),
    path('blog/',blog_view,name='blog-page'),
]
