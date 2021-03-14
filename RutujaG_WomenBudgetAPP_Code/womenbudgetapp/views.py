from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import CreateProfileForm,CreateUserForm, LoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Wallet, GoalSet
import re


def IndexView(request):
    return render(request, 'index.html')

# Create your views here.

def RegisterPage(request):
    form = CreateUserForm()
    profile = CreateProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile = CreateProfileForm(request.POST)

        # error check for password
        password1s = profile.data['password1']
        password2s = profile.data['password2']

        sp = ['$', '#', '@', '!', '*']
        if password1s != password2s:
            messages.error(request, 'Two passwords must be same')
        elif len(password1s) < 6 or len(password1s) > 8:
            messages.error(request, 'Password must be at least 6 and maximum 8 character and should have special character')
        elif re.search('[0-9]', password1s) is None:
            messages.error(request,'password must have at least one number')
        elif re.search('[A-Z]', password1s) is None:
            messages.error(request, 'password must have at least one Uppercase character')
        elif not any(c in sp for c in password1s):
            messages.error(request, 'password must have at least on special charecter')
        else:
            if form.is_valid() and profile.is_valid():
                user = form.save()
                first_names = form.cleaned_data.get('first_name')
                last_names  = form.cleaned_data.get('last_name')
                messages.success(request, 'account is created for ' + first_names + " " + last_names)
                profile = profile.save(commit=False)
                profile.user = user
                profile.save()
                print("registerd")
                context = {'form': form, 'profile': profile}
                return render(request, 'registration.html', context)

    context = {'form': form, 'profile': profile}
    return render(request, 'registration.html', context)


# login page
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        # request.session['username'] = username
        if forms.is_valid():
            cd = forms.cleaned_data
            username = cd.get('username')
            request.session['username'] = username
            password = cd.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('update')
            else:
                return redirect('update')
    context = {'form': form}
    return render(request, 'login.html', context)


def UpdateView(request):
    username = request.session.get('username')
    perticular_user = User.objects.all().filter(username=request.session.get('username'))
    wallet_amounts = 0
    for value in perticular_user:
        wallet_user = Wallet.objects.all().filter(user=value)
        for values in wallet_user:
            wallet_amount = values.walletamount
            wallet_amounts = wallet_amount
    ctext = {'user': username, 'wallet_amount': wallet_amounts}
    return render(request, 'update.html', ctext)


def AddWalletAmount(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        perticular_user = User.objects.all().filter(username=request.session.get('username'))
        for value in perticular_user:
            wallet_user = Wallet.objects.all().filter(user=value)
            for values in wallet_user:
                values.walletamount = str(int(values.walletamount) + int(amount))
                values.save()

    Final_dict={'value':values.walletamount}
    return JsonResponse(Final_dict)


def CalculateSaving(request):
    if request.method == 'POST':
        Final_dict = {}


        goal = request.POST['goal']
        capitalA = request.POST['capitalA']
        targetA = request.POST['targetA']
        duration = request.POST['duration']
        ym = request.POST['ym']
        capitalA = int(capitalA)
        targetA = int(targetA)
        duration = int(duration)
        walletA = ""
        perticular_user = User.objects.all().filter(username=request.session.get('username'))
        for value in perticular_user:
            wallet_user = Wallet.objects.all().filter(user=value)
            for values in wallet_user:
                values.walletamount = str(int(values.walletamount) - capitalA)
                walletA = values.walletamount
                values.save()

        if capitalA<1000:
            r = 1.8
        elif capitalA>=1000 and capitalA<=10000:
            r = 2.5
        elif capitalA>10000 and capitalA<=30000:
            r = 3
        elif capitalA>30000 and capitalA<=50000:
            r = 3.5
        elif capitalA>50000 and capitalA<=80000:
            r = 4
        elif capitalA>80000 and capitalA<=100000:
            r = 4.5
        else:
            r = 5

        if ym == "Yearly":
            print(ym)
            base = 1 + (r/100)
            a1 = targetA/(base**duration)
            a = a1 - capitalA
            a = a/duration
            Final_dict['saving'] = a
        else:
            base = 1 + (r / 100)
            a1 = targetA / (base ** duration)
            a = a1 - capitalA
            a = a / duration
            Final_dict['saving'] = a

        GoalSet_O = GoalSet()
        perticular_user = User.objects.all().filter(username=request.session.get('username'))
        for value in perticular_user:
            GoalSet_O.users = value
        GoalSet_O.goaltitle = str(goal)
        GoalSet_O.targetamount = str(targetA)
        GoalSet_O.duration = str(duration)
        GoalSet_O.capitalamount = str(capitalA)
        GoalSet_O.ym = ym
        GoalSet_O.savings = Final_dict['saving']
        GoalSet_O.save()

        Final_dict['goal'] = str(goal)
        Final_dict['target'] = str(targetA)
        Final_dict['duration'] = str(duration)
        Final_dict['capital'] = str(capitalA)
        Final_dict['ym'] = ym
        Final_dict['wallet_amount'] = walletA
        return JsonResponse(Final_dict)


def FetchAllGoals(request):
    if request.method == 'POST':
        Final_dict = {}
        perticular_user = User.objects.all().filter(username=request.session.get('username'))
        for value in perticular_user:
            GoalSet_perticularuser = GoalSet.objects.all().filter(users=value)
            count = 1
            for values in GoalSet_perticularuser:
                goal_data = []
                goal_data.append(values.goaltitle)
                goal_data.append(values.duration)
                goal_data.append(values.capitalamount)
                goal_data.append(values.ym)
                goal_data.append(values.savings)
                goal_data.append(values.targetamount)
                Final_dict[count] = goal_data
                count = count + 1
        return JsonResponse(Final_dict)







