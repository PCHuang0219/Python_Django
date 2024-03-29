let initLoadFunction = function(){
    getTestPlanTable()
    createFilterCondition()
    deleteCondition()
    selectCondition()
    runCondition()
}

let getTestPlanTable = function(){
    condition = localStorage.getItem("condition")
    if (!condition){
        condition = ""
    }
    $.ajax({
        type: "get",
        url: window.location.origin + "/test/testCaseManagement/testPlanTable/",
        data:{condition},
        dataType: "json",
        success: function(data, status){
            $(".table tbody").empty();
            let html = ""
            data = data["data"]
            for(var i=0,x=data.length-1 ; x >= 0 ; x--,i++)
            {
                element = JSON.parse(data[x])
                if (!element["project"]){
                    element["project"] = ''
                }
                html +=  
                "<tr>" +
                "<td data-th='#'>"+ element["testcase_topology"] + "</th>" +
                "<td data-th='Headline'>" + element["headline"] + "</td>" +
                "<td data-th='Purpose'>" + element["purpose"] + "</td>" +
                "<td data-th='Cost Time'>" + element["during_time"] + "</td>" +
                "<td data-th='Project' test_plan_id='" + element["_id"] + "'>" + element["project"] + "</td>" +
                "<td data-th='During_time'>" + element["during_time"] + "</td>" +
                "<td data-th='Model'>" + element["model"] + "</td>" +
                "<td data-th='Modify'>" + "<button class='edit' type='button'>Edit</button>"+"</td>" +
                "<td data-th='Last Test'>" + element["last_result"] + "</td>" +
                "</tr>"
            }
            $(".table tbody").append(html);
            $(".seeMore").click(function(){
                localStorage.setItem("test_plan_id",$(this).parent().parent().children().first().next().attr("test_plan_id"));
                location.href = window.location.origin + "/test/testPlanManagement/testPlanDetail"
            });
            $(".execute").click(function(){
                test_plan_id = $(this).parent().parent().children().first().next().attr("test_plan_id");
                location.href = window.location.origin + "/test/?test_plan_id=" + test_plan_id
            });
            $(".edit").click(function(){
                localStorage.setItem("test_plan_id",$(this).parent().parent().children().first().next().attr("test_plan_id"));
                location.href = window.location.origin + "/test/modifyTestPlan"
            });
        },
    })
    localStorage.clear();
}

let createFilterCondition = function(){
    $("#addViewsCondition").click(function(){
        html = '<div class="col-xs-12"> \
                    <div class="col-xs-6"> \
                        Condition<span class="red">*</span>：<br> \
                        <select class="col-xs-6"> \
                            <option>Project</option> \
                            <option>Job Name</option> \
                            <option>Job Description</option> \
                            <option>Submit Time</option> \
                            <option>Start Time</option> \
                            <option>End Time</option> \
                            <option>Result</option> \
                            <option>Status</option> \
                            <option>Platform</option> \
                            <option>Topology</option> \
                            <option>Model</option> \
                        </select> \
                        <a class="btn btn-primary selectCondition">Select</a> \
                    </div> \
                    <div class="col-xs-6"> \
                        Value<span class="red">*</span>：<br> \
                        <select class="col-xs-8"> \
                        </select> \
                        <a class="btn btn-primary deleteCondition">Delete</a> \
                    </div> \
                </div>'
        $("#filtercondition").append(html)
        deleteCondition()
        selectCondition()
    })
}

let deleteCondition = function(){
    $(".deleteCondition").click(function(){
        if ($(this).parent().parent().parent().children().length != 1){
            $(this).parent().parent().remove()
        }
    })
}

let selectCondition = function(){
    $(".selectCondition").click(function(){
        condition = $(this).prev().val()
        condition = condition.toLowerCase()
        condition = condition.replace(' ','_')
        if (condition == 'job_description'){
            condition = 'job_describe'
        }
        if (condition == 'topology'){
            condition = 'testcase_topology'
        }
        $(this).parent().next().children("input").remove()
        value_selection = $(this).parent().next().children("select")
        if (condition.includes('time')){
            value_selection.replaceWith('<select> \
                                            <option>&equiv;</option> \
                                            <option>&le;</option> \
                                            <option>&ge;</option> \
                                        </select> \
                                        <input style="margin-top: 4px" type="date" startDate=”${startTime?datetime}”>')
        }
        else{
            $.ajax({
                type:'get',
                data:{data:condition},
                dataType:'json',
                url: window.location.origin + "/test/get/selectionByCondition/",
                success:function(data){
                    data = data["data"]
                    value_selection.empty()
                    for ( var i=0 ; i < data.length ; i++){
                        value_selection.append("<option>" + data[i] + "</option>")
                    }
                }
            })
        }
    })
}

