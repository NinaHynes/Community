from django.urls import path, include
from . import views

app_name = 'CommunityUpcycle'  

urlpatterns = [
  path('', views.communityupcycle_list, name='communityupcycle_list'),
  path('<int:pk>/', views.communityupcycle_detail, name='communityupcycle_detail'),
  path('create/', views.communityupcycle_create, name='communityupcycle_create'),
  
]
