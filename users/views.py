from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfileForm()
    return render(request, 'users/create_user.html', {'form': form})

def success(request):
    return render(request, 'users/success.html')
