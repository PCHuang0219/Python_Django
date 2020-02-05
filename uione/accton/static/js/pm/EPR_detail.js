let initLoadFunction = function(){
    showEPR_detail();
}

let showEPR_detail = function(){
    EPR_ID = localStorage.getItem("EPR_ID")
    $.ajax({
        type:'get',
        data:{"EPR_ID":EPR_ID},
        dataType:'json',
        url: window.location.origin + "/project_management/get/EPRList/",
        success:function(data){
            data = data["data"]
            html = ''
            for ( var i=data.length-1 ; i >= 0 ; i--){
                element = JSON.parse(data[i])
                write_main_content(element)
            }
        }
    })
}

let caculateFileSize = function(size){
    if (size >= 1024){
        newSize = size / 1024
        newSize = newSize.toFixed(2)
        newSize = newSize.toString() + " KB"
        return newSize
    }
    else {
        newSize = size.toString() + " B"
        return newSize
    }
}

let write_main_content = function(data){
    attachment_html = '<table class="table"> \
                        <thead> \
                            <tr> \
                                <th scope="col">File Name</th> \
                                <th scope="col">File Size</th> \
                                <th scope="col">Description</th> \
                                <th scope="col">Downlaod</th> \
                            </tr> \
                        </thead> \
                        <tbody >'
    for(var i=0 ; i<data["attachments"].length ; i++){
        attachment = data["attachments"][i]
        path = attachment["file_path"].split("share")[1]
        attachment["file_size"] = caculateFileSize(attachment["file_size"])
        attachment_html += '<tr><td class="tableContent">' + attachment["file_name"] + '</td> \
                                <td class="tableContent">' + attachment["file_size"] + '</td> \
                                <td class="tableContent">' + attachment["description"] + '</td> \
                                <td class="tableContent"> \
                                <a href="#" file="'+path+'"><span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span></a></td> </tr>'
    }
    attachment_html += '</tbody>'
    html = '<div class="col-xs-6"> \
                <label class="form-inline">Project : <label style="color:#7700BB">' + data['project'] + '</label></label><br> \
                <label class="form-inline">EPR ID : <label style="color:#7700BB">' + data['EPR_ID'] + '</label></label><br> \
                <label class="form-inline">Status : <label style="color:#7700BB">' + data['status'] + '</label></label><br> \
                <label class="form-inline">Submitter : <label style="color:#7700BB">' + data['user'] + '</label></label><br> \
            </div>'
    $("#EPRDetailTitle").append(html);
    html = '<div class="col-xs-6"> \
                <div class="EPR_title">Headline :  </div>\
                <label style="color:#7700BB">' + data["headline"] + '</label> \
                <div class="EPR_title">Severity : </div>\
                <label style="color:#7700BB">' + data["severity"] + '</label> \
                <div class="EPR_title">CSC : </div>  \
                <label style="color:#7700BB">' + data["CSC"] + '</label> \
                <div class="EPR_title">Reproduce Rate : </div>  \
                <label style="color:#7700BB">' + data["rate"] + '</label> \
            </div> \
            <div class="col-xs-6"> \
                <div class="EPR_title">Test Problem : </div>\
                <label style="color:#7700BB">' + data["problem"] + '</label> \
                <div class="EPR_title">Expected Result : </div>  \
                <label style="color:#7700BB">' + data["expect"] + '</label> \
                <div class="EPR_title">Test Procedure : </div>\
                <label style="color:#7700BB">' + data["procedure"] + '</label> \
            </div> \
            <div class="col-xs-12" style="margin-top:20px"> \
                <div class="EPR_title">Attachments : </div>' + attachment_html +' \
            </div>'
    $("#EPRDetail").empty();
    $("#EPRDetail").append(html);
    downlaodFile();
}

let downlaodFile = function(){
    $(".glyphicon-download-alt").click(function(){
        path = $(this).parent().attr("file")
        location.href = "http://210.63.221.19:8888" + path
    })
}

addLoadEvent(initLoadFunction)