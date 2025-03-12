from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import playlist_user
from .forms import User_login_form, Password_reset_email_form, Password_reset_form
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
from youtube_search import YoutubeSearch
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
# import cardupdate


def singup(request):
    if request.method == 'POST':
        form = Singup_form(request.POST)
        if not form.is_valid():
            return HttpResponse("Invalid form")
        
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']

        if password != confirm_password:
            return HttpResponse("Passwords do not match")
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        
        if User.objects.filter(email=email).exists():
           return HttpResponse("Email has already been registered")
        
        user = User.objects.create_user(username=username, email=email,password=password)
        playlist_user.objects.create(username=user)
        return redirect('/login')
    
    form = Singup_form()
    return render(request, 'singup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Invalid credentials")
    
    form = User_login_form()

    return render(request, 'login.html', {'form':form})

def logout(request):
    logout(request)
    return redirect('/login')

#reset password
def password_reset(request):
    if request.method == 'POST':
        form = Password_reset_email_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)

                # Send password reset email
                subject = "Password Reset Requested"
                email_template_name = "registration/password_reset_email.html"
                context = {
                    "email": user.email,
                    "domain": request.META['HTTP_HOST'],
                    "site_name": "Website",
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    "token": default_token_generator.make_token(user),
                    "protocol": "http",
                }
                email = render_to_string(email_template_name, context)
                send_mail(subject, email, 'admin@yourdomain.com', [user.email], fail_silently=False)
                return redirect(reverse('reset_password_done'))
            else:
                return HttpResponse("User does not exist")
    form = Password_reset_email_form()
    return render(request, 'registration/password_reset.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try: 
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if request.method == 'POST':
        form = Password_reset_form(request.POST)
        if form.is_valid() and user is not None and default_token_generator.check_token(user, token):
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            if new_password != confirm_new_password:
                return HttpResponse("Passwords do not match")
            user.set_password(new_password)
            user.save()
            return redirect('/reset_password_complete')
    form = Password_reset_form()
    return render(request, 'registration/password_reset_confirm.html', {'form': form, 'uidb64': uidb64, 'token': token})


f = open('card.json', 'r')
CONTAINER = json.load(f)

def default(request):
    global CONTAINER


    if request.method == 'POST':

        add_playlist(request)
        return HttpResponse("")

    song = 'kSFJGEHDCrQ'
    return render(request, 'player.html',{'CONTAINER':CONTAINER, 'song':song})


def playlist(request):
    cur_user = playlist_user.objects.get(username = request.user)
    try:
      song = request.GET.get('song')
      song = cur_user.playlist_song_set.get(song_title=song)
      song.delete()
    except:
      pass
    if request.method == 'POST':
        add_playlist(request)
        return HttpResponse("")
    song = 'kSFJGEHDCrQ'
    user_playlist = cur_user.playlist_song_set.all()
    # print(list(playlist_row)[0].song_title)
    return render(request, 'playlist.html', {'song':song,'user_playlist':user_playlist})

def search(request):
  if request.method == 'POST':

    add_playlist(request)
    return HttpResponse("")
  try:
    search = request.GET.get('search')
    song = YoutubeSearch(search, max_results=10).to_dict()
    song_li = [song[:10:2],song[1:10:2]]
    # print(song_li)
  except:
    return redirect('/')

  return render(request, 'search.html', {'CONTAINER': song_li, 'song':song_li[0][0]['id']})




def add_playlist(request):
    cur_user = playlist_user.objects.get(username = request.user)

    if (request.POST['title'],) not in cur_user.playlist_song_set.values_list('song_title', ):

        songdic = (YoutubeSearch(request.POST['title'], max_results=1).to_dict())[0]
        song__albumsrc=songdic['thumbnails'][0]
        cur_user.playlist_song_set.create(song_title=request.POST['title'],song_dur=request.POST['duration'],
        song_albumsrc = song__albumsrc,
        song_channel=request.POST['channel'], song_date_added=request.POST['date'],song_youtube_id=request.POST['songid'])
