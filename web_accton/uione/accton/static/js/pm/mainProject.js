let InitLoadFunction = function(){
    creatMainProject()
    getProjectData()
}
const customer = $("#customer").text().split(" ")[0]

let creatMainProject = function(){
    $("#createMainProject").click(function(){
        var cust_model = $("#custModel").val()
        var project_name = $("#projectName").val()
        var description = $("#modelDes").val()
        var PL = $("#pl").val()
        var PM = $("#pm").val()
        if ( cust_model == "" || project_name == "" || description == ""){
            alert("Please confirm information is complete")
        }
        else{
            data = {"cust_model":cust_model,
                    "project_name":project_name,
                    "description":description,
                    "customer":customer,
                    "PL":PL,
                    "PM":PM}
            postData(data)
        }
    })
}

let postData = function(data){
    $.ajax({
        type: "post",
        url: "http://" + Config.ip_address + Config.port + "/project_management/save/mainProjectData/",
        data:{cust_model:data["cust_model"],project_name:data["project_name"],description:data["description"],customer:data["customer"]},
        dataType: "json",
        success: function(data,status){
            if (status == "success"){
                location.href =  "http://" + Config.ip_address + Config.port +"/project_management/att"
            }
            else{
                alert("Create Error !")
            }
        }
    })
}

let getProjectData = function(){
    $.ajax({
        type: "get",
        url: "http://" + Config.ip_address + Config.port + "/project_management/get/mainProjectData/",
        data:{customer:customer},
        dataType: "json",
        success: function(data){
            data = data["data"]
            html = ''
            for (var i=0 ; i < data.length ; i++){
                element = JSON.parse(data[i])
                html = write_html(element,html)
            }
            $("#project_content").empty()
            $("#project_content").append(html)
            $(".tablesorter").tablesorter();
        },
    })
}

let write_html = function(data,html){
    if (!data["note"]){
        data["note"] = ""
    }
    html += '<tr> \
                <td data-th="Cust Model No">' + data["cust_model"] + '</td> \
                <td data-th="Project Name">' + data["project_name"] + '</td> \
                <td data-th="Model Description">' + data["description"] + '</td> \
                <td data-th="Note">' + data["note"] + '</td> \
            </tr>'
    return html
}

addLoadEvent(InitLoadFunction);