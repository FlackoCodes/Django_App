from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Customer
# Create your views here.


def home(request):
    records = Customer.objects.all()
    # logging user in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the user
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Logs')
    context_dictionary = {'records':records}
    return render(request, 'home.html',context_dictionary )



def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        # send everything in the post request to the signup form
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login newly created user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Congrats you have signed up successfully')
            return redirect('home')
    form = SignUpForm()
    context_dictionary = {'form':form}
    return render(request, 'register.html', context_dictionary)


def customer_records(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        context_dictionary = {'customer_record': customer_record}
        return render(request, 'customer_records.html', context_dictionary)
    messages.error(request, 'please log in to view')
    return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        user_record = Customer.objects.get(id=pk)
        user_record.delete()
        messages.success(request, 'You have successfully deleted the record')
        return redirect('home')
    messages.error(request, 'please log in to view')
    return redirect('home')


def add_records(request):
    form  = AddRecordForm(request.POST)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'You have successfully added a new record')
                return redirect('home')
        context_dictionary = {'form':form}
        return render(request, 'add_record.html', context_dictionary)
    return redirect('home')



@login_required(login_url='home')
def update_records(request, pk):
    current_record = Customer.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully')
        return redirect('home')
    context_dictionary = {'form':form}
    return render(request, 'update.html', context_dictionary)
