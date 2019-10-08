from django.urls import path
from . import views

urlpatterns = [
                path('', views.index, name='index'),
                path('<int:client_id>/', views.clp_view, name='clp_view'),
                path('<int:client_id>/<int:equipamento_id>/equip_on/'
                     , views.EquipOn, name='equip_on'),
                path('<int:client_id>/<int:equipamento_id>/equip_off/'
                     , views.EquipOff, name='equip_off'),
                ]

