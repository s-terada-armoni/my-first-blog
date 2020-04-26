from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    # Postからデータ抽出
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts = Post.objects.all().order_by('created_date')

    # {'posts': posts} テンプレートファイルにpostsを渡す
    return render(request, 'blog/post_list.html', {'posts': posts})
