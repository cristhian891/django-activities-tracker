from django.urls import path
from . import views

app_name = 'activity'

urlpatterns = [
    path('', views.ActivityList.as_view(), name="list"),
    path('create/', views.CreateActivityView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ActivityDetails.as_view(), name='detail'),
    path('update/<int:pk>/', views.ActivityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ActivityDeleteView.as_view(), name='delete'),
    path('calories/', views.MetricsView.as_view(), name='calories'),
]