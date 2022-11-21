from django.shortcuts import render, HttpResponse
from django.http import Http404


author = {
    "name": "Сергей",
    "surname": "Ботвинко",
    "middle_name": "В",
    "email": "sergey.botvinko@megafon.ru",
    "phone": "+7-999-999-9999"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    return render(request, 'index.html')


def about(request):
    context = {
        "author": author
    }
    return render(request, 'about.html', context)


def items_view(request):
    context = {
        "items": items
    }
    # answer = "<ol>"
    # for item in items:
    #     answer += f"<li><a href=/item/{item['id']}>id: {item['id']}, название: {item['name']} кол-во: {item['quantity']}</a></li>"
    # answer += "</ol>"
    # return HttpResponse(answer)
    return render(request, 'items_list.html', context)


def item_view(request, id):
    for item in items:
        if item['id'] == id:
            answer = f"<b>название:</b> {item['name']} <b>кол-во:</b> {item['quantity']}"
            return HttpResponse(answer)
    raise Http404(f'Товар с id {id} не найден')
