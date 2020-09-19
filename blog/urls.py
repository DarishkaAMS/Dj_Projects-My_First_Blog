from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), #Django uses angle brackets < > to capture the values from the URL and return the equivalent post detail page.
]