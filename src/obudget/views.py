from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def main(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin/budget_lines/budgetline/my/')
    else:
        user = authenticate(username='budget', password='supersecretbudgetpassword')
        login(request, user)
        return HttpResponseRedirect('/admin/budget_lines/budgetline/my/')

