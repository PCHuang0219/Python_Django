let project = localStorage.getItem("project"); // TRR Project Name
let TRR_ID = localStorage.getItem("TRR_ID"); // TRR Project Name

let InitLoadFunction = function(){
    createDescription()
    getTRRContent()
    getDescription()
    createDiscussion()
    getDiscussion()
}
let createDescription = function(){
    $("#createDescription").click(function(){
        description =tinyMCE.activeEditor.getContent()
        if ( description == "" ){
            alert("Please confirm information is complete")
        }
        else{
            $.ajax({
                type: "post",
                url: "http://" + Config.ip_address + Config.port + "/project_management/save/TRRDescription/",
                data:{project:project,TRR_ID:TRR_ID,description:description},
                dataType: "json",
                success: function(data,status){
                    if (status == "success"){
                        location.href =  "http://" + Config.ip_address + Config.port +"/project_management/bug_issue_detail"
                    }
                    else{
                        alert("Create Error !")
                    }
                }
            })
        }
    })
}

let createDiscussion = function(){
    $("#createIssue").click(function(){
        mail = $("#mail").val()
        issue = tinyMCE.activeEditor.getContent()
        if ( mail == "" || issue == "" ){
            alert("Please confirm information is complete")
        }
        else{
            $.ajax({
                type: "post",
                url: "http://" + Config.ip_address + Config.port + "/project_management/save/TRRDiscussion/",
                data:{project:project,TRR_ID:TRR_ID,issue:issue,mail:mail},
                dataType: "json",
                success: function(data,status){
                    if (status == "success"){
                        location.href =  "http://" + Config.ip_address + Config.port +"/project_management/bug_issue_detail"
                    }
                    else{
                        alert("Create Error !")
                    }
                }
            })
        }
    })
}

let getDiscussion = function(){
    $.ajax({
        type:"get",
        data:{"TRR_ID":TRR_ID},
        dataType:"json",
        url:"http://" + Config.ip_address + Config.port + '/project_management/get/TRRDiscussion/',
        success:function(data){
            data = data["data"]
            if (data.length != 0){
                html = '<div class="panel panel-default"><div class="panel-body">'
                for (var i=data.length-1 ; i >= 0 ; i--){
                    html+='<div class="x_panel"><div style="text-align:center;"> = = = = = = = = = = ' + data[i]["submit_time"] + '&nbsp;by : ' + data[i]["user"] + ' = = = = = = = = = = </div>'
                    if (data[i]["mail"]){
                        data[i]["mail"] = data[i]["mail"].replace(new RegExp("\n","g"),"<br>")
                        html+='<p>Email Dummy:</p><div class="maildummy"><h5>' + data[i]["mail"] + '</h5></div>'
                    }
                    data[i]["issue"] = data[i]["issue"].replace(new RegExp("\n","g"),"<br>")
                    html+='<p>Email Content:</p><div class="mailcontent"><h5>' + data[i]["issue"] + '</h5></div></div>'
                }
                html += '</div></div>'
            }
            else{
                html = '<h1> This is no content ! </h1>'
            }
            $("#bugIssue").append(html)
        }
    })
}

let getDescription = function(){
    $.ajax({
        type:"get",
        data:{"TRR_ID":TRR_ID},
        dataType:"json",
        url:"http://" + Config.ip_address + Config.port + '/project_management/get/TRRDescription/',
        success:function(data){
            data = data["data"]
            if (data.length != 0){
                html = '<div class="panel panel-default"><div class="panel-body">'
                for (var i=data.length-1 ; i >= 0 ; i--){
                    html+='<div style="text-align:center;"> = = = = = = = = = = ' + data[i]["submit_time"] + ' = = = = = = = = = = </div>'
                    html+='<h5>' + data[i]["description"] + '</h5>'
                }
                html += '</div></div>'
            }
            else{
                html = '<h1> This is no content ! </h1>'
            }
            $("#bugDescription").append(html)
        }
    })
}

