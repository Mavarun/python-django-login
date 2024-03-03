from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from django.contrib import messages
User = get_user_model() 
# Create your views here.
@login_required(login_url='login')
# def HomePage(request):
#     return render (request,'home.html')
def HomePage(request):
    user = request.user  # Retrieve the logged-in user
    context = {
        'user': user  # Pass the user object to the template
    }
    return render(request, 'home.html', context)



# def SignupPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         profile_picture = request.FILES.get('profile_picture')

#         if password1 != password2:
#             return HttpResponse("Your password and confirm password are not the same!!")
#         else:
#             my_user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password1,
#                 first_name=first_name,
#                 last_name=last_name,
#                 address = address,
#                 city = city,
#                 state = state,
#                 pincode = pincode,
#                 profile_picture = profile_picture
#             )

            

#             my_user.save()
#             return redirect('login')

#     return render(request, 'signup.html')
# def SignupPage(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         profile_picture = request.FILES.get('profile_picture')

#         if password1 != password2:
#             return HttpResponse("Your password and confirm password are not the same!!")
#         else:
#             # Create a user object without saving it yet
#             my_user = User(
#                 username=username,
#                 email=email,
#                 first_name=first_name,
#                 last_name=last_name,
#                 address=address,  # Assign address
#                 city=city,  # Assign city
#                 state=state,  # Assign state
#                 pincode=pincode,  # Assign pincode
#                 profile_picture=profile_picture  # Assign profile_picture
#             )
#             # Assign user to the selected group (patient or doctor)
#             user_type = request.POST.get('userType')
#             group = Group.objects.get(name=user_type)
#             group.user_set.add(my_user)

#             my_user.set_password(password1)  # Set password
#             my_user.save()  # Save the user with all details

#             return redirect('login')

#     return render(request, 'signup.html')

# def SignupPage(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         profile_picture = request.FILES.get('profile_picture')
#         user_type = request.POST.get('userType')  # Retrieve user type

#         if password1 != password2:
#             return HttpResponse("Your password and confirm password are not the same!!")
#         else:
#             # Create a user object
#             my_user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 first_name=first_name,
#                 last_name=last_name,
#                 address=address,
#                 city=city,
#                 state=state,
#                 pincode=pincode,
#                 profile_picture=profile_picture
#             )
            
#             # Set user password
#             my_user.set_password(password1)
#             my_user.save()  # Save the user

#             # Assign user to the selected group (patient or doctor)
#             group = Group.objects.get(name=user_type)
#             group.user_set.add(my_user)

#             return redirect('login')

#     return render(request, 'signup.html')


def SignupPage(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_picture = request.FILES.get('profile_picture')
        user_type = request.POST.get('userType')  # Retrieve user type

        if password1 != password2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                # Create a user object
                my_user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    city=city,
                    state=state,
                    pincode=pincode,
                    profile_picture=profile_picture
                )

                # Set user password
                my_user.set_password(password1)
                my_user.save()  # Save the user

                # Assign user to the selected group (patient or doctor)
                group = Group.objects.get(name=user_type)
                group.user_set.add(my_user)

                return redirect('login')

            except Group.DoesNotExist:
                messages.error(request, 'Group does not exist. Please select a valid group.')
                # Redirect back to signup page or handle the error appropriately
                return redirect('signup')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                # Redirect back to signup page or handle the error appropriately
                return redirect('signup')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = "HELLO DR.VARUN"  # Combine the original lines into one
            return HttpResponse(message)
            

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')