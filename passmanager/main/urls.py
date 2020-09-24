from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('edits', views.edits, name='edits'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete, name='delete')

]
