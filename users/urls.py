from django.urls import path
from users import views

urlpatterns = [
    path('user-list/', views.UserListView.as_view(), name='user-list'),
]
