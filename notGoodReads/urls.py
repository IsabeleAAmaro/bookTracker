from django.urls import path
from . import views

urlpatterns = [
    # Livro URLs
    path('livro/', views.livro_list, name='livro_list'),
    path('livro/form/', views.livro_form, name='livro_form'),
    path('livro/form/<int:id>/', views.livro_form, name='livro_update'),
    path('livro/delete/<int:id>/', views.livro_delete, name='livro_delete'),

    # Usuario URLs
    path('usuario/', views.usuario_list, name='usuario_list'),
    path('usuario/form/', views.usuario_form, name='usuario_form'),
    path('usuario/form/<int:id>/', views.usuario_form, name='usuario_update'),
    path('usuario/delete/<int:id>/', views.usuario_delete, name='usuario_delete'),
]
