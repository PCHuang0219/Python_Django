let project = localStorage.getItem("project"); // TRR Project Name
    let user = localStorage.getItem("user"); // Username
let initLoadFunction = function(){
    getUploadFileData();
    saveEPR();
    writeTheTitle();
}

var fileList = []
var formFile = new FormData()
var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
formFile.append("csrfmiddlewaretoken",csrf)
formFile.append("project",project)

let writeTheTitle = function(){
    html = '<label class="form-inline">Submitter : <label style="color:#7700BB">' + user + '</label></label><br> \
            <label class="form-inline">Project : <label style="color:#7700BB">' + project + '</label></label><br>'
    $("#summary_area").append(html)
}

let getUploadFileData = function(){
    const fileUploader = document.querySelector('#file');
    fileUploader.addEventListener('change', (e) => {
        file_info = e.target.files
    });
    $("#createAttachment").click(function(){
        description = $("#description").val()
        html = "<tr>"
        size = caculateFileSize(file_info[0]["size"])
        file_name = file_info[0]["name"]
        html += '<td class="tableContent">' + file_name + "</td>"
        html += '<td class="tableContent">' + size + "</td>"
        html += '<td class="tableContent">' + description + "</td></tr>"
        $("#attachmentSummary").append(html)
        var fileObj = document.getElementById("file").files[0];
        fileObj.value = description
        fileList.push(description)
        formFile.append(description,fileObj)

        initModal()
    })
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

let saveEPR = function(){
    $("#saveEPR").click(function(){
        headline = $("#headline").val()
        severity = $("#severity").val()
        CSC = $("#CSC").val()
        rate = $("#numerator").val() + "/" + $("#denominator").val()
        problem = $("#testProblem").val()
        expect = $("#expectedResult").val()
        procedure = $("#testProcedure").val()
        if (headline == "" || problem == "" || expect == "" || procedure == ""){
            alert("Please confirm your data is complete")
        }
        else{
            EPR_content = {"headline":headline,"severity":severity,"CSC":CSC,"rate":rate,
            "problem":problem,"expect":expect,"procedure":procedure,
            "user":user,"project":project}
            console.log(fileList)
            formFile.append("fileList",fileList)
            $.ajax({
                type:'POST',
                url:'http://' + Config.ip_address + Config.port + '/project_management/save/EPRAttachment/',
                data:formFile,
                dataType:'json',
                processData: false,//用于对data参数进行序列化处理 这里必须false
                contentType: false,//必须
                success:function(data){
                    EPR_ID = data["data"]
                    EPR_content.EPR_ID = EPR_ID
                    $.ajax({
                        type:'POST',
                        url:'http://' + Config.ip_address + Config.port + '/project_management/save/EPRContent/',
                        data:EPR_content,
                        dataType:'json',
                        success:function(data){
                            location.href = 'http://' + Config.ip_address + Config.port + '/project_management/EPRList'
                        }
                    })
                } 
            })
        }
    })
}

addLoadEvent(initLoadFunction)