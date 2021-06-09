from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('memories/', views.memories),
    path('memoryForm/', views.memoryForm),
    path('createMemories/', views.createMemories),
    path('<int:memory_id>/commentForm/', views.commentForm),
    path('createComment/', views.createComment),
    path('logReg/', views.logReg),
    path('hiddenLog/', views.hiddenLog),
    path('hiddenReg/', views.hiddenReg),
]