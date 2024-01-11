from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/',
         views.downvote_post, name='downvote_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
