from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def reviews(request):
    return render(request, 'reviews.html')    


# Create your views here.
