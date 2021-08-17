from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='dashboard-staff-delete'),
    path('product/', views.product, name='dashboard-product'),
    path('product/detail/<int:pk>/', views.product_detail, name='dashboard-product-detail'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('supplier/', views.supplier, name='dashboard-supplier'),
    path('supplier/delete/<int:pk>/', views.supplier_delete, name='dashboard-supplier-delete'),
    path('order/', views.order, name='dashboard-order'),
    path('order/delete/<int:pk>/', views.order_delete, name='dashboard-order-delete'),

]
