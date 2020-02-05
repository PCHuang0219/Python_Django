let InitLoadFunction = function(){
    createTRR()
    getTRRList()
    getProjectList()
    updateTRRContent()
    uploadTRRstatus()
    getAllTDList()
    showTCByTD()
    createFilterCondition()
    selectCondition()
    runCondition()
}

let createTRR = function(){
    $("#createTRR").click(function(){
        project = $("#project").val()
        startTime = $("#startTime").val()
        endTime = $("#endTime").val()
        TRR_ID = $("#trrid").val()
        bios = $("#bios").val()
        diag = $("#diag").val()
        cpld = $("#cpld").val()
        onie = $("#onie").val()
        SW = $("#sw").val()
        HW = $("#hw").val()
        PL = $("#pl").val()
        PM = $("#project_manager").val()
        test_type = $("#test_type").val()
        test_phase = $("#test_phase").val()
        boot = $("#boot_version").val()
        profile_name = $("#profile_name").val()
        test_module = $("#module").val()
        code = project + " " + SW
        if ( project == "" || startTime == "" || endTime == "" || TRR_ID == "" || bios == "" || diag == "" || cpld == "" || onie == "" || SW == "" || HW == "" || PL == "" || PM == "" || test_type == "" || test_phase == "" || boot_version == "" || profile_name == ""){
            alert("Please confirm information is complete")
        }
        else{
            issue = {"project":project,"start_time":startTime,"end_time":endTime,"status":status,"TRR_ID":TRR_ID,"module":test_module,"TRR_ID":TRR_ID,
                    "bios":bios,"diag":diag,"cpld":cpld,"onie":onie,"S/W":SW,"H/W":HW,"module":test_module,"test_type":test_type,"test_phase":test_phase,
                    "boot":boot,"profile_name":profile_name,"code":code}
            postTRR(issue)
        }
    })
}

let postTRR = function(data_info){
    $.ajax({
        type: "post",
        url: window.location.origin + "/project_management/save/TRR/",
        data:{"project":data_info["project"],"start_time":data_info["start_time"],"end_time":data_info["end_time"], "status":data_info["status"],
            "TRR_ID":data_info["TRR_ID"],"module":data_info["module"],"bios":data_info["bios"],"diag":data_info["diag"],"cpld":data_info["cpld"],
            "onie":data_info["onie"],"S/W":data_info["S/W"],"H/W":data_info["H/W"],"module":data_info["module"],"test_type":data_info["test_type"],
            "test_phase":data_info["test_phase"],"boot":data_info["boot"],"profile_name":data_info["profile_name"],"code":data_info["code"]},
        dataType: "json",
        success: function(data,status){
            type = typeof(data)
            if (type != "string"){
                location.href =  window.location.origin +"/project_management/"
            }
            else{
                alert("Sorry, You can't access to create data !")
            }
        }
    })
}

let getProjectList = function(){
    $.ajax({
        type:'get',
        url: window.location.origin + '/project_management/get/projectList/',
        dataType:'json',
        success:function(data){
            data = data["data"]
            for (var i=0 ; i < data.length ; i++){
                data[i] = JSON.parse(data[i])
                html = '<option>' + data[i]["project_name"] + '</option>'
                $("#project").append(html)
            }
        }
    })
}

let getTRRList = function(){
    data = localStorage.getItem("condition")
    if (!data){
        data = ""
    }
    $.ajax({
        type: "get",
        url: window.location.origin + "/project_management/get/TRRViewsByCondition/",
        data:{data},
        dataType: "json",
        success: function(data,status){
            data = data["data"]
            html = ''
            TRR_list = ''
            for ( var i=data.length-1 ; i >= 0 ; i--){
                element = JSON.parse(data[i])
                html = writeTRRListHtml(element,html)
                TRR_list += '<option>' + element["TRR_ID"] + '</option>'
            }
            $("#issue_content").empty()
            $("#issue_content").append(html)
            $("#trrlist").append(TRR_list)
            $(".tablesorter").tablesorter();
            $(".detailButton").click(function(){
                project = $(this).parent().siblings(":first").text()
                TRR_ID = $(this).parent().prev().prev().text()
                localStorage.setItem("project",project);
                localStorage.setItem("TRR_ID",TRR_ID);
                location.href = window.location.origin + "/project_management/TR_Detail"
            })
            changeTRRstatus();
        }
    })
    localStorage.clear();
}

