let initLoadFunction = function(){
    getTasksList();
}

let initModal = function(){
    $("#addAttachment").modal('hide')
    $("#attachmentContent").empty()
    html = 'Description<span class="red">*</span>： \
            <input id="description" style="width:30%;">  \
            <input type="file" id="file">'
    $("#attachmentContent").append(html)
    const fileUploader = document.querySelector('#file');
    fileUploader.addEventListener('change', (e) => {
        file_info = e.target.files
    })
}

let getTasksList = function(){
    $.ajax({
        type:'get',
        data:{},
        dataType:'json',
        url: "http://" + Config.ip_address + Config.port + "/project_management/get/tasksList/",
        success:function(data){
            data = data["data"]
            html = ''
            for ( var i=data.length-1 ; i >= 0 ; i--){
                element = JSON.parse(data[i])
                html = writeEPRListHtml(element,html)
            }
            $("#tasks_list").empty()
            $("#tasks_list").append(html)
            $(".tablesorter").tablesorter();
            jumpDetailPage();
        }
    })
}

let writeEPRListHtml = function(data,html){
    html += '<tr> \
                <td data-th="Task_ID">' + data["Task_ID"] + '</td> \
                <td data-th="status">' + data["status"] + '</td> \
                <td data-th="M.E.D.F">' + data["MEDF"] + '</td> \
                <td data-th="Submit Time">' + data["submit_time"] + '</td> \
                <td data-th="Owner">' + data["owner"] + '</td>  \
                <td data-th="Detail"><button class="btn btn-link detailButton" type="button" style="width:50px">detail</button></td> \
            </tr>'
    return html
}

let jumpDetailPage = function(){
    $(".detailButton").click(function(){
        Task_ID = $(this).parent().siblings(":first").text()
        localStorage.setItem("Task_ID",Task_ID);
        location.href = 'http://' + Config.ip_address + Config.port + '/project_management/NTC_tasks/task_detail'
    })
}

addLoadEvent(initLoadFunction)