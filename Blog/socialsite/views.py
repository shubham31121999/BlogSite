from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserProfile,Post,Comment
from django.core.files.storage import default_storage
from django.utils import timezone
from django.http import JsonResponse
import os
from django.db.models import Prefetch
import uuid
from django.views.decorators.csrf import csrf_exempt




def login(request):
    form_type = None
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'signup':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            date_of_birth = request.POST.get('date_of_birth')
            password = request.POST.get('password')
            
            if not (first_name and last_name and email and date_of_birth and password):
                return render(request, 'login.html', {'error': 'Please fill in all required fields.'})

            try:
                # Create user for authentication
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                UserProfile.objects.create(
                    user=user,
                    date_of_birth=date_of_birth,
                    unique_user_id=uuid.uuid4()
                )
                
                return redirect('login')  # Redirect to a success page or home page
            except IntegrityError:
                return render(request, 'login.html', {'error': 'User with this email already exists.'})
        
        elif form_type == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not (email and password):
                return render(request, 'login.html', {'error': 'Please fill in all required fields.'})

            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main')  
                return render(request, 'login.html', {'error': 'Invalid email or password.'})

    
    return render(request, 'login.html')



def base(request):
    return render(request, 'base.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

@csrf_exempt
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        
        
        if not title or not content or not status:
            return JsonResponse({'error':'Fields are required'})
            
        try:
            
            
                if not request.user.is_authenticated:
                    return JsonResponse({'error': 'User must be logged in to create a post.'}, status=403)
                
                
                
                    
                post = Post(
                    title=title,
                    content = content,
                    status =int(status),
                    author = request.user,
                    image = image
                    
                )
                    
                post.save()
                
                return JsonResponse({'message':'Posted Your Blog'})
            
        except Exception as e:
                
                return JsonResponse({'error':str(e)})
    
    return JsonResponse({'error':'Invalid Request'})


def post_list(request):
    
    if not request.user.is_authenticated:  
        return redirect('login')  

    
    comments = Comment.objects.all()[:2]
    posts = Post.objects.filter(author=request.user).prefetch_related(
        Prefetch('comments', queryset=comments, to_attr='limited_comments')
    )

    return render(request, 'allpost.html', {'posts': posts})




def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.status = int(request.POST.get('status'))
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        return redirect('post_list')  
    return render(request, 'update_post.html', {'post': post})



@login_required
def del_post(request, pk):
    posts = get_object_or_404(Post,pk=pk,author=request.user)
    
    if request.method =='POST':
        posts.delete()
        return redirect('post_list')
    
    return render(request, 'allpost.html',{'posts':posts})


@login_required
def view_single_post(request,post_id):
    post = get_object_or_404(Post, id =post_id)
    return render(request, 'allpost.html',{'post':post})


def comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content =request.POST.get('content')
        if content:
            Comment.objects.create(post=post,author=request.user,content=content)
        
        
    return redirect('main')

def post_detail(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    return render(request, 'post_details.html',{'post':post})


def main(request):
    user = request.user
    userprofile = UserProfile.objects.get(user=user)
    birthday_message = None
    status = request.GET.get('status',None)
    if status:
        posts = Post.objects.filter(status=status)
    else:
        posts = Post.objects.all()
        
    today = timezone.now().date()
    
    
    
    if userprofile.date_of_birth is not None:
            if userprofile.date_of_birth.month == today.month and userprofile.date_of_birth.day == today.day:
                birthday_message = "Happy Birthday, {}!".format(userprofile.user.get_full_name())
                
            else:
                
                birthday_message = None 
                
                
    context = {
        'posts': posts,
        'birthday_message': birthday_message
    }
        
    return render(request, 'post_details.html',context)


def post_like(request,post_id):
    post = get_object_or_404(Post,id = post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('main')