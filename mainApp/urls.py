from django.urls import path
from .views import *

app_name='mainApp'
urlpatterns = [
    path('', main, name = 'main'),
    
    path('challengeList/', challengeList, name = "challengeList"),
    path('tipList/', tipList, name = "tipList"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),
    
    # 댓글 
    path('create-comment/<int:post_id>/', create_comment, name = "create-comment"),
    path('delete-comment/<int:comment_id>/', delete_comment, name = "delete-comment"),

    #좋아요
    path('add-like/<int:post_id>/', add_like, name = "add-like"),
    path('remove-like/<int:post_id>/', remove_like, name = "remove-like"),
]