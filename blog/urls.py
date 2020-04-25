from django.urls import path
from . import views

urlpatterns = [
    # デフォルトサイトにアクセスしてきたらviews.post_listが行き先
    path('', views.post_list, name='post_list'),
]
