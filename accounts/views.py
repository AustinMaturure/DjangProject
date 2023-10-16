# Import necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages  # Import the messages module


def signup_view(request):
    """
    View for user registration.

    This view handles user registration using the UserCreationForm.
    It allows users to sign up for an account and log in upon successful registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page with the registration form.

    """
    # Clear any existing messages from previous requests
    messages.clear(request)
    if request.method == 'POST':
        # Create a UserCreationForm instance with POST data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user and log them in
            user = form.save()
            login(request, user)
            # Add a success message and redirect to a page
            messages.success(
                request, 'Registration successful. You are now logged in.')
            if 'next' in request.POST:
                return redirect("practice:detail")
            else:
                return redirect("practice:list")
        else:
            # If the form is invalid, add error messages for each field
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        # Create a blank UserCreationForm instance for GET requests
        form = UserCreationForm()

    # Render the signup.html template with the form data
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """
    View for user login.

    This view handles user login using the AuthenticationForm.
    It allows users to log in to their accounts and provides a redirect mechanism.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page with the login form.

    """
    # Clear any existing messages from previous requests
    messages.clear(request)
    if request.method == 'POST':
        # Create an AuthenticationForm instance with POST data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # If the form is valid, log in the user
            user = form.get_user()
            login(request, user)
            # Add a success message
            messages.success(request, 'Login successful.')

            # Check if 'next' is present in both GET and POST requests
            next_url = request.POST.get('next') or request.GET.get('next')

            if next_url:
                # Redirect to the URL specified in 'next'
                return redirect(next_url)
            else:
                # Redirect to a default URL if 'next' is not provided
                return redirect("practice:list")
        else:
            # If the form is invalid, add a generic error message
            messages.error(
                request, 'Login failed. Please check your username or password.')

    # Create an AuthenticationForm instance for GET requests
    form = AuthenticationForm()

    # Render the login.html template with the form data
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    View for user logout.

    This view handles user logout. It logs the user out and redirects them to a default page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the default page.

    """
    if request.method == 'POST':
        logout(request)
        return redirect("practice:list")
