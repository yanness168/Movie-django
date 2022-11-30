from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    path('', views.hello, name='home'),
    path('add_movie/', views.addMovie, name='add'),
    path('edit_movie/<str:id>', views.editMovie, name='edit'),
    path('delete_movie/<str:id>', views.deleteMovie, name='delete'),
    path('add_review/', views.addReview, name='addR'),
    path('edit_review/<str:id>', views.editReview, name='editR'),
    path('delete_review/<str:id>', views.deleteReview, name='deleteR'),
    path('<str:id>/', views.displayById, name="identifier"),
]