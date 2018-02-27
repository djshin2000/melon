from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect


User = get_user_model()

__all__ = (
    'login_view',
)


def login_view(request):
    # post 요청일때는
    # authenticate -> login후 'index'로 redirect

    # get 요청일 때는
    # members/login.html파일을 보여줌
    #   해당 파일의 form에는 username, password input과 'login'버튼이 있음
    #   form은 method POST 로 다시 이 view로의 action(빈값)을 가짐
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {
                'error_message': '인증실패 - 다시 로그인해주세요.'
            }
            return render(request, 'members/login.html', context)
    return render(request, 'members/login.html')
