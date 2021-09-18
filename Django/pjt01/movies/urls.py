from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # /movies/ : 메인페이지 (영화 목록)
    path('', views.index, name='index'),
    
    # /movies/create/ : 영화 목록 생성
    path('create/', views.create, name='create'),
    
    # /movies/<movie_pk> : 영화 상세 내용 조회
    path('<int:movie_pk>/', views.detail, name='detail'),
    
    # /movies/<movie_pk>/update/ : 데이터 수정
    path('<int:movie_pk>/update/', views.update, name='update'),
    
    # /movies/<movie_pk>/delete/ : 데이터 삭제
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]
