from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request, user)
    return HttpResponse('OK')


# def persona_login(request):
#     print('login view', file=sys.stderr)
#     # user = PersonaAuthenticationBackend().authenticate(request.POST['assertion'])
#     user = authenticate(assertion=request.POST['assertion'])
#     if user is not None:
#         login(request, user)
#     return redirect('/')