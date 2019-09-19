let changeDropdownValue = function(){
    $(".dropdown-menu li a").click(function(){
        $(this).parents(".dropdown").find('.btn').html($(this).text() + '<span class="caret"></span>');
        $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
     });
}
let storeImageValue =function() {
    if(localStorage.getItem("change_page") == "1") {
        let image_path = (localStorage.getItem("image_path"))
        let job_name = (localStorage.getItem("job_name"))
        let job_description = (localStorage.getItem("job_description"))
        document.getElementById('build_image_location').value = image_path
        document.getElementById('job_name').value = job_name
        document.getElementById('job_description').value = job_description
    }
    localStorage.clear();
}
let isShow = false;
let platform_name = $('#platform_choose button').text();
let model_name = $('#model_choose button').text();
let topology_name = $('#topology_choose button').text();

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

let saveInformation = function(){
    job_name = document.getElementById('job_name').value
    job_description = document.getElementById('job_description').value
    localStorage.setItem("job_name",job_name);
    localStorage.setItem("job_description",job_description)
    location.href = "http://" + Config.ip_address + Config.port + "/test/jenkinsViews"
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
    let value_list =  []
    $('#testCase input[type="checkbox"]:checked').each(function(){
        let type = ($(this).parent().parent().parent().parent().first().children().children().children().next().text())
        type = type.slice(0,-4);
        if(type.toString().length < 50){
            if(type.toString().length == 0){
                value_list.push($(this).next().text());
            }
            else{
                value_list.push(type + "/" + $(this).next().text());
            }
        }
    });
    job_name = document.getElementById("job_name").value;
    job_description = document.getElementById("job_description").value;
    image_version = document.getElementById("build_image_location").value;
    var radios = document.getElementsByName('Schedle');
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
    if(job_name == ''){
        alert("job_name cannot be empty");
    }
    else if(execute_time == ''){
        alert("Execute Time cannot be empty")
    }
    else if(value_list.length == 0){
        alert("please select at least one testcase");
    }
    else{
        $.ajax({
            type:'post',
            url:"http://"+ Config.ip_address + Config.port +"/test/submitTestcase/",
            data:{job_name: job_name,job_description: job_description,testList: value_list,platform: platform_name,
                model: model_name,topology: topology_name,execute_time: execute_time,image_version: image_version,},
            dataType:'json',
            success:function(data){
                localStorage.setItem("jobId",data["job_id"]);
                localStorage.setItem("platform",platform_name);
                if(execute_time == "now"){
                    location.href = "http://" + Config.ip_address + Config.port +"/test/status";
                }
                else{
                    location.href = "http://" + Config.ip_address + Config.port +"/test/jobManagement";
                }
            }
        })
    }
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

let show_testcase_view = function(testData,platform){
    $( "#testCase" ).empty();
    last_testcase_category = ""
    let html_list = "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                    "<div class='custom-control custom-checkbox'>" + 
                    "<input type='checkbox' class='custom-control-input category' id='defaultCheckedall'>"+
                    "<label class='custom-control-label' for='defaultCheckedall'>Select All</label>"+
                    "</li></ul>"
    let j = 100000
    if ( platform != "Facebook"){
        for(var i = 0; i < testData.length;i++){
            if(i == 0){
                html_list +=                    
                    "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                    "<div class='custom-control custom-checkbox'>" + 
                    "<input type='checkbox' class='custom-control-input category' id='defaultChecked"+j+"'>"+
                    "<label class='custom-control-label' for='defaultChecked"+j+"'>" + testData[i]["category"] + "</label>"+
                    "<button class='show_button' type='button'>down</button>"+
                    "</div>"+
                    "</li>"+
                    "<ul style='list-style-type:circle;' class='test'>" +
                    "<li>"+
                    "<div class='custom-control custom-checkbox'>"+
                    "<input type='checkbox' class='custom-control-input' id='defaultChecked"+i+"'>"+
                    "<label class='custom-control-label' for='defaultChecked"+i+"'>" + testData[i]["testId"]+ "</label>"+
                    "</div>"+
                    "</li>"
                j -= 1 ;
            }
            else if(last_testcase_category != testData[i]["category"] && i!= 0){
                html_list +=  
                    "</ul>"+
                    "</ul>"+
                    "<ul style='list-style-type:circle;'>" + 
                    "<li>" + 
                    "<div class='custom-control custom-checkbox'>" + 
                    "<input type='checkbox' class='custom-control-input category' id='defaultChecked"+j+"'>"+
                    "<label class='custom-control-label' for='defaultChecked"+j+"'>" + testData[i]["category"] + "</label>"+
                    "<button class='show_button' type='button'>down</button>"+
                    "</div>"+
                    "</li>"+
                    "<ul style='list-style-type:circle;' class='test'>"+
                    "<li>"+
                    "<div class='custom-control custom-checkbox'>"+
                    "<input type='checkbox' class='custom-control-input' id='defaultChecked"+i+"'>"+
                    "<label class='custom-control-label' for='defaultChecked"+i+"'>" + testData[i]["testId"]+ "</label>"+
                    "</div>"+
                    "</li>"
                j -= 1
            }
            else{
                html_list += 
                    "<li>"+
                    "<div class='custom-control custom-checkbox' class='test'>"+
                    "<input type='checkbox' class='custom-control-input' id='defaultChecked"+i+"'>"+
                    "<label class='custom-control-label' for='defaultChecked"+i+"'>" + testData[i]["testId"]+ "</label>"+
                    "</div>"+
                    "</li>"
            }
            if(i == testData.length-1){
                html_list += "</ul>"
                html_list += "</ul>"
            }
            last_testcase_category = testData[i]["category"]
        }
    }
    else{
        for(var i = 0; i < testData.length;i++){
            html_list += "<ul style='list-style-type:circle;'>" + 
                        "<li>"+
                        "<div class='custom-control custom-checkbox'>"+
                        "<input type='checkbox' class='custom-control-input' id='defaultChecked"+i+"'>"+
                        "<label class='custom-control-label' for='defaultChecked"+i+"'>" + testData[i]["testId"]+ "</label>"+
                        "</div>"+
                        "</li></ul>"
            if(i == testData.length-1){
                html_list += "</ul>"
                html_list += "</ul>"
            }
            last_testcase_category = testData[i]["category"]
        }
    }
       
    $( "#testCase" ).append(
        html_list
    );
    setTestChildClick();
    $(".show_button").parent().parent().next().css("display","None");
    setTestChildDisplay();
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

let get_testcases_list=function(){
    $.ajax({
        type:'get',
        dataType:'json',
        url:"http://" + Config.ip_address + Config.port + "/test/save/getTestcasesList/",
        success:function(data){
            data = data["testcases_list"]
            show_testcase_view(data);

        }
    })
}

addLoadEvent(changeDropdownValue);
addLoadEvent(storeImageValue);
addLoadEvent(show_DUT_list);
