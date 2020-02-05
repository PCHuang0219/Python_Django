let initLoadFunction = function(){
    getEPRList();
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

let getEPRList = function(){
    $.ajax({
        type:'get',
        data:{},
        dataType:'json',
        url: window.location.origin + "/project_management/get/EPRList/",
        success:function(data){
            data = data["data"]
            html = ''
            for ( var i=data.length-1 ; i >= 0 ; i--){
                element = JSON.parse(data[i])
                html = writeEPRListHtml(element,html)
            }
            $("#EPR_list").empty()
            $("#EPR_list").append(html)
            $(".tablesorter").tablesorter();
            jumpDetailPage();
        }
    })
}

let writeEPRListHtml = function(data,html){
    if(data["status"] == "Submitted"){
        data["status"] = '<td data-th="Status"><button class="btn btn-primary eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Verified"){
        data["status"] = '<td data-th="Status"><button class="btn btn-secondary eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Verified"){
        data["status"] = '<td data-th="Status"><button class="btn btn-secondary eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Assigned"){
        data["status"] = '<td data-th="Status"><button class="btn btn-info eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Closed"){
        data["status"] = '<td data-th="Status"><button class="btn btn-dark eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Cancelled"){
        data["status"] = '<td data-th="Status"><button class="btn btn-warning eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    else if(data["status"] == "Resloved"){
        data["status"] = '<td data-th="Status"><button class="btn btn-success eprstatus" type="button" data-target="#changeStatus" data-toggle="modal">' + data["status"] + '</button></td>'
    }
    html += '<tr> \
                <td data-th="Project">' + data["project"] + '</td> \
                <td data-th="EPR_ID">' + data["EPR_ID"] + '</td> \
                <td data-th="Headline">' + data["headline"] + '</td> \
                <td data-th="Submit Time">' + data["submit_time"] + '</td>' + data["status"] + ' \
                <td data-th="Submitter">' + data["user"] + '</td>  \
                <td data-th="Detail"><button class="btn btn-link detailButton" type="button" style="width:50px">detail</button></td> \
            </tr>'
    return html
}

let jumpDetailPage = function(){
    $(".detailButton").click(function(){
        EPR_ID = $(this).parent().siblings(":first").next().text()
        localStorage.setItem("EPR_ID",EPR_ID);
        location.href = window.location.origin + '/project_management/EPRList/EPR_detail'
    })
}

addLoadEvent(initLoadFunction)