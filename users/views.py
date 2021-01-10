from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import userRegisterForm, UserUpdateForm, ProfileUpdateForm
from cards.models import Card, Set


def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')            
            return redirect('login')
    else:
        form = userRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')            
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    sets = Set.objects.all().order_by('release_date')
    cards = Card.objects.all().order_by('slug')

    context = {'u_form': u_form,'p_form': p_form,
    'sets':sets, 'cards':cards
    }
    
    return render(request, 'users/profile.html', context)