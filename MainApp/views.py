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
    text = f"""
    <h1>\"Изучаем django\"</h1>
    <strong>Автор</strong>: <i>{author['surname']} {author['name'][0]}.{author['middle_name'][0]}. </i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Отчество <b>{author['middle_name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    телефон: <b>{author['phone']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)


def items_view(request):
    answer = "<ol>"
    for item in items:
        answer += f"<li><a href=/item/{item['id']}>id: {item['id']}, название: {item['name']} кол-во: {item['quantity']}</a></li>"
    answer += "</ol>"
    return HttpResponse(answer)


def item_view(request, id):
    for item in items:
        if item['id'] == id:
            answer = f"<b>название:</b> {item['name']} <b>кол-во:</b> {item['quantity']}"
            return HttpResponse(answer)
    raise Http404(f'Товар с id {id} не найден')
