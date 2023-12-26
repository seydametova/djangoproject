from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-date')   # Получение всех объектов, отсортированных по дате публикации в порядке убывания(-date)
    return render(request, 'news/news_home.html', {"news": news})   # Передача всех объектов внутрь шаблона, как третий параметр

"""Создаю класс, наследующий все от класса DetailView(страница будет постоянно меняться в зависимости от параметра)"""
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'    # Шаблон, будет обрабатывать страницу
    context_object_name = 'article'    # По ключу будет передаваться запись в шаблон

"""Создаю класс для редактирования записей"""
class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    
    form_class = ArticlesForm   # Класс для отображения формы

"""Создаю класс для удаления записей"""
class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'    # Адрес для переадресации после удаления записи
    template_name = 'news/news_delete.html'

"""Метод create() осуществляет проверку введенных данных, и добавляет новые записи"""
def create(request):
    error = ''
    if request.method == 'POST':    # Если сейчас идет метод передачи данных POST, то данные отправляются из формы
        form = ArticlesForm(request.POST)   # В объекте будут находиться данные, полученные от пользователя
        if form.is_valid():    # Если форма заполнена корректно, то сохранит новую запись и переадресует на страницу сайта с новостями
            form.save()
            return redirect('news')
        else:   # Иначе - выведет текст об ошибке
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,   # Ключ:объект
        'error': error  # Передаю текст ошибки по ключу
    }
    return render(request, 'news/create.html', data)