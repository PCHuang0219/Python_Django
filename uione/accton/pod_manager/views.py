# from django.contrib.auth.forms import UserCreationForm # 新增
# from django.shortcuts import render
# from django.shortcuts import redirect

# def register(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)
# 		print("Errors", form.errors)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('')
# 		else:
# 			return render(request, 'registration/register.html', {'form':form})
# 	else:
# 		form = UserCreationForm()
# 		context = {'form': form}
# 		return render(request, 'registration/register.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import UserRegistrationForm


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

def permissin_denied(request):
    return render(request, "account/permission_denied.html")

def page_not_found(request, exception, template_name='errors/page_not_found.html'):
    response = render(request,template_name)
    return response

def report_center(request):
    return render(request,'errors/report_center.html')