from django.shortcuts import render
from django.http import HttpResponse
from users.forms import UserRegistrationForm


def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

def register(request):
    context = {}
    # print(request.POST, request.GET)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            return HttpResponse(content='user successfully created!')
        else:
            print(form.errors)
            # return HttpResponse(content=form.errors)
    
    else:
        form = UserRegistrationForm()
        context.update({
            'form': form,
        })
    return render(request, 'user_registration.html', context)