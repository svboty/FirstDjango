from django.urls import path

from MainApp import views


app_name = 'mainapp'
urlpatterns = [
    path('', views.home, name='index'),
    path('items', views.items_view, name='list-items'),
    path('item/<int:id>', views.item_view, name='item'),
]
