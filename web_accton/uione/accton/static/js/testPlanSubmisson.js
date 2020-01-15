let changeDropdownValue = function(){
    $(".dropdown-menu li a").click(function(){
        $(this).parents(".dropdown").find('.btn').html($(this).text() + '<span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
     });
}

let isShow = false;
let testData = []
let test_plan_id = ""

let initLoadPage = function(){
    if (localStorage.getItem("test_plan_id")){
        test_plan_id = localStorage.getItem("test_plan_id")
        enterValueByTestPlan(test_plan_id)
    }
    localStorage.clear();
    changeDropdownValue()
    show_DUT_list()
    submitTestCase()
    modifyTestPlan()
}

let enterValueByTestPlan = function(test_plan_id){
    $.ajax({
        type:'get',
        url:'http://' + Config.ip_address + Config.port + '/test/testPlanManagement/detail/',
        data:{test_plan_id :test_plan_id},
        dataType:'json',
        success:function(data){
            data = data['detail']
            $('#project').val(data['project'])
            $('#headline').val(data['headline'])
            $('#purpose').val(data['purpose'])
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
                $(".custom-control-input").prop("checked",true);
            }
            ($(this).parent().parent().next().children().children().children("input").prop("checked",true));        
        }
        else{
            if ( $(this).next("label").text() == "Select All" ){
                $(".custom-control-input").prop("checked",false);
            }
            ($(this).parent().parent().next().children().children().children("input").prop("checked",false));        
        }
    });
}

