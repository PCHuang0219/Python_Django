let changeDropdownValue = function(){
    $(".dropdown-menu li a").click(function(){
        $(this).parents(".dropdown").find('.btn').html($(this).text() + '<span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
     });
}
let storeImageValue =function() {
    if(getUrlParameter("test_plan_id")) {
        let test_plan_id = getUrlParameter("test_plan_id")
        enterValueByTestPlan(test_plan_id)
    }
    if (getUrlParameter("image_path") || getUrlParameter("job_name")){
        document.getElementById('build_image_location').value = getUrlParameter("image_path")
        document.getElementById('job_name').value = getUrlParameter("job_name")
        document.getElementById('job_description').value = getUrlParameter("job_description")
    }
}
let isShow = false;
let testData = []

let enterValueByTestPlan = function(test_plan_id){
    $.ajax({
        type:'get',
        url:window.location.origin + '/test/testPlanManagement/detail/',
        data:{test_plan_id :test_plan_id},
        dataType:'json',
        success:function(data){
            data = data['detail']
            if (getUrlParameter("image_path") || getUrlParameter("job_name")){
                document.getElementById('build_image_location').value = getUrlParameter("image_path")
                document.getElementById('job_name').value = getUrlParameter("job_name")
                document.getElementById('job_description').value = getUrlParameter("job_description")
            }
            $('#project').val(data['project'])
            $('#platform_choose button').text(data['platform']);
            $('#model_choose button').text(data['model']);
            $('#topology_choose button').text(data['testcase_topology']);
            data['testcase_list'].forEach(function(element){
                category = element['test_name']
                testId = element['test_case']
                testData.push({'category':category,'testId':testId})
            })
            $("#selectTestCaseList").trigger('click');
        }

    })

}

let setTestChildClick = function(){
    $(".category").click(function(){
        if($(this).is(':checked')) {
            if ( $(this).next("label").text() == "Select All" ){
                $(this).parent().parent().parent().parent().children().children().children().children().children('input').prop("checked", true);
                $(this).parent().parent().parent().parent().children().children().children().children('input').prop("checked", true);
            }
            else{
                $(this).parent().parent().next().children().children().children("input").prop("checked",true);        
            }
        }
        else{
            if ( $(this).next("label").text() == "Select All" ){
                $(this).parent().parent().parent().parent().children().children().children().children().children('input').prop("checked", false)
                $(this).parent().parent().parent().parent().children().children().children().children('input').prop("checked", false);
            }
            else{
                $(this).parent().parent().next().children().children().children("input").prop("checked",false);
            }
        }
    });
}

let setParentClick = function(){
    $(".child-check").click(function(){
        parent_node = $(this).parent().parent().parent().prev().children().children("input")
        child_list = $(this).parent().parent().parent().children().children().children('input[type="checkbox"]')
        status = 'true'
        for (i=0 ; i<child_list.length ; i ++){
            element = child_list[i]
            if (!element['checked']){
                status = 'false'
            }
        }
        if (status == 'true'){
            parent_node.prop('checked',true)
        }
        else{
            parent_node.prop('checked',false)
        }
    })
}

let saveInformation = function(){
    let url = ""
    if (getUrlParameter("test_plan_id")){
        url+="?test_plan_id=" + getUrlParameter("test_plan_id") + "&"
    }
    else{
        url+="?"
    }
    project = document.getElementById('project').value
    job_name = document.getElementById('job_name').value
    job_description = document.getElementById('job_description').value
    url += "job_name=" + job_name + "&job_description=" + job_description + "&project=" + project
    location.href = window.location.origin + "/test/jenkinsViews" + url
}

let setTestChildDisplay = function(){
    $(".show_button").unbind('click');
    $(".show_button").bind('click',function(){
        if($(this).parent().parent().next().css("display") != 'none'){
            $(this).parent().parent().next().css("display","None");
            return;
        }    
        else{
            $(this).parent().parent().next().css("display","block");
            return;
        }
    });
}

let submitTestCase = function(){
    $('#submitTestCase').click(function(){
        if ($(this).attr('id') != 'disableButton'){
            break_val = 'False'
            let test_item_list =  []
            let value_list =  []
            let thread_num = 0
            $(".system_T1_Table").children().children("#testCase").each(function(){
                type =  $(this).children('#time_period').children('input[type="radio"]:checked').val();
                value = $(this).children('#time_period').children('input[type="radio"]:checked').next().val();
                time_period = String(value) + type
                stage_id = $(this).children('#stage_id').children('input').val()
                if($(this).find('textarea').length > 0){
                    test_item_list.push($(this).children("textarea").val())
                    thread_num += 1
                }
                else{
                    value_list = []
                    $(this).children().children().find('input[type="checkbox"]:checked').each(function(){
                        if (break_val == 'True'){
                            return;
                        }
                        let type = ($(this).parent().parent().parent().parent().first().children().children().children().next().text())
                        type = type.slice(0,-4);
                        if(type.toString().length < 50){
                            if(type.toString().length == 0){
                                value_list.push($(this).next().text());
                            }
                            else{
                                times = $(this).next().val()
                                times = 1
                                test_case = $(this).next().next().text()
                                if (times == ""){
                                    alert('Please enter number of executions of ' + test_case + '.');
                                    break_val = 'True';
                                }
                                else{
                                    if (type != "L3 Traffic Test(IXIA 100G, snake test)"){
                                        json_text = '{"TD":"' + type + '","TC":"' + test_case + '","time_period":"' + time_period + '","stage_id":"' + stage_id + '"}'
                                        value_list.push(json_text);
                                    }
                                }
                            }
                        }
                    });
                    test_item_list.push(value_list)
                    thread_num += 1
                }
            })
            project = document.getElementById("project").value;
            job_name = document.getElementById("job_name").value;
            job_description = document.getElementById("job_description").value;
            image_version = document.getElementById("build_image_location").value;
            var radios = document.getElementsByName('Schedule');
            for (var i = 0, length = radios.length; i < length; i++){
                if (radios[i].checked){
                    if (radios[i].value == '1'){   
                        execute_date = document.getElementById("execute_date").value;
                        execute_time = document.getElementById("execute_time").value;
                        if (execute_date != ''){
                            if (execute_time != ''){
                                execute_time = execute_date+"_"+execute_time ;                                        
                                alert(execute_time)
                            }
                            else{
                                execute_time = '' ;
                                break;}
                            }
                        }
                    else if (radios[i].value == '0'){ 
                        execute_time = 'now'
                    }
                }
            }
            if (project == ''){
                alert("Project cannot be empty");
            }
            else if(job_name == ''){
                alert("Name of job cannot be empty");
            }
            else if(execute_time == ''){
                alert("Execute Time cannot be empty")
            }
            else if(test_item_list[0].length == 0){
                alert("please select at least one testcase");
            }
            else{
                $.ajax({
                    type:'post',
                    url:window.location.origin +"/test/submitTestcase/",
                    data:{project: project,
                        job_name: job_name,
                        job_description: job_description,
                        testList: test_item_list,
                        platform: platform_name,
                        model: model_name,
                        topology: topology_name,
                        execute_time: execute_time,
                        image_version: image_version,
                        thread_num: thread_num},
                    dataType:'json',
                    // success:function(data){
                    //     localStorage.setItem("jobId",data["job_id"]);
                    //     localStorage.setItem("platform",platform_name);
                    //     if(execute_time == "now"){
                    //         location.href = window.location.origin +"/test/status";
                    //     }
                    //     else{
                    //         location.href = window.location.origin +"/test/jobManagement";
                    //     }
                    // }
                })
            }
        }
    })
}

let addButton = '<a class="btn btn-primary btn-lg addNextStage" id="addNextStage" role="button" style="float:right" type="button">Add Another Test</a> \
                <a class="btn btn-primary btn-lg addTestScript" id="addTestScript" role="button" style="float:right" type="button">Add Test Script</a>'

let selectTestCase = function(){
    platform_name = $('#platform_choose button').text();
    model_name = $('#model_choose button').text();
    topology_name = $('#topology_choose button').text();
    $(".stage_views").remove()
    $("#disableButton").removeAttr('disabled')
    $("#disableButton").attr('id', 'submitTestCase')
    if($("#submitTestCase").next(".addNextStage").length == "0"){
        addButton = '<a class="btn btn-primary btn-lg addNextStage" id="addNextStage" role="button" style="float:right" type="button">Add Another Test</a> \
                    <a class="btn btn-primary btn-lg addTestScript" id="addTestScript" role="button" style="float:right" type="button">Add Test Script</a>'
        $("#submitTestCase").after(addButton)
        showNextStageSelection()
    }   
    $.ajax({
        type:'post',
        url:window.location.origin +"/test/testCaseList/",
        data:{platform:platform_name,model: model_name,topology: topology_name},
        dataType:'json',
        success:function(data, status){
            platform = data["platform"]
            data = data["testData"]
            show_testcase_view(data,platform);
        }
    });
}

let html = ""
let index = 0

let clickLabelTriggerLastCheckbox = function(){
    $(".custom-control-label").click(function(){
        $(this).parent().children("input[type='checkbox']").trigger('click')
    })
}

let show_testcase_view = function(dataList,platform){
    let check_box_list = []
    $( "#testCase" ).empty();
    if (platform == "Facebook"){
        html_list = "<p id='stage_id' style='padding-left:40px;'><label class='custom-control-label'>Stage ID&emsp;:&emsp;</label>" + 
        '<input type="text" id="stage" onkeyup="ValidateNumber(this)" style="width: 30px" value="1"></p>' + 
        '<p id="time_period" style="padding-left:40px;"><label class="custom-control-label">Time Period&emsp;:&emsp;</label>' +
            '<input checked name="time_period0" style="margin-left: 10px" type="radio" value=" times">' +
            '<input type="text" id="run_times" onkeyup="ValidateNumber(this)" style="width: 50px" value="1"> times' +
            '<input name="time_period0" style="margin-left: 10px" type="radio" value=" hours">' +
            '<input type="text" id="time_period_time" onkeyup="ValidateNumber(this)" style="width: 50px"> Hours' +
        '</p>' +
        "<ul style='list-style-type:circle;'>" + 
            "<li>" + 
            "<div class='custom-control custom-checkbox'>" + 
                "<input type='checkbox' class='custom-control-input category'>"+
                "<label class='custom-control-label'>Select All</label>"+
            "</li></ul>"
    }
    else{
        html_list = "<ul style='list-style-type:circle;'>" + 
        "<li>" + 
        "<div class='custom-control custom-checkbox'>" + 
            "<input type='checkbox' class='custom-control-input category'>"+
            "<label class='custom-control-label'>Select All</label>"+
        "</li></ul>"
    }
    last_testcase_category = ""
    for(var i = 0; i < dataList.length ;i++){
        testData.forEach(function(element){
            if (dataList[i]["category"] == element["category"] && dataList[i]['testId'] == element['testId']){
                check_box_list.push("#defaultChecked"+i)
            }
        })
        if (dataList[i]["category"] == "L3 Traffic Test(IXIA 100G, snake test)"){
            input_html = "<input type='checkbox' class='custom-control-input child-check see_detail' id='defaultChecked"+i+"'>"
        }
        else{
            input_html = "<input type='checkbox' class='custom-control-input child-check' id='defaultChecked"+i+"'>"
        }
        if(i == 0){
            html_list +=                    
                "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                        "<div class='custom-control custom-checkbox'>" + 
                            "<input type='checkbox' class='custom-control-input category'>"+
                            "<label class='custom-control-label'>" + dataList[i]["category"] + "</label>"+
                            "<button class='show_button' type='button'>down</button>"+
                        "</div>"+
                    "</li>"+
                    "<ul style='list-style-type:circle;' class='test'>" +
                        "<li>"+
                            "<div class='custom-control custom-checkbox'>"+
                                input_html+
                                '<input type="text" style="ime-mode:disabled; width:80px; height:30px;" onkeyup="ValidateNumber(this)" />'+
                                "<label class='custom-control-label' >" + dataList[i]["testId"]+ "</label>"+
                                "<label class='custom-control-label' style='font-size:12px' >" + dataList[i]["comment"]+ "</label>"+
                            "</div>"+
                        "</li>"
        }
        else if(last_testcase_category != dataList[i]["category"] && i!= 0){
            
            html_list +=  
                    "</ul>"+
                "</ul>"+
                "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                        "<div class='custom-control custom-checkbox'>" + 
                            "<input type='checkbox' class='custom-control-input category'>"+
                            "<label class='custom-control-label'>" + dataList[i]["category"] + "</label>"+
                            "<button class='show_button' type='button'>down</button>"+
                        "</div>"+
                    "</li>"+
                    "<ul style='list-style-type:circle;' class='test'>"+
                    "<li>"+
                        "<div class='custom-control custom-checkbox'>"+
                            input_html+
                            '<input type="text" style="ime-mode:disabled; width:80px; height:30px;" onkeyup="ValidateNumber(this)" />'+
                            "<label class='custom-control-label' >" + dataList[i]["testId"]+ "</label>"+
                            "<label class='custom-control-label' style='font-size:12px' >"+ dataList[i]["comment"]+ "</label>"+
                        "</div>"+
                    "</li>"
        }
        else{
                html_list += 
                        "<li>"+
                            "<div class='custom-control custom-checkbox' class='test'>"+
                                input_html+
                                '<input type="text" style="ime-mode:disabled; width:80px; height:30px;" onkeyup="ValidateNumber(this)" />'+
                                "<label class='custom-control-label' >" + dataList[i]["testId"]+ "</label>"+
                                "<label class='custom-control-label' style='font-size:12px' >" + dataList[i]["comment"]+ "</label>"+
                            "</div>"+
                        "</li>"
        }
        if(i == dataList.length-1){
            html_list += "</ul></ul>"
        }
        last_testcase_category = dataList[i]["category"]
    }
    $( "#testCase" ).append(html_list);
    html = html_list
    check_box_list.forEach(function(element){
        $(element).attr('checked',true)
        $(element).next().val('1')
    })
    setTestChildClick();
    $(".show_button").parent().parent().next().css("display","None");
    setTestChildDisplay();
    setParentClick();
    clickLabelTriggerLastCheckbox();
    showDetailConfig();
    submitTestCase();
}

let show_DUT_list=function(){
    html = ''
    $.ajax({
        type:'get',
        dataType:'json',
        url:window.location.origin + "/test/save/getDUTList/",
        success:function(data){
            data = data["DUT_list"]
            for(var i=0 ; i < data.length ; i++){
                html += '<li><a>'+data[i]+'</a></li>'
            }
            $("#DUTList").empty()
            $("#DUTList").append(html)
            changeDropdownValue()
        }
    })
}

function ValidateNumber(obj){
    // 清除"数字"和"."以外的字符
    obj.value = obj.value.replace(/[^\d.]/g,"");
    // 验证第一个字符是数字
    obj.value = obj.value.replace(/^\./g,"");
    // 只保留第一个, 清除多余的
    obj.value = obj.value.replace(/\.{2,}/g,".");
    obj.value = obj.value.replace(".","$#$").replace(/\./g,"").replace("$#$",".");
    // 只能输入两个小数
    obj.value = obj.value.replace(/^(\-)*(\d+)\.(\d\d).*$/,'$1$2.$3');
}

let showNextStageSelection = function(){
    $(".addNextStage").click(function(){
        html = html.replace('name="time_period' + String(index) + '"' ,'name="time_period' + String(index+1) + '"')
        html = html.replace('name="time_period' + String(index) + '"' ,'name="time_period' + String(index+1) + '"')
        index += 1
        $(this).prev().attr('id', 'disableButton')
        $(this).prev().attr('disabled', true)
        $(this).next().remove()
        $(this).remove()
        $(".system_T1_Table").append(
            '<div class="x_content panel stage_views" style="float:right"> \
                <div class="panel body" id="testCase" style="height: 500px ;overflow: auto"> \
                    <br><br>' + html +
            '   </div> \
                <a class="btn btn-primary btn-lg" id="submitTestCase" role="button" style="float:right" type="button">Submit</a> \
                <a class="btn btn-primary btn-lg addNextStage" id="addNextStage" role="button" style="float:right" type="button">Add Another Test</a> \
                <a class="btn btn-primary btn-lg addTestScript" id="addTestScript" role="button" style="float:right" type="button">Add Test Script</a> \
                <a class="btn btn-primary btn-lg deleteStage"  role="button" style="float:right" type="button">Cancel</a> \
            </div>'
        )
        setTestChildClick();
        $(".system_T1_Table").children().last(".stage_views").children().children().children().children().children(".show_button").parent().parent().next().css("display","None");
        setTestChildDisplay();
        setParentClick();
        showNextStageSelection();
        deleteStage();
        submitTestCase();
        showDetailConfig();
        clickLabelTriggerLastCheckbox();
        $('html,body').animate({ scrollTop: $(document).height() }, 800);
    })
    $(".addTestScript").click(function(){
        $(this).prev().prev().attr('id', 'disableButton')
        $(this).prev().prev().attr('disabled', true)
        $(this).prev().remove()
        $(this).remove()
        $(".system_T1_Table").append(
            '<div class="x_content panel stage_views" style="float: right"> \
                <div class="col-md-12" id="testCase" style="padding: 10px;"> \
                    <div class="col-md-12"> \
                        <label>  Script type : <input>  \
                            Target type : <input> \
                            Target platform version : <input> \
                        </label> \
                    </div> \
                    <div class="col-md-12"> \
                        <label> Return 0 or "true" at the end of for pass condition or error code (<>0), "nil" for no error check.</label> \
                    </div> \
                    <textarea class="col-md-12"  style="height: 500px; margin: 11px 0 15px 0"></textarea> \
                </div> \
                <a class="btn btn-primary btn-lg" id="submitTestCase" role="button" style="float:right" type="button">Submit</a> \
                <a class="btn btn-primary btn-lg addNextStage" id="addNextStage" role="button" style="float:right" type="button">Add Another Test</a> \
                <a class="btn btn-primary btn-lg addTestScript" id="addTestScript" role="button" style="float:right" type="button">Add Test Script</a> \
                <a class="btn btn-primary btn-lg deleteStage"  role="button" style="float:right" type="button">Cancel</a> \
            </div>'
        )
        showNextStageSelection();
        deleteStage();
        $('html,body').animate({ scrollTop: $(document).height() }, 800);
        submitTestCase();
    })
}

let deleteStage = function(){
    $(".deleteStage").click(function(){
        if ($(this).parent().next().length == 0){
            $(this).parent().prev().children('#disableButton').attr('id', 'submitTestCase')
            $(this).parent().prev().children().removeAttr('disabled')
            if ($(this).parent().prev().children().length >= "3" && $(this).parent().prev().children().length <= "5"){
                $(this).parent().prev().children("#submitTestCase").after(addButton);
                showNextStageSelection();
            }
            else{
                return;
            }
        }
        $(this).parent().remove()
    })
}

let showDetailConfig = function(){
    $(".see_detail").click(function(){
        if($(this)[0].checked){
            $('#c').modal('show')
            $('.modal-header').empty()
            title = $(this).next().next()[0]["firstChild"]['data']
            config_html = '<h1 class="modal-title">' + title +'<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">&times;</span></button></h1>'
            $('.modal-header').append(config_html)
            $('#example_image').empty()
            config_html = '<img src="/static/images/FB/' + title + '.png" style="width:100%">'
            $('#example_image').append(config_html)
        }
    })
}

let initialLoadFunction = function(){
    changeDropdownValue();
    storeImageValue();
    show_DUT_list();
}

addLoadEvent(initialLoadFunction);