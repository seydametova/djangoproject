from django.shortcuts import render

"""Создаю метод get_index()

get_index() будет показывать пользователю то, что указано внутри,
при переходе по ссылке. В данном случае - главную страницу

"""
def get_index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')