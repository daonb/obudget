from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def main(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin')
    else:
        user = authenticate(username='budget', password='budget')
        login(request, user)
        return HttpResponseRedirect('/admin')

