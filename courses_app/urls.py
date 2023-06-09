from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('create', views.create),
    path('destroy/<int:id>', views.destroy_page),
    path('destroy/<int:id>/done', views.destroy),
]