let setParentClick = function(){
    $(".child-check").click(function(){
        parent_node = $(this).parent().parent().parent().prev().children().children("input")
        child_list = $(this).parent().parent().parent().children().children().children("input")
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

let setTestChildDisplay = function(){
    $(".show_button").click(function(){
        if(isShow){
            $(this).parent().parent().next().css("display","None");
            isShow = false;
        }    
        else{
            $(this).parent().parent().next().css("display","block");
            isShow = true;
        }
    });
}

let submitTestCase = function(){
    $('#createTestPlan').click(function(){
        let value_list =  []
        break_val = 'False'
        $('#testCase input[type="checkbox"]:checked').each(function(){
            let type = ($(this).parent().parent().parent().parent().first().children().children().children().next().text())
            type = type.slice(0,-4);
            if(type.toString().length < 50){
                if(type.toString().length == 0){
                    value_list.push($(this).next().text());
                }
                else{
                    test_case = $(this).next().text()
                    value_list.push(type + "--" + test_case);                    
                }
            }
        });
        project = document.getElementById("project").value;
        headline = document.getElementById("headline").value;
        purpose = document.getElementById("purpose").value;
        if (project == ''){
            alert("Project cannot be empty.");
        }
        else if(headline == ''){
            alert("Headline cannot be empty.");
        }
        else if(purpose == ''){
            alert("Purpose cannot be empty.")
        }
        else if(value_list.length == 0){
            alert("Please select at least one testcase.");
        }
        else{
            $.ajax({
                type:'post',
                url:"http://"+ Config.ip_address + Config.port +"/test/createTestPlan/",
                data:{project: project,headline: headline,purpose: purpose,testList: value_list,platform: platform_name,
                    model: model_name,topology: topology_name,},
                dataType:'json',
                success:function(data){
                    location.href = "http://" + Config.ip_address + Config.port + "/test/testPlanManagement"
                }
            })
        }
    })
}

let modifyTestPlan = function(){
    $("#modifyTestPlan").click(function(){
        if (test_plan_id == ""){
            $('#createTestPlan').trigger('click')
        }
        else{
            let value_list =  []
        break_val = 'False'
        $('#testCase input[type="checkbox"]:checked').each(function(){
            let type = ($(this).parent().parent().parent().parent().first().children().children().children().next().text())
            type = type.slice(0,-4);
            if(type.toString().length < 50){
                if(type.toString().length == 0){
                    value_list.push($(this).next().text());
                }
                else{
                    test_case = $(this).next().text()
                    value_list.push(type + "--" + test_case);                    
                }
            }
        });
        project = document.getElementById("project").value;
        headline = document.getElementById("headline").value;
        purpose = document.getElementById("purpose").value;
        if (project == ''){
            alert("Project cannot be empty.");
        }
        else if(headline == ''){
            alert("Headline cannot be empty.");
        }
        else if(purpose == ''){
            alert("Purpose cannot be empty.")
        }
        else if(value_list.length == 0){
            alert("Please select at least one testcase.");
        }
        else{
            $.ajax({
                type:'post',
                url:"http://"+ Config.ip_address + Config.port +"/test/modifyTestPlan/",
                data:{test_plan_id: test_plan_id, project: project, headline: headline, purpose: purpose,
                    testList: value_list, platform: platform_name, model: model_name, topology: topology_name,},
                dataType:'json',
                success:function(data){
                    location.href = "http://" + Config.ip_address + Config.port + "/test/testPlanManagement"
                }
            })
        }
        }
    })
}

let selectTestCase = function(){
    platform_name = $('#platform_choose button').text();
    model_name = $('#model_choose button').text();
    topology_name = $('#topology_choose button').text();
    $.ajax({
        type:'post',
        url:"http://" + Config.ip_address + Config.port +"/test/testCaseList/",
        data:{platform:platform_name,model: model_name,topology: topology_name},
        dataType:'json',
        success:function(data, status){
            platform = data["platform"]
            data = data["testData"]
            show_testcase_view(data,platform);
        }
    });
}

let show_testcase_view = function(dataList,platform){
    let check_box_list = []
    $( "#testCase" ).empty();
    last_testcase_category = ""
    let html_list = "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                    "<div class='custom-control custom-checkbox'>" + 
                    "<input type='checkbox' class='custom-control-input category' id='defaultCheckedall'>"+
                    "<label class='custom-control-label' for='defaultCheckedall'>Select All</label>"+
                    "</li></ul>"
    let j = 100000
    for(var i = 0; i < dataList.length;i++){
        testData.forEach(function(element){
            if (dataList[i]["category"] == element["category"] && dataList[i]['testId'] == element['testId']){
                check_box_list.push("#defaultChecked"+i)
            }
        })
        if(i == 0){
            html_list +=                    
                "<ul style='list-style-type:circle;'>" + 
                "<li>" + 
                "<div class='custom-control custom-checkbox'>" + 
                "<input type='checkbox' class='custom-control-input category' id='defaultChecked"+j+"'>"+
                "<label class='custom-control-label' for='defaultChecked"+j+"'>" + dataList[i]["category"] + "</label>"+
                "<button class='show_button' type='button'>down</button>"+
                "</div>"+
                "</li>"+
                "<ul style='list-style-type:circle;' class='test'>" +
                "<li>"+
                "<div class='custom-control custom-checkbox'>"+
                "<input type='checkbox' class='custom-control-input child-check' id='defaultChecked"+i+"'>"+
                "<label class='custom-control-label' for='defaultChecked"+i+"'>" + dataList[i]["testId"]+ "</label>"+
                "<label class='custom-control-label' style='font-size:12px' for='defaultChecked"+i+"'>" + dataList[i]["comment"]+ "</label>"+
                "</div>"+
                "</li>"
            j -= 1 ;
        }
        else if(last_testcase_category != dataList[i]["category"] && i!= 0){
            html_list +=  
                "</ul>"+
                "</ul>"+
                "<ul style='list-style-type:circle;'>" + 
                "<li>" + 
                "<div class='custom-control custom-checkbox'>" + 
                "<input type='checkbox' class='custom-control-input category' id='defaultChecked"+j+"'>"+
                "<label class='custom-control-label' for='defaultChecked"+j+"'>" + dataList[i]["category"] + "</label>"+
                "<button class='show_button' type='button'>down</button>"+
                "</div>"+
                "</li>"+
                "<ul style='list-style-type:circle;' class='test'>"+
                "<li>"+
                "<div class='custom-control custom-checkbox'>"+
                "<input type='checkbox' class='custom-control-input child-check' id='defaultChecked"+i+"'>"+
                "<label class='custom-control-label' for='defaultChecked"+i+"'>" + dataList[i]["testId"]+ "</label>"+
                "<label class='custom-control-label' style='font-size:12px' for='defaultChecked"+i+"'>"+ dataList[i]["comment"]+ "</label>"+
                "</div>"+
                "</li>"
            j -= 1
        }
        else{
            html_list += 
                "<li>"+
                "<div class='custom-control custom-checkbox' class='test'>"+
                "<input type='checkbox' class='custom-control-input child-check' id='defaultChecked"+i+"'>"+
                "<label class='custom-control-label' for='defaultChecked"+i+"'>" + dataList[i]["testId"]+ "</label>"+
                "<label class='custom-control-label' style='font-size:12px' for='defaultChecked"+i+"'>" + dataList[i]["comment"]+ "</label>"+
                "</div>"+
                "</li>"
        }
        if(i == dataList.length-1){
            html_list += "</ul>"
            html_list += "</ul>"
        }
        last_testcase_category = dataList[i]["category"]
    }

    $( "#testCase" ).append(
        html_list
    );
    check_box_list.forEach(function(element){
        $(element).attr('checked',true)
    })
    setTestChildClick();
    $(".show_button").parent().parent().next().css("display","None");
    setTestChildDisplay();
    setParentClick();
}

let show_DUT_list=function(){
    html = ''
    $.ajax({
        type:'get',
        dataType:'json',
        url:"http://" + Config.ip_address + Config.port + "/test/save/getDUTList/",
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

addLoadEvent(initLoadPage);