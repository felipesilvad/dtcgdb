from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from .forms import userRegisterForm, UserUpdateForm, ProfileUpdateForm, Collection, Collection_Set
from cards.models import Card, Set
from .models import UserCard


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
    usercards = UserCard.objects.all().filter(profile=request.user.profile)
    if request.method == 'POST':
        form = Collection(
            request.POST,
        )
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.save()

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
        form = Collection()

    sets = Set.objects.all().order_by('release_date')
    cards = Card.objects.all().order_by('slug')

    context = {'form': form, 'usercards':usercards,
    # 'u_form': u_form,'p_form': p_form,
    'sets':sets, 'cards':cards
    }
    
    return render(request, 'users/profile.html', context)

@login_required
def collection(request):
    usercards = UserCard.objects.all().filter(profile=request.user.profile)
    usercards_c = usercards.filter(quantity__gt=0).count()
    usercards_q = usercards.aggregate(Sum('quantity'))
    sets = Set.objects.all().order_by('slug')
    cards = Card.objects.all().order_by('slug')

    usercards_set_c = usercards.filter(quantity__gt=0).values('card__set__slug').annotate(total=Count('id'))
    sets_total_cards = sets.values('card__set__slug').annotate(total=Count('id'))

    set_percentages = {}
    for setcards in sets_total_cards:
        for usercards in usercards_set_c:
            if usercards['card__set__slug'] == setcards['card__set__slug']:
                set_percentages[setcards['card__set__slug']] = round((usercards['total'] / setcards['total']) * 100, 2)
                
    context = {'usercards':usercards, 'usercards_c':usercards_c, 'usercards_q':usercards_q,
    'sets':sets, 'cards':cards, 'usercards_set_c':usercards_set_c, 'sets_total_cards':sets_total_cards,
    'set_percentages':set_percentages
    }
    
    return render(request, 'users/collection.html', context)

@login_required
def collection_set(request, slug_set):
    set = Set.objects.get(slug=slug_set)
    cards = set.card_set.all().order_by('slug')
    usercards = UserCard.objects.all().filter(profile=request.user.profile).filter(card__set=set)
    usercards_c = usercards.filter(quantity__gt=0).count()
    cards_c = cards.count()
    set_percent = round((usercards_c / cards_c)  * 100, 2)
    
    usercards_ids = []
    for usercard in usercards:
        usercards_ids.append(usercard.card.id)

    usercard = None
    if request.method == 'POST':
        usercard = UserCard.objects.all().filter(profile=request.user.profile).filter(card=request.POST.get('card')).first()
        form = Collection_Set(request.POST, instance=usercard)
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = Collection_Set(instance=usercard)

    context = {'usercards':usercards,'set':set, 'cards':cards, 'usercards_ids':usercards_ids,
    'usercards_c':usercards_c, 'cards_c':cards_c, 'set_percent':set_percent,
    'form':form, 'usercard':usercard
    }
    
    return render(request, 'users/collection_set.html', context)