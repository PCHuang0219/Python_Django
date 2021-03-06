from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='test_index'),
    path('topologyConfig', views.topology_configuration, name='test_index'),
    path('status',views.status, name="test_status"),
    path('jobManagement/jobDetail/',views.detail, name="test_detail"),
    path('jobManagement',views.management, name="job_management"),
    path('jobManagement/jobDetail/jobLog/',views.log, name="job_log"),
    path('jobImage',views.image, name="job_image"),
    path('jenkinsViews',views.jenkins_views, name="Show Jenkins Information"),
    path('labInformation',views.lab_status_views, name="Show Lab Information"),
    path('deviceManagement',views.device_management_views, name="Show Device Status"),
    path('testPlanManagement',views.testPlanManagement, name="Test Plan Management Page"),
    path('createTestPlan',views.createTestPlan, name="Create Test Plan Page"),
    path('modifyTestPlan',views.modifyTestPlan, name="Modify Test Plan Page"),
    path('testPlanManagement/testPlanDetail',views.testPlanDetail, name="Test Plab Detail Page"),
    
    path('get/topoConfig/', views.get_topo_config),
    path('get/topoModel/', views.get_topo_model),
    path('get/modelConfig/', views.get_model_config),

    path('createTestPlan/',views.createTestPlanFunction),
    path('modifyTestPlan/',views.createTestPlanFunction),
    path('testPlanManagement/testPlanTable/', views.getTestPlanTable),
    path('testPlanManagement/detail/',views.getTestPlanDetail),



################################################################
    path('testCaseManagement',views.testCaseManagement, name="Test Case Management"),
    path('testCaseManagement/testPlanTable/', views.getTestPlanTable),
#################################################################


    path('save/finishedTestLog/',views.receive_finished_log_from_server),
    path('save/finishedTestReport/',views.receive_finished_report_from_server),
    path('save/getDUTList/',views.get_DUT_list),
    path('save/getTestcasesList/',views.get_testcases_list),

    path('save/IXIAInformation/',views.save_IXIA_Information),
    path('save/getIXIAInformation/',views.get_IXIA_Information),
    path('save/updateIXIAInformation/',views.update_IXIA_Information),
    path('save/updateIXIAChangeView/',views.update_IXIA_Change_View),
    path('save/ixiaSchedule/',views.create_ixia_schedule),

    path('save/deviceList/',views.create_deivce_list),
    
    path('get/ixiaSchedule/',views.get_ixia_schedule),
    path('get/weekDate/',views.get_week_date),
    path('get/updateIXIAConfig/',views.update_ixia_config),

    path('get/deviceList/',views.get_device_list),
    path('change/deviceList/',views.change_device_list),

    path('get/deviceListByRack/',views.get_device_list_by_rack),

    path('get/selectionByCondition/',views.get_selection_by_condition),

    path('status/currentRunningName/',views.get_current_test_name),
    path('submitTestcase/',views.submit_testcase),
    path('status/testConfigure/',views.get_job_configuration),
    path('status/jobStatus/',views.get_job_status),
    path('status/jobProgress/',views.get_job_progress),
    path('status/jobExecuteTime/',views.get_job_execute_time),
    path('status/jobRunningList/',views.get_running_job_list),
    path('status/nowTestLog/',views.get_now_test_log_from_server),
    path('status/getPlatformByJobID/',views.get_platform_by_job_id),

    path('image/imageTable/',views.get_image_table),
    path('detail/testTableInJob/',views.get_test_table_in_job),
    path('testCaseList/',views.get_test_case),
    path('management/jobTable/',views.get_job_table),
    path('jobDetail/testLog/',views.get_test_log),

    path('jenkins/getJobs/',views.get_jenkins_jobs),
    path('jenkins/getBuilds/',views.get_jenkins_builds),
    path('jenkins/buildjob/',views.build_jenkins_job),
    path('jenkins/getBuildresult/',views.get_build_result),
]

