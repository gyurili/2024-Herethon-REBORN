from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from accountApp.models import *
# Create your views here.

# 메인 홈
def main(request):
    users = User.objects.all()
    return render(request, "mainApp/main.html", {'object_list': users})

# 챌린지 게시판 리스트
def challengeList(request):
    # 존재하는 모든 카테고리 확인
    categories = Category.objects.all()

    # 카테고리 ID가 1인 글만 필터링
    category = get_object_or_404(Category, id=1)
    
    # 정렬 기준을 GET 파라미터로 받음, 기본값은 'latest'
    sort = request.GET.get('sort', 'latest')
    
    if sort == 'likes':
        posts = category.posts.all().annotate(like_count=models.Count('like')).order_by('-like_count', '-id')
    else:
        posts = category.posts.all().order_by('-id')

    return render(request, 'mainApp/challengeList.html', {'posts': posts, 'categories': categories, 'sort': sort})



#팁 게시판 리스트
def tipList(request):
    # 존재하는 모든 카테고리 확인
    categories = Category.objects.all()

    # 카테고리 ID가 1인 글만 필터링
    category = get_object_or_404(Category, id=2)
    
    # 정렬 기준을 GET 파라미터로 받음, 기본값은 'latest'
    sort = request.GET.get('sort', 'latest')
    
    if sort == 'likes':
        posts = category.posts.all().annotate(like_count=models.Count('like')).order_by('-like_count', '-id')
    else:
        posts = category.posts.all().order_by('-id')
    
    return render(request, 'mainApp/tipList.html', {'posts': posts, 'categories': categories, 'sort': sort})

# CRUD
@login_required
def create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            image = image,
        )

        # 다대다 카테고리 연결
        for category in category_list:
            post.category.add(category)

        post.save()    

        # 선택된 카테고리에 따라 리다이렉트 경로 설정
        if any(category.id == 1 for category in category_list):
            return redirect('mainApp:challengeList')
        else:
            return redirect('mainApp:tipList')

    return render(request, 'mainApp/create.html', {'categories': categories})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    categories = post.category.all()
    category_ids = [category.id for category in categories]
    return render(request, 'mainApp/detail.html', {'post': post, 'category_ids': category_ids })

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        image = request.FILES.get('image')

        if image:
            post.image.delete()
            post.image = image
            
        post.save()
        return redirect('mainApp:detail', id)
    return render(request, 'mainApp/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    categories = post.category.all()
    post.delete()

    if any(category.id == 1 for category in categories):
        return redirect('mainApp:challengeList')
    else:
        return redirect('mainApp:tipList')

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post
        )
        return redirect('mainApp:detail', post_id)
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('mainApp:detail', id=comment.post.id)
    else:
        return redirect('mainApp:detail', id=comment.post.id)
    
def add_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.add(request.user)
    return redirect('mainApp:detail', post_id)

def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.remove(request.user)
    return redirect('mainApp:detail', post_id)