let writeTRRListHtml = function(data,html){
    if (!data["MEDF"]){
        data["MEDF"] = ""
    }
    if(data["status"] == "Submitted"){
        data["status"] = '<td data-th="Status"><button class="btn btn-primary trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Verified"){
        data["status"] = '<td data-th="Status"><button class="btn btn-secondary trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Verified"){
        data["status"] = '<td data-th="Status"><button class="btn btn-secondary trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Assigned"){
        data["status"] = '<td data-th="Status"><button class="btn btn-info trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Closed"){
        data["status"] = '<td data-th="Status"><button class="btn btn-dark trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Cancelled"){
        data["status"] = '<td data-th="Status"><button class="btn btn-warning trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Resloved"){
        data["status"] = '<td data-th="Status"><button class="btn btn-success trrstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    html += '<tr> \
                <td data-th="Project">' + data["project"] + '</td> \
                <td data-th="Model">' + data["module"] + '</td> \
                <td data-th="Submit Time">' + data["submit_time"] + '</td> \
                <td data-th="Start Time">' + data["start_time"] + '</td> \
                <td data-th="End Time">' + data["end_time"] + '</td> \
                <td data-th="M.E.D.F">' + data["MEDF"] + '</td> \
                <td data-th="TRR ID">' + data["TRR_ID"] + '</td> ' + data["status"] + ' \
                <td data-th="Detail"><button class="btn btn-link detailButton" type="button" style="width:50px">detail</button></td> \
                <td data-th="H/W">' + data["H/W"] + '</td> \
                <td data-th="S/W">' + data["S/W"] + '</td> \
                <td data-th="bios">' + data["bios"] + '</td> \
            </tr>'
            // <td data-th="EPR"><button class="btn btn-link" type="button">EPR</button></td> \
        return html
}
var TRR_ID = ""
let changeTRRstatus = function(){
    list = ['Submitted','Verified','Assigned','Closed','Cancelled','Resloved']
    $(".trrstatus").click(function(){
        $("#changeStatusContent").empty()
        index = list.indexOf($(this).text())
        html = ''
        if ($(this).text() == "Submitted" || $(this).text() == "Verifed" || $(this).text() == "Assigned"){
            for(var i=index ; i<list.length ; i++){
                html += '<option>' + list[i] + '</option>'
            }
        }
        else{
            for(var i=3 ; i<list.length ; i++){
                html += '<option>' + list[i] + '</option>'
            }
        }
        $("#changeStatusContent").append(html)
        TRR_ID = $(this).parent().prev().text()
        project = $(this).parent().parent().children().first().text()
    })
}

let uploadTRRstatus = function(){
    $("#changeTRRStatus").click(function(){
        status = $("#changeStatusContent").val()
        TLConfirm = $("#TLConfirm").val()
        data_list = []
        if (status == "Verified"){
            data=TLConfirm
            MEDF=""
        }
        else if (status == "Assigned"){
            count = $("#assignContent").children().length;
            TC = []
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
            var yyyy = today.getFullYear();
            max_date = yyyy + '-' + mm + '-' + dd ;

            for (var i=0 ; i < count ; i++){
                bar = $("#assignContent").children().eq(i)
                TD = bar.children().eq(0).children("select").val()
                $('#assignContent input[type="checkbox"]:checked').each(function(){
                    TC.push($(this).next().text())
                })
                engineer = bar.children().eq(2).children("select").val()
                end_date_org = bar.children().eq(3).children("input").val()
                
                compareResult = compareDate(end_date_org,max_date)
                if (compareResult == "true"){
                    max_date = end_date_org
                }
                num = i+1
                Task_ID = TRR_ID + "-" + (Array(2).join('0') + num).slice(-2)
                data_list.push(TD + "/" + TC + "/" + engineer + "/" + end_date_org + "/" + Task_ID + "/" + project + "/" + TRR_ID)
            }
            data = data_list
            MEDF = max_date
        }
        else{
            data = ""
            MEDF = ""
        }
        $.ajax({
            type:"post",
            url: window.location.origin + "/project_management/save/changeTRRStatus/",
            dataType:"json",
            data:{"TRR_ID":TRR_ID,"status":status,"content":data,"MEDF":MEDF},
            success:function(){
                location.href =  window.location.origin +"/project_management/"
            }
        })
    })
}

let compareDate = function(date1,date2){
    date1 = date1.replace(/\-/gi,"/");
    date2 = date2.replace(/\-/gi,"/");
    var time1 = new Date(date1).getTime();
    var time2 = new Date(date2).getTime();
    if(time1 < time2){
        return 'false';
    }
    else if(time1 == time2){
        return 'false';
    }
    else{
        return 'true';
    }
}

let getAllTDList = function(){
    $.ajax({
        type:'get',
        url: window.location.origin + "/project_management/get/TDList/",
        success:function(data){
            data = data["data"]
            $(".TDList").empty()
            html = ''
            for(var i=0; i < data.length ; i++){
                element = JSON.parse(data[i])
                html += "<option>" + element["TD_ID"] + "</option>"
            }
            $(".TDList").append(html)
            getAllTCList(html)
        }
    })
}

let getAllTCList = function(TD_html){
    TD_ID = $(".TDList").val()
    $.ajax({
        type:'get',
        url: window.location.origin + "/project_management/get/TCList/",
        data:{"TD_ID":TD_ID},
        dataType: 'json',
        success:function(data){
            data = data["data"]
            $(".TCList").empty()
            html = ''
            for(var i=0; i < data.length ; i++){
                element = JSON.parse(data[i])
                html += '<input type="checkbox"><label>' + element["TC_ID"] + '</label><br>'
            }
            $(".TCList").append(html)
            showStatusViews(TD_html,html)
        }
    })
}

let showTCByTD = function(){
    $(".selectTD").click(function(){
        TD_ID = $(this).prev().prev().prev().val()
        button_odm = $(this)
        $.ajax({
            type:'get',
            url: window.location.origin + "/project_management/get/TCList/",
            data:{"TD_ID":TD_ID},
            dataType: 'json',
            success:function(data){
                data = data["data"]
                html = ''
                for(var i=0; i < data.length ; i++){
                    element = JSON.parse(data[i])
                    html += '<input type="checkbox"><label>' + element["TC_ID"] + '</label><br>'
                }
                button_odm.parent().next().children(".TCList").empty()
                button_odm.parent().next().children(".TCList").append(html)
            }
        })
    })
}

let showStatusViews = function(TD_html,TChtml){
    $("#changeStatusContent").click(function(){
        status = $("#changeStatusContent").val()
        if (status == "Verified"){
            $("#verifiedContent").attr("style","display:block;")
            $("#assignContent").attr("style","display:none;")
            $("#addAsignBar").attr("style","display:none;")
        }
        else if (status == "Assigned"){
            $("#verifiedContent").attr("style","display:none;")
            $("#assignContent").attr("style","display:initial;")
            $("#addAsignBar").attr("style","display:initial;")
        }
        else{
            $("#verifiedContent").attr("style","display:none;")
            $("#assignContent").attr("style","display:none;")
            $("#addAsignBar").attr("style","display:none;")
        }
    })
    $("#addAsignBar").click(function(){
        $("#assignContent").append('<div class="col-xs-12 x_panel"> \
                                        <div class="col-xs-6"> \
                                            TD List <span class="red">*</span>：<br> \
                                            <select class="TDList" class="statusComment"> \
                                                ' + TD_html + ' \
                                            </select> \
                                        </div> \
                                        <div class="col-xs-6"> \
                                            TC List <span class="red">*</span>：<br> \
                                            <div class="TCList" class="statusComment"> \
                                                ' + TChtml + '\
                                            </div> \
                                        </div> \
                                        <div class="col-xs-6"> \
                                            Engineer <span class="red">*</span>：<br> \
                                            <select class="engineer" class="statusComment"> \
                                                <option>River</option> \
                                                <option>Mark</option> \
                                                <option>Joe</option> \
                                                <option>Juice</option> \
                                                <option>Iris</option> \
                                                <option>Brian</option> \
                                                <option>Gino</option> \
                                                <option>Blithe</option> \
                                                <option>Henry</option> \
                                            </select> \
                                        </div> \
                                        <div class="col-xs-6"> \
                                            M.E.D.F. <span class="red">*</span>：<br> \
                                            <input class="MEDF" type="date" class="statusComment"> \
                                        </div> \
                                    </div> '
                                    )
    })
    showTCByTD()
}

let updateTRRContent = function(){
    $("#updateTRRContent").click(function(){
        type = $("#changeType").val()
        content = $("#content").val()
        TRR_ID = $("#trrlist").val()
        if (type == "BIOS"){
            type = "bios"
        }
        else if (type == "Diag"){
            type = "diag"
        }
        else if (type == "ONIE"){
            type = "onie"
        }
        else if (type == "CPLD"){
            type = "cpld"
        }
        $.ajax({
            type:'post',
            url:window.location.origin + "/project_management/save/updateTRRContent/",
            data:{"type":type,"content":content,"TRR_ID":TRR_ID},
            dataType:'json',
            success:function(data,status){
                if (data["result"] == 'True'){
                    location.href =  window.location.origin +"/project_management/"
                }
                else{
                    alert("Update Error !")
                }
            }
        })
    })
}

let createFilterCondition = function(){
    $("#addViewsCondition").click(function(){
        html = '<div class="col-xs-12"> \
                    <div class="col-xs-6"> \
                        Condition<span class="red">*</span>：<br> \
                        <select class="col-xs-6"> \
                            <option>Project</option> \
                            <option>Module</option> \
                            <option>TRR_ID</option> \
							<option>Status</option> \
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
        if (condition == "Project" || condition == "Module" || condition == "Status"){
            condition = condition.toLowerCase()
        }
        value_selection = $(this).parent().next().children("select")
        $.ajax({
            type:'get',
            data:{data:condition},
            dataType:'json',
            url: window.location.origin + "/project_management/get/selectionByCondition/",
            success:function(data){
                data = data["data"]
                value_selection.empty()
                for ( var i=0 ; i < data.length ; i++){
                    value_selection.append("<option>" + data[i] + "</option>")
                }
            }
        })
    })
}

let runCondition = function(){
    $("#updateTRRViews").click(function(){
        $(".modal").attr("style","display:none");
        condition_number = $("#filtercondition").children().length
        project_val = []
        module_val = []
        status_val = []
        TRR_ID_val = []
        data = "{"
        for (var i=0 ; i < condition_number ; i++){
            key = $("#filtercondition").children().eq(i).children().eq(0).children().siblings("select").val()
            value = $("#filtercondition").children().eq(i).children().eq(1).children().siblings("select").val()
            if (key == "Project" || key == "Module" || key == "Status"){
                key = key.toLowerCase()
            }
            if (key == "project"){
                project_val.push(value)
            }
            else if (key == "module"){
                module_val.push(value)
            }
            else if (key == "TRR_ID"){
                TRR_ID_val.push(value)
            }
            else if (key == "status"){
                status_val.push(value)
            }
        }
        data = ConvertMutilValueToMongoDB(data,"project",project_val)
        data = ConvertMutilValueToMongoDB(data,"module",module_val)
        data = ConvertMutilValueToMongoDB(data,"TRR_ID",TRR_ID_val)
        data = ConvertMutilValueToMongoDB(data,"status",status_val)
        data += "}"
        localStorage.clear();
        localStorage.setItem("condition",data)
        location.href = window.location.origin + "/project_management/"
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
            html += '"' + key + '":"' + value_list[0] + '"'
        }
        else {
            buff = "["
            for(var i=0 ; i < value_list.length ; i++){
                if ( i>0 ){
                    buff += ','
                }
                if (!value_list[i]){
                    value_list[i] = ""
                }
                buff += '"' + value_list[i]  + '"' 
            }
            buff += "]"
            html += '"' + key + '":{"$in":' + buff + "}"
        }
        return html
    }
    return html
}

addLoadEvent(InitLoadFunction);