let getTRRContent = function(){
    $.ajax({
        type: "get",
        url: "http://" + Config.ip_address + Config.port + "/project_management/get/TRRContent/",
        data:{ project:project,TRR_ID:TRR_ID},
        dataType: "json",
        success: function(data,status){
            localStorage.setItem("user",data["user"])
            element = data["data"]
            write_main_content(element)
        }
    })
}

let write_main_content = function(data){
    html = '<div class="col-xs-6"> \
                <label class="form-inline">Project : <label style="color:#7700BB">' + data['project'] + '</label></label><br> \
                <label class="form-inline">TRR ID : <label style="color:#7700BB">' + data['TRR_ID'] + '</label></label><br> \
                <label class="form-inline">Start Time : <label style="color:#7700BB">' + data['start_time'] + '</label></label><br> \
                <label class="form-inline">End Time : <label style="color:#7700BB">' + data['end_time'] + '</label></label><br> \
                <label class="form-inline">Status : <label style="color:#7700BB">' + data['status'] + '</label></label><br> \
            </div>'
    $("#bugDetailTitle").append(html);
    data["test_phase"] = data["test_phase"].replace(new RegExp("\\n","g"),"<br>")
    html = '<div class="panel panel-default"> \
                <div class="panel-body"> \
                    <div class="col-xs-6"> \
                        <div class="TRR_title">Test Type :  </div>\
                        <label style="color:#7700BB">' + data["test_type"] + '</label> \
                        <div class="TRR_title">Boot/Loader Version : </div>\
                        <label style="color:#7700BB">' + data["boot"] + '</label> \
                        <div class="TRR_title">Diag Version : </div>  \
                        <label style="color:#7700BB">' + data["diag"] + '</label> \
                        <div class="TRR_title">Profile Name : </div>  \
                        <label style="color:#7700BB">' + data["profile_name"] + '</label> \
                        <div class="TRR_title">Test Phase : </div>  \
                        <label style="color:#7700BB">' + data["test_phase"] + '</label> \
                    </div> \
                    <div class="col-xs-6"> \
                        <div class="TRR_title">Software Project Lead : </div>\
                        <label style="color:#7700BB">' + data["PL"] + '</label> \
                        <div class="TRR_title">Project Manager : </div>  \
                        <label style="color:#7700BB">' + data["PM"] + '</label> \
                        <div class="TRR_title">H/W Version : </div>\
                        <label style="color:#7700BB">' + data["H/W"] + '</label> \
                        <div class="TRR_title">S/W Version : </div>  \
                        <label style="color:#7700BB">' + data["S/W"] + '</label> \
                        <div class="TRR_title">Code Base : </div>  \
                        <label style="color:#7700BB">' + data["code"] + '</label> \
                    </div> \
                </div> \
            </div>'
    title_html = '<div class="col-xs-6"> \
                    <a href="#" file="bios"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a> \
                    <label class="form-inline">&nbsp;&nbsp;BIOS Version : <label style="color:#7700BB">' + data['bios'] + '</label></label><br> \
                    <a href="#" file="diag"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a> \
                    <label class="form-inline">&nbsp;&nbsp;DIAG Version : <label style="color:#7700BB">' + data['diag'] + '</label></label><br> \
                    <a href="#" file="cpld"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a> \
                    <label class="form-inline">&nbsp;&nbsp;CPLD Version : <label style="color:#7700BB">' + data['cpld'] + '</label></label><br> \
                    <a href="#" file="onie"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a> \
                    <label class="form-inline">&nbsp;&nbsp;ONIE Version : <label style="color:#7700BB">' + data['onie'] + '</label></label><br> \
                </div>'
    $("#bugDetailTitle").append(title_html)
    $("#bugDtail").empty();
    $("#bugDtail").append(html);
    downlaodFile()
}

let downlaodFile = function(){
    $(".glyphicon-download-alt").click(function(){
        file = $(this).parent().attr("file")
        location.href = "http://210.63.221.19:8888/TRR/" + project + "/" + TRR_ID + "/" + file + ".zip"
    })
}

addLoadEvent(InitLoadFunction);