from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import uuid
from accounts.models import Profile, ValidLink
from django.core.mail import send_mail
from django.conf import settings
from words.models import Score, CorrectWord

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST['user_or_email'])
        except:
            try:
                User.objects.get(email=request.POST['user_or_email'])
            except:
                return render(request, 'accounts/login.html', {'message':'account does not exist.'})
            user =  User.objects.filter(email=request.POST['user_or_email']).values('username')
            username = user[0]['username']
            user = auth.authenticate(username=username, password=request.POST['password'])
            if user is not None:
                try:
                    profile_obj = Profile.objects.get(user=user)
                    if not profile_obj.is_verified:
                        return render(request, 'accounts/login.html',
                                      {'message': 'Your account is not verified. Check your email.'})
                    else:
                        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('index')
                except:
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
            else:
                return render(request, 'accounts/login.html', {'message': 'Invalid username/email or password'})
        user = auth.authenticate(username=request.POST['user_or_email'], password=request.POST['password'])
        if user is not None:
            try:
                profile_obj = Profile.objects.get(user=user)
                if not profile_obj.is_verified:
                    return render(request, 'accounts/login.html',
                                  {'message': 'Your account is not verified. Check your email.'})
                else:
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
            except:
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'message': 'Invalid username/email or password'})
    else:
        return render(request, 'accounts/login.html')

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     if request.method == 'POST':
#         try:
#             User.objects.get(username=request.POST['user_or_email'])
#         except:
#             try:
#                 User.objects.get(email=request.POST['user_or_email'])
#             except:
#                 return render(request, 'accounts/login.html', {'message':'Account does not exist'})
#             user = User.objects.filter(email=request.POST['user_or_email']).values('username')
#             username = user[0]['username']
#             user = auth.authenticate(username=username, password=request.POST['password'])
#             if user is not None:
#                 try:
#                     profile_obj = Profile.objects.get(user=user)
#                     if not profile_obj.is_verified:
#                         return render(request, 'accounts/login.html',
#                                       {'message': 'Your account is not verified. Check your email.'})
#                     else:
#                         auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                         return redirect('index')
#                 except:
#                     auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                     return redirect('index')
#         user = auth.authenticate(username=request.POST['user_or_email'], password=request.POST['password'])
#         if user is not None:
#             try:
#                 profile_obj = Profile.objects.get(user=user)
#                 if not profile_obj.is_verified:
#                     return render(request, 'accounts/login.html',
#                                   {'message': 'Your account is not verified. Check your email.'})
#                 else:
#                     auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                     return redirect('index')
#             except:
#                 auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 return redirect('index')
#         else:
#             return render(request, 'accounts/login.html', {'message': 'Invalid username/email or password!'})
#     else:
#         return render(request, 'accounts/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request, 'accounts/register.html', {'message':'Account already exists. Try login instead?'})
        except User.DoesNotExist:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/register.html', {'message':'Username is already taken!'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
                    auth_token = str(uuid.uuid4())
                    profile_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    profile_obj.save()
                    send_mail_after_registration(request.POST['email'], auth_token)
                    return render(request, 'accounts/token_send.html')
                    # auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    # return redirect('index')
            else:
                return render(request, 'accounts/register.html', {'message' : 'Passwords does not match!'})
    else:
        return render(request, 'accounts/register.html')

def token(request):
    return render(request, 'accounts/token_send.html')

def verify(request, auth_token):
    profile_obj = Profile.objects.get(auth_token=auth_token)
    if profile_obj:
        if profile_obj.is_verified:
            return render(request, 'accounts/login.html', {'message':'Your account is already verified.'})
        else:
            profile_obj.is_verified = True
            profile_obj.save()
            return render(request, 'accounts/login.html', {'message':'Your account has been verified.'})

def send_mail_after_registration(to_email, auth_token):
    subject = 'Spelling Bee: Email Verification'
    message = f'Your link for email verification is http://127.0.0.1:8000/accounts/verify/{auth_token}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [to_email])

def profile(request):
    scoreObj = Score.objects.filter(username = request.user).values('score')
    correctWordObj = CorrectWord.objects.filter(user = request.user)
    sendvals = {
        'scoreObj': scoreObj,
        'correctWordObj':correctWordObj
    }
    return render(request, 'accounts/profile.html', {'sendvals': sendvals})

def send_mail_for_reset_password(userEmail, auth_token):
    subject = 'Spelling Bee: Reset Password'
    message = f'Your link for resetting password is http://127.0.0.1:8000/accounts/reset/{auth_token}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [userEmail])

def reset(request, auth_token):
    try:
        ValidLink.objects.get(unique_code = auth_token)
    except:
        return render(request, "accounts/forgot_password.html", {'error':'The link is invalid. Please try again.'})
    valid_link_obj = ValidLink.objects.get(unique_code = auth_token)
    valid_link_obj.delete()
    return render(request, "accounts/password_reset_form.html")

def password_reset_done(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            userEmail = request.session['userEmail']
            user = User.objects.get(email=userEmail)
            user.set_password(password1)
            user.save()
            return render(request, "accounts/login.html", {'message':'Password has been reset.'})
        return render(request, "accounts/password_reset_form.html", {'message':'Password do not match!'})

def forgot_password(request):
    if request.method == 'POST':
      userEmail = request.POST['email']
      try:
        user = User.objects.get(email=userEmail)
        Profile.objects.get(user=user)
      except:
          return render(request, "accounts/forgot_password.html", {'message':'Your account has not been registered.'})
      auth_token = str(uuid.uuid4())
      valid_link_obj = ValidLink.objects.create(unique_code = auth_token)
      valid_link_obj.save()
      request.session['userEmail'] = userEmail
      send_mail_for_reset_password(userEmail, auth_token)
      return render(request, 'accounts/email_sent.html')
    else:
        return render(request, 'accounts/forgot_password.html')

def email_sent(request):
    return render(request, 'accounts/email_sent.html')
