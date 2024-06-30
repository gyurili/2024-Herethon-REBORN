from datetime import date, timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from accountApp.models import *

# Create your views here.

# 메인 홈
def main(request):
    users = User.objects.all()
    # 오늘 날짜
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())

    # 이번주 상위 3개의 게시글
    weekly_posts = Post.objects.filter(created_at__date__gte=start_of_week) \
                .annotate(like_count=models.Count('like')) \
                .order_by('-like_count', '-id')[:3]

    today_posts = Post.objects.filter(created_at__date=today) \
                .annotate(like_count=models.Count('like')) \
                .order_by('-like_count', '-id')

    # 오늘 게시글 순위
    day_most_liked_post = today_posts.first()

    # 사용자 게시글 순위
    if  today_posts.filter(author=request.user.id):
        user_post = today_posts.filter(author=request.user.id).first()
    else :
        user_post = 0
    user_post_rank = list(today_posts).index(user_post) + 1 if user_post else 0
    
    # 검색
    query = request.GET.get('query', '')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))


    return render(request, "mainApp/main.html", {'object_list': users, 'day_most_liked_post':day_most_liked_post,
                                                'weekly_posts':weekly_posts, 'user_post_rank':user_post_rank, 'query': query})

# 챌린지 게시판 리스트
def challengeList(request):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=1)
    sort = request.GET.get('sort', 'latest')
    query = request.GET.get('query', '')

    posts = category.posts.all()

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    if sort == 'likes':
        posts = posts.annotate(like_count=models.Count('like')).order_by('-like_count', '-id')
    else:
        posts = posts.order_by('-id')

    return render(request, 'mainApp/challengeList.html', {'posts': posts, 'categories': categories, 'sort': sort, 'query': query})

#팁 게시판 리스트
def tipList(request):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=2)
    sort = request.GET.get('sort', 'latest')
    query = request.GET.get('query', '')
    
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
        
    if sort == 'likes':
        posts = category.posts.all().annotate(like_count=models.Count('like')).order_by('-like_count', '-id')
    else:
        posts = category.posts.all().order_by('-id')
    
    return render(request, 'mainApp/tipList.html', {'posts': posts, 'categories': categories, 'sort': sort})

# 글 작성
@login_required
def create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        file = request.FILES.get('file')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id=category_id) for category_id in category_ids]

        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            image=image,
            file=file,
        )

        for category in category_list:
            post.category.add(category)

        post.save()

        if any(category.id == 1 for category in category_list):
            return redirect('mainApp:challengeList')
        else:
            return redirect('mainApp:tipList')

    return render(request, 'mainApp/create.html', {'categories': categories})

# 글 조회 
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    categories = post.category.all()
    category_ids = [category.id for category in categories]
    return render(request, 'mainApp/detail.html', {'post': post, 'category_ids': category_ids})

# 글 수정
def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        image = request.FILES.get('image')
        file = request.FILES.get('file')

        if image:
            post.image.delete()
            post.image = image
        if file:
            post.file.delete()
            post.file = file

        post.save()
        return redirect('mainApp:detail', id)
    return render(request, 'mainApp/update.html', {'post': post})

# 글 삭제
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    categories = post.category.all()
    post.delete()

    if any(category.id == 1 for category in categories):
        return redirect('mainApp:challengeList')
    else:
        return redirect('mainApp:tipList')

# 댓글 작성
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        Comment.objects.create(
            content=request.POST.get('content'),
            author=request.user,
            post=post
        )
        return redirect('mainApp:detail', post_id)

# 댓글 삭제
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('mainApp:detail', id=comment.post.id)
    else:
        return redirect('mainApp:detail', id=comment.post.id)

# 하트 누르기
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('mainApp:detail', post_id)

# 하트 취소
def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.remove(request.user)
    return redirect('mainApp:detail', post_id)
