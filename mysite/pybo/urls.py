from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    #http://localhost:8000/pybo/ URL은 index, http://localhost:8000/pybo/2와 같은 URL에는 detail 이라는 이름을 부여했다.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create')
]
