from django.shortcuts import render, redirect
from authentication.models import CustomUser
from organisation.models import Organisation
from sector.models import Sector
# Email Send and Token Genarator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def organisation(request):
    org = Organisation.object.all()
    data = {
        'org': org,
    }
    return render(request, 'organisation/organisation.html', data)


# @transaction.atomic
def addorg(request):
    sector1 = Sector.objects.all()
    data = {
        'sector1': sector1,
    }
    if request.method == "POST":
        organisation_name = request.POST['organisation_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        sector = request.POST['sector']
        user = CustomUser(username=username, email=email,
                          first_name=first_name, last_name=last_name, password="123456", user_type=2)
        user.save()
        # user.organisation.organisation_name = organisation_name
        # sector_obj = Sector.objects.get(id=sector)
        # user.organisation.sector = sector_obj
        organisation = Organisation(user=user)
        organisation.organisation_name = organisation_name
        organisation.sector_id = sector
        organisation.save()
        return redirect('organisation')

        # Email Verications
        # current_site = get_current_site(request)
        # mail_subject = 'Please Activate Your Account'
        # message = render_to_string(
        #     'authentication/activate.html', {
        #         'user': user,
        #         'domain': current_site,
        #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #         'token': default_token_generator.make_token(user),
        #     })
        # to_email = email
        # send_email = EmailMessage(
        #     mail_subject, message, 'mksifat101@gmail.com', to=[to_email])
        # send_email.send()
        # messages.success(request, 'Registration Successfull.')
        # return redirect('/accounts/login/?command=verifaction&email='+email)
    return render(request, 'organisation/addorg.html', data)


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = Organisation._default_manager(pk=uid)
#     except(TypeError, ValueError, OverflowError, Organisation.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_activate = True
#         user.save()
#         # messages.success(request, 'Congratulations! Your Account Activated.')
#         return redirect('activated')
#     else:
#         # messages.error(request, 'Invalid activate link.')
#         return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = CustomUser._default_manager(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        # messages.success(request, 'Please Reset Your Password')
        return redirect('activated')
    else:
        # messages.error(request, 'This link is expired')
        return redirect('login')


def activated(request):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = CustomUser.objects.get(pk=uid)
            user.set_password()
            user.save()
            # messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            # messages.error(request, 'Password not match')
            return redirect('resetPassword')
    else:
        return render(request, 'authentication/activated.html')
