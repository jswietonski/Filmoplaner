from django.shortcuts import render

# Create your views here.


def render_homepage(request):
    '''Zaleznie od zalogowania uzytkownika pokazuje stronę główną bądź przekirowuje na strone logowania po odpowiednim komunikacie'''
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    return render(request, "user_not_logged/auth_fail.html")

