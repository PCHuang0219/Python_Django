from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='tmssetup_index'),
    path('usermgmt',views.usermgmt),
    path('ixiaSchedule',views.ixia_schedule),


    path('getEveryTableDataCount/',views.get_every_table_data_count),
    path('updateUserPriority/',views.update_user_priority),
    path('getUserTypeTable/',views.get_user_type_table),
    path('AccountList/',views.get_account_list),
    path('deleteAccount/',views.delete_user),

    path('get/usernamebyid/',views.get_username_by_id),
]

