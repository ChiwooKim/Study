from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    # 게시판 메인페이지
    path('', views.index, name='index'),
    # 게시판 글쓰기
    path('create/', views.create, name='create'),
    # 게시판 글
    path('<int:review_pk>/', views.detail, name='detail'),
    # 게시판 글 수정
    path('<int:review_pk>/update/', views.update, name='update'),
    # 게시판 글 삭제
    path('<int:review>/delete/', views.delete, name='delete'),
]