let dateAdd = function (startDate,days) {
    startDate = new Date(startDate);
    startDate = +startDate + days * 1000 * 60 * 60 * 24;
    startDate = new Date(startDate);
    var nextStartDate = startDate.getFullYear() + "-" + (startDate.getMonth() + 1) + "-" + startDate.getDate();
    return nextStartDate;
}

let runCondition = function(){
    $("#updateTRRViews").click(function(){
        // $(".modal").attr("style","display:none");
        condition_number = $("#filtercondition").children().length
        key_list = ['project','job_name','job_describe','submit_time','start_time','end_time','result',
                    'status','platform','testcase_topology','model']
        project_val = []
        job_name_val = []
        job_describe_val = []
        submit_time_val = []
        start_time_val = []
        end_time_val = []
        result_val = []
        status_val = []
        platform_val = []
        testcase_topology_val = []
        model_val = []

        value_list = [project_val, job_name_val, job_describe_val, submit_time_val, start_time_val, end_time_val,
                    result_val , status_val, platform_val, testcase_topology_val, model_val]
        data = "{"
        for (var i=0 ; i < condition_number ; i++){
            key = $("#filtercondition").children().eq(i).children().eq(0).children().siblings("select").val()
            key = key.toLowerCase()
            key = key.replace(' ','_')
            if (key == 'job_description'){
                key = 'job_describe'
            }
            if (key == 'topology'){
                key = 'testcase_topology'
            }
            if (key.includes('time')){
                operator = $("#filtercondition").children().eq(i).children().eq(1).children().siblings("select").val()
                date = $("#filtercondition").children().eq(i).children().eq(1).children().siblings("input").val()
                value = [operator, date]
            }
            else{
                value = $("#filtercondition").children().eq(i).children().eq(1).children().siblings("select").val()
            }

            if (key == "project"){
                project_val.push(value)
            }
            else if (key == "job_name"){
                job_name_val.push(value)
            }
            else if (key == "job_describe"){
                job_describe_val.push(value)
            }
            else if (key == "submit_time"){
                submit_time_val.push(value)
            }
            else if (key == "start_time"){
                start_time_val.push(value)
            }
            else if (key == "end_time"){
                end_time_val.push(value)
            }
            else if (key == "result"){
                result_val.push(value)
            }
            else if (key == "status"){
                status_val.push(value)
            }
            else if (key == "platform"){
                platform_val.push(value)
            }
            else if (key == "testcase_topology"){
                testcase_topology_val.push(value)
            }
            else if (key == "model"){
                model_val.push(value)
            }

        }
        for (var i=0 ; i < key_list.length ; i ++){
            data = ConvertMutilValueToMongoDB(data, key_list[i], value_list[i])
        }
        data += "}"
        console.log(data)
        localStorage.clear();
        localStorage.setItem("condition",data)
        // location.href = window.location.origin + "/test/jobManagement"
    })
}

let ConvertMutilValueToMongoDB = function(html,key,value_list){
    if (value_list.length >0){
        if (html.indexOf('"') != -1){
            html += ','
        }
        if (value_list.length == 1){
            if (!value_list[0]){
                value_list[0] = ""
            }
            if (!key.includes('time')){
                html += '"' + key + '":"' + value_list[0] + '"'
            }
            else{
                if (value_list[0][0] == '≡'){
                    date = value_list[0][1]
                    nextDate = dateAdd(value_list[0][1], 1)
                    html += '"' + key + '":{"$lte":ISODate("' + nextDate + '"),"$gte":ISODate("' + date + '")}'
                }
                if (value_list[0][0] == '≤'){
                    html += '"' + key + '":{"$lte":ISODate("' + value_list[0][1] + '")}'
                }
                if (value_list[0][0] == '≥'){
                    html += '"' + key + '":{"$gte":ISODate("' + value_list[0][1] + '")}'
                }
            }
        }
        else {
            if (!key.includes('time')){
                buff = "["
            }
            for(var i=0 ; i < value_list.length ; i++){
                if ( i>0 ){
                    buff += ','
                }
                if (!value_list[i]){
                    value_list[i] = ""
                }
                if (!key.includes('time')){
                    buff += '"' + value_list[i]  + '"' 
                }
                else{
                    if (value_list[0][0] == '≡'){
                        buff += '"' + key + '":"ISODate(' + value_list[0][1] + ')"'
                    }
                    if (value_list[0][0] == '≤'){
                        buff += '"' + key + '":{"$lte":"ISODate(' + value_list[0][1] + ')"}'
                    }
                    if (value_list[0][0] == '≥'){
                        buff += '"' + key + '":{"$gte":"ISODate(' + value_list[0][1] + ')"}'
                    }
                     
                }
            }
            if (!key.includes('time')){
                buff += "]"
                html += '"' + key + '":{"$in":' + buff + "}"
            }
            else{
                html += '"' + key + '":{' + buff + "}"
            }
        }
        return html
    }
    return html
}

addLoadEvent(initLoadFunction);