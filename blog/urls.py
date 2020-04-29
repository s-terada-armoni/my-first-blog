from django.urls import path
from . import views

urlpatterns = [
    # デフォルトサイトにアクセスしてきたらviews.post_listが行き先
    path('', views.post_list, name='post_list'),

    # http://127.0.0.1:8000/post/5/ などのURLが要求されたら、post_detailが行き先
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]
