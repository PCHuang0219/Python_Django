"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from . import views as atnurllibviews
#from jsonform import views as jsonformview
#from djangoform import views as djangoformview
from django.urls import include, path

#added by JL

urlpatterns = [

    #path('djangoform', djangoformview.hijk),
    #path('jsonform', jsonformview.index),

    path('', atnurllibviews.redfishv1),
    path('view?p=json', atnurllibviews.redfishv1),
    path('redfish/v1/',atnurllibviews.redfishv1),

    path('redfish/v1/Managers', atnurllibviews.redfishv1Managers),
    path('redfish/v1/Managers/RMC', atnurllibviews.redfishv1ManagersRMC),
    path('redfish/v1/Managers/RMC/NetworkProtocol', atnurllibviews.redfishv1ManagersRMCNetworkProtocol),

    path('redfish/v1/EventService', atnurllibviews.redfishv1EventService),
    path('redfish/v1/EventService/Subscriptions', atnurllibviews.redfishv1EventServiceSubscriptions),

    path('redfish/v1/MessageRegistry',atnurllibviews.redfishv1MessageRegistry),

    path('redfish/v1/Chassis',atnurllibviews.redfishv1Chassis),
    path('redfish/v1/Chassis/Rack', atnurllibviews.redfishv1ChassisRack),
    path('redfish/v1/Chassis/Rack/PowerZones', atnurllibviews.redfishv1ChassisRackPowerZones),
    path('redfish/v1/Chassis/Rack/PowerZones/1', atnurllibviews.redfishv1ChassisRackPowerZones1),
    path('redfish/v1/Chassis/Rack/PowerZones/1/Actions', atnurllibviews.redfishv1ChassisRackPowerZones1Actions),
    path('redfish/v1/Chassis/Rack/PowerZones/1/Actions/PowerZoneRequestStateChange', atnurllibviews.redfishv1ChassisRackPowerZones1ActionsPowerZoneRequestStateChange),

    #below no data from AS4610, but need to implement
    path('redfish/v1/Chassis/Rack/ThermalZones', atnurllibviews.redfishv1ChassisRackThermalZones),
    path('redfish/v1/Chassis/Rack/ThermalZones/1', atnurllibviews.redfishv1ChassisRackThermalZones1),

    path('redfish/v1/Chassis/Rack/MBPs', atnurllibviews.redfishv1ChassisRackMBPs),
    path('redfish/v1/Chassis/Rack/MBPs/1', atnurllibviews.redfishv1ChassisRackMBPs1),

    path('redfish/v1/Chassis/Drawer1', atnurllibviews.redfishv1ChassisDrawer1),

]
