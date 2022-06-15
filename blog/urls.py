from django.urls import path
from.views import BlogListView, BlogdatailView,Blogcreateview, BlogupdateViev, blogDeletView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/new/', Blogcreateview.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogdatailView.as_view(), name='post_datail'),
    path('post/<int:pk>/delete', blogDeletView.as_view(), name= 'post_delete'),
    path('post/<int:pk>/edit', BlogupdateViev.as_view(), name='post_edit'),
]