let initLoadFunction = function(){
    showEPR_detail();
}

let showEPR_detail = function(){
    Task_ID = localStorage.getItem("Task_ID")
    $.ajax({
        type:'get',
        data:{"Task_ID":Task_ID},
        dataType:'json',
        url: window.location.origin + "/project_management/get/tasksDtail/",
        success:function(data){
            data = data["data"]
            html = ''
            element = JSON.parse(data[0])
            write_main_content(element)
        }
    })
}

let write_main_content = function(data){
    html = '<div class="col-xs-6"> \
                <label class="form-inline">Project : <label style="color:#7700BB">' + data['project'] + '</label></label><br> \
                <label class="form-inline">TRR ID : <label style="color:#7700BB">' + data['TRR_ID'] + '</label></label><br> \
                <label class="form-inline">Task ID : <label style="color:#7700BB">' + data['Task_ID'] + '</label></label><br> \
                <label class="form-inline">Status : <label style="color:#7700BB">' + data['status'] + '</label></label><br> \
                <label class="form-inline">Owner : <label style="color:#7700BB">' + data['owner'] + '</label></label><br> \
                <label class="form-inline">Submitted Time : <label style="color:#7700BB">' + data['submit_time'] + '</label></label><br> \
            </div>'
    TD_count = data["TD"].split(",").length-1;
    TC_count = data["TC"].split(",").length;
    TD_html = ""
    TC_html = ""
    if (TD_count == 0){
        TD_html += data["TD"]
    }
    else{
        for (var i=0 ; i < TD_count ; i++){
            TD_html += data["TD"].split(",")[i]
        }
    }
    if (TC_count == 0){
        TC_html += data["TC"]
    }
    else{
        for (var i=0 ; i < TC_count ; i++){
            TC_html += data["TC"].split(",")[i]
        }
    }
    console.log(TC_html)
    $("#TaskDetailTitle").append(html);
}

addLoadEvent(initLoadFunction)