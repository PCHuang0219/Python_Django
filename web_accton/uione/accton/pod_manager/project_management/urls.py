from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='PM'),
    path('att',views.att, name="AT&T"),
    path('fb',views.fb, name="FaceBook"),
    path('amozon',views.amozon, name="Amozon"),
    path('sonic',views.sonic, name="SONiC"),
    path('TR_Detail',views.TR_detail),
    path('NTC_tasks',views.NTC_tasks),
    path('NTC_tasks/task_detail',views.NTC_task_detail),
    path('submit_EPR',views.submit_EPR),
    path('EPRList',views.EPR_page),
    path('EPRList/EPR_detail',views.EPR_detail),

    path('save/TRR/',views.create_TRR_data),
    path('save/mainProjectData/',views.create_main_project_data),
    path('save/TRRDescription/',views.create_TRR_description),
    path('save/TRRDiscussion/',views.create_TRR_discussion),
    path('save/changeTRRStatus/',views.change_TRR_status),
    path('save/updateTRRContent/',views.update_TRR_content),

    path('save/EPRContent/',views.save_EPR_content),
    path('save/EPRAttachment/',views.save_EPR_attachment),
    
    path('get/TRRContent/',views.get_TRR_detail),
    path('get/mainProjectData/',views.get_main_project_data),
    path('get/TRRDescription/',views.get_TRR_description),
    path('get/TRRDiscussion/',views.get_TRR_discussion),
    path('get/projectList/',views.get_project_list),

    path('get/EPRList/',views.get_EPR_list),

    path('get/tasksList/',views.get_tasks_list),
    path('get/tasksDtail/',views.get_task_detail_by_task_ID),

    path('get/TDList/',views.get_TD_list),
    path('get/TCList/',views.get_TC_list),
    path('get/TRRViewsByCondition/',views.get_views_by_condition),
    path('get/selectionByCondition/',views.get_selection_by_condition),

    path('test/',views.test)
]

