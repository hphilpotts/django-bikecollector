from django.urls import path
from . import views

urlpatterns = [
    # Main Paths:
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Bike Paths:
    path('bikes/', views.bikes_index, name='index'),
    path('bikes/<int:bike_id>', views.bikes_detail, name='detail'),
    path('bikes/create', views.BikeCreate.as_view(), name='bikes_create'),
    path('bikes/<int:pk>/update', views.BikeUpdate.as_view(), name='bikes_update'),
    path('bikes/<int:pk>/delete', views.BikeDelete.as_view(), name='bikes_delete'),
    path('bikes/<int:bike_id>/add_component/', views.add_component, name='add_component'),
    # Accessory Paths:
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessories_delete'),
    # Associate/Unassociate Paths:
    path('bikes/<int:bike_id>/assoc_accessory/<int:accessory_id>', views.assoc_accessory, name='assoc_accessory'),
    path('bikes/<int:bike_id>/unassoc_accessory/<int:accessory_id>', views.unassoc_accessory, name='unassoc_accessory')
    
]
