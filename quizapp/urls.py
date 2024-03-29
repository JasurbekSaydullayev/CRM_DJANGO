from django.urls import path, include

from .views import question, qiuz, result_list

urlpatterns = [
    path('', qiuz, name='quiz'),
    path('quiz/<int:pk>/', question, name='questions'),
    path('results/', result_list, name='results'),
]
