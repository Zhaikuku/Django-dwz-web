from django.urls import path

from . import views




urlpatterns = [
    path('', views._login_page, name='_login_page'),
    path('home/', views._home_page, name='_home'),
    path('sale/', views._sale_page, name='_sale'),
    path('position/', views._position_page, name='_position'),
    path('purchase/', views._purchase_page, name='_purchase'),
    path('saleCsv/', views._sale_Csv, name='_sale_csv'),
    path('positionCsv', views._position_Csv, name='_position_Csv'),
    path('purchaseCsv', views._purchase_Csv, name='_purchase_Csv'),

]