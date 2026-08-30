from . import views
from django.urls import path
urlpatterns = [
    path("",views.home, name = 'home'),
    path("about/",views.about, name = 'about'),
    path("contact/",views.contact, name = 'contact'),
    path("preview/",views.preview_404, name = 'preview_404'),
    path("products/",views.product_list,name='product_list'),
    path('product<int:pk>/',views.product_details, name="product_details"),
]
