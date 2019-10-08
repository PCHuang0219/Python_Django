let download_button_click = function(){
    $("#201903_performanceBtn").click(function(){
        $.ajax({
            type: "get",
            url: "http://"+ Config.ip_address + Config.port + "/sonic/downloads/getAcctonSonicImage/",
            data:{},
            dataType: "json",
            success: function(data){
                if (typeof data == "string"){
                    return alert("You are not authorized to download this version. Click learn more for detail.");
                }
            data = data["data"];
            image_list = data;
            let version = '';
            radio_list = $("#201903_version").children() ;
            for (var i = 0 ; i < radio_list.length; i++){
                if (radio_list[i].checked){
                    version = radio_list[i].value;
                }
            }
            for (var i = 0 ; i < image_list.length ; i++ ){
                if ((image_list[i][1] == "201903") && (image_list[i][2] == version)){
                    location.href = image_list[i][3];
                }
            }
            if ( version ==''){alert("Please Choose Version");}
            },
        })
    })

    $("#201811_performanceBtn").click(function(){
        $.ajax({
            type: "get",
            url: "http://"+ Config.ip_address + Config.port + "/sonic/downloads/getAcctonSonicImage/",
            data:{},
            dataType: "json",
            success: function(data){
                if (typeof data == "string"){
                    return alert("You are not authorized to download this version. Click learn more for detail.");
                }
            data = data["data"];
            image_list = data;
            let version = '';
            radio_list = $("#201811_version").children() ;
            for (var i = 0 ; i < radio_list.length; i++){
                if (radio_list[i].checked){
                    version = radio_list[i].value;
                }
            }
            for (var i = 0 ; i < image_list.length ; i++ ){
                if ((image_list[i][1] == "201811") && (image_list[i][2] == version)){
                    location.href = image_list[i][3];
                }
            }
            if ( version ==''){alert("Please Choose Version");}
            },
        })
    })
    $("#201807_performanceBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
    $("#201803_performanceBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
    $("#201803_communityBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
    $("#201807_communityBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
    $("#201811_communityBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
    $("#201903_communityBtn").click(function(){
        location.href = 'http://210.63.221.19:8888/SONiC/Community/sonic-broadcom.bin';
    })
}

let getImageList = function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/downloads/getSonicImageVersionData/",
        data:{},
        dataType: "json",
        success: function(data){
            data = data["data"];
            image_list = data;
            changeVersionViews(image_list);
        },
    })
}

let addGithubBuild = function(data_list){
    var html='<h4 class="performance_source">Github Build</h4>';
    for (var i=0 ; i < 2 ; i++) {
        html+='<input name="build_version" type="radio" value="'+data_list[i][2]+'"> \
                <i>Newest_Build&nbsp;&nbsp;&nbsp;06/12/2019</i> \
                <i class="fa fa-file-code-o"></i> \
                <i class="fa fa-tasks">  feature_list</i><br>';
    }
    return html ;
}

let addAcctonBuild = function(data_list){
    var html='<h4 class="performance_source">Accton Performance Build</h4>';
    for (var i=0 ; i < 3 ; i++) {
        html+='<input name="build_version" type="radio" value="'+data_list[i][2]+'"> \
                <i>Newest_Build&nbsp;&nbsp;&nbsp;06/12/2019</i> \
                <i class="fa fa-file-code-o"></i> \
                <i class="fa fa-tasks">  feature_list</i><br>';
    }
    return html ;
}

let changeVersionViews = function(data_list){
    let html_201903 = '';
    let html_201811 = '';
    var x=0 ;
    var y=0 ;
    var array_201903 = new Array();
    var array_201811 = new Array();
    for(let i = 0; i < data_list.length; i++){
        if ( data_list[i][1] == "201903"){
            array_201903[x]=data_list[i];
            x++;
        }
        if ( data_list[i][1] == "201811"){
            array_201811[y]=data_list[i];
            y++;
        }
    }
    html_201903 += addGithubBuild(array_201903);
    html_201903 += addAcctonBuild(array_201903);
    html_201811 += addGithubBuild(array_201811);
    html_201811 += addAcctonBuild(array_201811);
    $("#201903_version").empty();
    $("#201903_version").append(html_201903);
    $("#201811_version").empty();
    $("#201811_version").append(html_201811);
    download_button_click(data_list);
}

addLoadEvent(getImageList);