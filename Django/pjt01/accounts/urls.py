from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # 회원가입
    path('signup/', views.signup, name='signup'),
    # 로그인
    path('login/', views.login, name='login'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
    # 회원탈퇴
    path('delete/', views.delete, name='delete'),
    # 회원정보변경
    path('update/', views.update, name='update'),
    # 비밀번호 변경
    path('password/', views.change_password, name='change_password'),
]
