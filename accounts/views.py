from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import userProfiles, posts, Friends
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import re

# Create your views here.

# Home page view


def Home(request):
    return render(request, 'Home.html')

# Login page view


def Login(request):
    if request.method == 'GET':

        return render(request, 'Login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            return redirect('/')
        else:
            return render(request, 'Login.html', {'massage': 'You are not authorized'})
# Register page view


def Register(request):
    if request.method == 'GET':

        return render(request, 'Register.html')
    else:
        firstName = request.POST["firstName"]
        middleName = request.POST["middleName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        DOB = request.POST["DOB"]
        username = request.POST["username"]
        password = request.POST["password"]
        profile = request.FILES["profilePic"]
        username_pattern=r'^([a-zA-Z]{2,})([!@#$%&*]*)([0-9]*)$'
        password_pattern=r'^([a-zA-Z]+)([!@#$%&*]+)([0-9]+)$'
        username_check=re.search(username_pattern,username)
        password_pattern=re.search(password_pattern,password)
        if(username_check==None or password_pattern==None):
            return render(request,'Register.html',{"error":"Either username or password is not in correct format.Username must contain atleast two character For password the format is characters followed by special character folllowed by digits"})
        
        else:
            user = User.objects.create_user(password=password, username=username, first_name=firstName,
                                        last_name=lastName, email=email)
            user.save()
            ins = userProfiles.objects.create(
            username=username, profile_pics=profile, middle_name=middleName, DOB=DOB)
            ins.save()
            return redirect('/')

# Profile page view


def Profile(request):
    username = request.session['username']
    data = User.objects.get(username=username)
    userdata = userProfiles.objects.get(username=username)

    context = {
        "username": data.username,
        "email": data.email,
        "first_name": data.first_name,
        "last_name": data.last_name,
        "profile_pic": userdata.profile_pics.url,
        "middle_name": userdata.middle_name,
        "DOB": userdata.DOB
    }

    return render(request, 'Profile.html', context)

# view  for logout


def logout(request):
    auth.logout(request)
    return redirect('/')


def uploadPost(request):
    if request.method == 'GET':
        return render(request, 'UploadPost.html')
    else:
        img = request.FILES["postImageinput"]
        caption = request.POST['caption']
        privacy = request.POST['privacy']
        username = request.session['username']
        data = User.objects.get(username=username)
        owner_username = username

        p1 = posts.objects.create(owner_username=owner_username, privacy=privacy,
                                  post_image=img, captions=caption)
        p1.save()
        return redirect('/')


def Posts(request):
    post = posts.objects.filter(privacy="public")
    print(post)
    post_list = {
        'post': post
    }
    return render(request, 'Posts.html', post_list)


def searchFriends(request):
    if request.method == 'GET':

        return render(request, 'SearchFriends.html')
    else:
        username = request.session['username']
        friends = Friends.objects.filter(
            friends2=username)
        friends_list = []
        for i in friends:
            friends_list.append(i.friends1)

        print(friends_list)

        search_text = request.POST['search_text']
        search_result = User.objects.filter(
            username__contains=search_text).exclude(username=username)
        context = {'friends': friends_list, 'search_result': search_result}

        print(search_result)
        return render(request, 'SearchFriends.html', context)


@csrf_exempt
def addFollowers(request):
    data = json.loads(request.body)
    reciever = data['accountHolder']
    sender = data['folllowerUsername']
    friends = Friends.objects.create(friends1=reciever, friends2=sender)
    friends.save()
    print(reciever)
    return JsonResponse({'status': 'success'})


def Feeds(request):
    username = request.session['username']
    friends = Friends.objects.filter(
        friends2=username)
    friends_list = []
    for i in friends:
        friends_list.append(i.friends1)

    feeds = posts.objects.filter(owner_username__in=friends_list)
    context = {
        'feeds': feeds
    }
    return render(request, 'Feeds.html', context)


