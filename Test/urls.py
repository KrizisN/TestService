from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('topic/<int:pk>', views.topic, name='topic'),
    path('test/<int:pk>', views.test_ready, name='test_answer'),
    path('testing/<int:pk>', views.test_answer, name='testing'),
    path('test_now/<int:pk>', views.testing, name='test_now'),
    path('result/<int:pk>/<int:pk2>', views.result, name='result'),
    path('solved_tests/<int:pk>', views.solved_tests, name='solved_tests'),
    path('delete_solved_tests/<int:pk>/<int:pk2>', views.delete_test_of_student, name='delete_solved_tests'),
    path('all_result/', views.all_results, name='all_result')
]
