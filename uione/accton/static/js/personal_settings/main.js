window.onload = function() {
    var src = document.getElementById("src");
    var target = document.getElementById("target");
    showImage(src,target);
    getInformationByUser();
    getPersonalPicture();
    editBtnClick();
    leaveAlert();
}

var changeEvent = 'False'

function showImage(src,target) {
    var fr = new FileReader();
    // when image is loaded, set the src of the image where you want to display it
    fr.onload = function(e) { 
        target.src = this.result; 
    };
    src.addEventListener("change",function() {
        // fill fr with image data    
        fr.readAsDataURL(src.files[0]);
        $("#uploadPicture").attr("style","display:none")
        $("#savePicture").attr("style","display:block")
        changeEvent = "True";
        leaveAlert();
    });
}

var first_name = ''
var last_name = ''
let getInformationByUser = function(){
    $.ajax({
        type:'get',
        url:'http://' + Config.ip_address + Config.port + '/personal_settings/getInfoByUser/',
        dataType:'json',
        success:function(data){
            data = data["data"]
            $("#user_name").empty()
            $("#user_name").append(data[0]["username"])
            $("#first_name").val(data[0]["first_name"])
            first_name = data[0]["first_name"]
            last_name = data[0]["last_name"]
            $("#email").empty()
            $("#email").append(data[0]["email"])
            $("#user_type").empty()
            $("#user_type").append(data[0]["user_type"])
            $("#last_name").val(data[0]["last_name"])
        },
        error:function(status){
            console.log(status)
            console.log(data[0])
        }
    })
}

let uploadPersonalPicture = function(){
    $("#uploadpicturebtn").click(function(){
        img = $("#target").attr("src")
        $.ajax({
            type:'post',
            url:'http://' + Config.ip_address + Config.port + '/personal_settings/save/personal_picture/',
            data:{img:img},
            dataType:'json',
            success:function(){
                window.onbeforeunload = false
                location.href = 'http://' + Config.ip_address + Config.port + '/personal_settings/'
            }
        })
    })
}

let cancelUploadPicture = function(){
    $("#canceluploadbtn").click(function(){
        $("#target").attr("src",defaultPicture)
        $("#savePicture").attr("style","display:none")
        $("#uploadPicture").attr("style","display:bolck")
        changeEvent = "Flase";
        leaveAlert();
    })
}

var defaultPicture = "";
let getPersonalPicture = function(){
    $("#target").attr("src","")
    $.ajax({
        type:'get',
        url:'http://' + Config.ip_address + Config.port + '/personal_settings/get/personal_picture/',
        dataType:'json',
        success:function(data){
            data = data["data"]
            if(data.length > 0){
                $("#target").attr("src","")
                element = JSON.parse(data)
                defaultPicture = element["img"]
                $("#target").attr("src",element["img"])
            }
            else{
                defaultPicture = "/static/images/tms_default.svg"
                $("#target").attr("src","/static/images/tms_default.svg")
            }
            uploadPersonalPicture()
            cancelUploadPicture()
        }
    })
}

let editBtnClick = function(){
    $(".editValue").click(function(){
        $(this).prev().removeAttr("disabled");
        $(this).prev().val("");
        $(this).prev().attr("placeholder","Please input new content...")
        $(this).prev().attr("style","border-color: #2685C7;border-style:solid;border-width:0.5px;")
        saveBTN = '<a class="col-xs-2" style="color:white;padding-left:8px"><button type="button" class="btn btn-primary button-text" style="margin-left:8px">Save</button></a>'
        cancelBTN = '<a class="col-xs-2 cancelbtn"><button type="button" class="btn btn-default button-text" style="border:none;color:#2685C7">Cancel</button></a>'
        $(this).parent().append(saveBTN)
        $(this).parent().append(cancelBTN)
        $(this).remove()
        cancelBtnClick()
        saveBtnClick()
        changeEvent = "True";
        leaveAlert();
    })
}

let cancelBtnClick = function(){
    $(".cancelbtn").click(function(){
        editBTN = '<a class="col-xs-2 editValue">Edit</a>'
        $(this).prev().prev().attr("disabled","")
        $(this).prev().prev().attr("style","")
        $(this).prev().remove()
        $(this).prev().attr("placeholder","")
        $(this).parent().append(editBTN)
        $(this).remove()
        $("#first_name").val(first_name)
        $("#last_name").val(last_name)
        editBtnClick();
        changeEvent = "False";
    })
}

let saveBtnClick = function(){
    $(".saveValue").click(function(){
        type=$(this).prev().attr("id")
        content=$(this).prev().val()
        $.ajax({
            type:'post',
            url: 'http://' + Config.ip_address + Config.port + '/personal_settings/save/changeDB/',
            data:{type:type,content:content},
            dataType:'json',
            success:function(){
                window.onbeforeunload = false
                location.href = 'http://' + Config.ip_address + Config.port + '/personal_settings/'
            }
        })
    })
}

let leaveAlert = function(){
    if (changeEvent == "True"){
        window.onbeforeunload = function() {
            return "Are you sure to leave page? Data will not be saved if you didn't save.";
        } 
    }
}