from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list_create_view), 
    path("<int:pk>/update/", views.ProductUpdateApiView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteApiView.as_view()),
    path("<int:pk>/", views.ProductDetailApiView.as_view()),
]
