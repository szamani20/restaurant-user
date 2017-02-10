from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import RegistrationForm


@csrf_exempt
def login(request):
    print('Cookie: ', request.COOKIES)
    if request.user.is_authenticated():
        return HttpResponse(content='User already logged in',
                            status=200,
                            content_type='text/plain')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponse(content=request.session.session_key,
                                status=202,
                                content_type='text/plain')

    return HttpResponse(content='Not an appropriate request',
                        status=400,
                        content_type='text/plain')


@csrf_exempt
def register(request):
    print(request.user)

    if request.user.is_authenticated():
        return HttpResponse(content='User already logged in',
                            status=200,
                            content_type='text/plain')

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse(content='User created',
                                status=201,
                                content_type='text/plain')

    return HttpResponse(content='Not an appropriate request',
                        status=400,
                        content_type='text/plain')


@csrf_exempt
def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponse(content='User logged out',
                            status=200,
                            content_type='text/plain')
