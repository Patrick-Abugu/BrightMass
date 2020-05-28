from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Post
from django.contrib.auth.decorators import login_required
from .import forms
#from django.db.models import Q

# Create your views here.
def home(request):
    content = Post.objects.all()[:50]#.order_by('-date')
    form = forms.FeedbackForm()
    return render(request, 'site/home.html', {'contents': content, 'form':form})

def latest(request):
    things = Post.objects.all()[:10]#.order_by('-date')
    return render(request,'site/latest.html', {'thing': things})


def post_body(request, slug):
    details = Post.objects.get(slug=slug)
    form = forms.FeedbackForm()
    return render(request, 'site/post_body.html', {'details': details, 'form':form})

def about(request):
    return render(request, 'site/about.html')

def services(request):
    return render(request, 'site/services.html')

    #post pages
def page2(request):
    content = Post.objects.all()[51:150]#.order_by('-date')
    return render(request, 'site/page2.html', {'contents': content})

def page3(request):
    content = Post.objects.all()[151:300]#.order_by('-date')
    return render(request, 'site/page3.html', {'contents': content})

def page4(request):
    content = Post.objects.all()[301:]#.order_by('-date')
    return render(request, 'site/page4.html', {'contents': content})

#views for create post form
@login_required(login_url="/profile/login/")
def create_post(request):
    if request.method=='POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            #save post to db
            instance = form.save(commit=False)
            instance.user = request.user #instance.user this user is the one i created as post author in models
            instance.save()
            #save ends
            return redirect('site:home')
    else:
        form = forms.CreatePost()
    return render(request, 'site/create_post.html', {'form': form})


def feedback(request):
    if request.method == 'GET':
            form = forms.FeedbackForm()
    else:
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #form.save(commit=False)
            try:
                send_mail(subject, message, email,  ['patrickabugu@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Feedback not sent! Try again')
            return redirect('site.home')

    return render(request, 'site/home.html', {'form':form})

# views for comment form
