from userauthentication.forms import UserForm, UserprofileForm
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.user.is_authenticated():
        print request.user
        
        return redirect('/')
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserprofileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']
            profile.mobileno = request.POST['mobileno']
            profile.address = request.POST['address']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserprofileForm()
        
    # Render the template depending on the context.
    return render_to_response(
            'userauthentication/registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def my_login(request):

    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.POST['next'])
            else:
                pass
        else:
            message = 'user is not Authenticated'
    if request.method == 'GET':
        if request.GET.has_key('next'):
            next = request.GET['next']
        else:
            next = '/'
        return render(request, 'userauthentication/login.html', {'next': next})

    return render(request, 'userauthentication/login.html')

def my_logout(request):
    logout(request)
    return redirect('/')