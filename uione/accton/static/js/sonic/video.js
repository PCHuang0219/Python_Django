let dropdown_button_click = function(){
    $("#typeSelect li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $(this).parent().parent().prev().val($(this).text());
    });
    $("#bandwidthSelect li a").click(function(){
        $(this).parent().parent().prev().text($(this).text());
        $(this).parent().parent().prev().val($(this).text());
    });
}

let apply_button_click = function(data_list){
    $("#apply").click(function(){
        var type = $("#typeSelect button").text();
        var bandwidth = $("#bandwidthSelect button").text();
        if ((type=="By Type") || (bandwidth=="By Bandwidth")){
            alert("Please Select Condition");
        }
        updateVideoList(data_list,type,bandwidth);
    })
}

let getSortList = function(data_list) {
    var type_list = new Set();
    data_list.forEach(item => {
        type_list.has(item["type"]) ? item["type"] : type_list.add(item["type"]) ;
    })
    html = showDropdownView(type_list,"type");
    $("#typeSelect").empty();
    $("#typeSelect").append(html);
    var bandwidth_list = new Set();
    data_list.forEach(item => {
        bandwidth_list.has(item["bandwidth"]) ? item["type"] : bandwidth_list.add(item["bandwidth"]) ;
    })
    html = showDropdownView(bandwidth_list,"bandwidth")
    $("#bandwidthSelect").empty();
    $("#bandwidthSelect").append(html);
    dropdown_button_click();
    apply_button_click(data_list);
}

let showDropdownView = function(set,key){
    let data_list = Array.from(set);
    if (key == "type"){
        html = '<button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">By Type<span class="caret"></span></button><ul class="dropdown-menu">';
    }
    else{
        html = '<button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">By Bandwidth<span class="caret"></span></button><ul class="dropdown-menu">';
    }
    data_list.forEach((element) => {
        html += '<li><a role="menuitem" href="#">'+element+'</a></li>';
    })
    html += '<li><a role="menuitem" href="#">Select All</a></li></ul>';
    return html ;
}

let stop_video = function() {
    $("#a").on("hidden.bs.modal",function (){
        var ytid = "#"+$(this).attr("value");
        $(ytid).attr("src",$(ytid).attr("src"));
    });
}

let updateVideoList=function(data_list,type,bandwidth){
    var new_list = new Array();
    var index = 0
    data_list.forEach((element) => {
        if ( type == "Select All" ){
            if ( element["bandwidth"] == bandwidth){
                new_list[index]=element;
                index ++ ;
            }
            else if (bandwidth == "Select All"){return;}
        }
        else if (bandwidth == "Select All"){
            if ( element["type"] == type){
                new_list[index]=element;
                index ++ ;
            }
            else if (type == "Select All"){return;}
    }})
    if (new_list == ''){
        new_list = data_list;
    }
    showVideo(new_list);
}

let showVideo=function(data_list){
    $("#video").empty();
    let html = '';
    for(var i=0 ; i<data_list.length ; i++){
        data_list[i]["video_link"] = data_list[i]["video_link"].replace("watch?v=","/embed/");
        html += '<div class="col-sm-4 col-xs-12"> \
        <img class="u2icon" src="../../../static'+data_list[i]["png"]+'" data-toggle="modal" data-target="#show" style="width:100%"> \
        <div class="modal" id="show" role="dialog" aria-hidden="true" value="youtube"> \
            <div id="window" class="modal-dialog modal-dialog-centered " role="document" style="width:80%"> \
            </div> \
        </div> \
        <div class="col-sm-12 col-xs-12 u2_title">'+data_list[i]["TMS_title"]+'</div> \
    </div>'
    }
    $("#video").append(html);
    showYoutube(data_list);
}

let showYoutube=function(data_list){
    $(".u2icon").click(function(){
        title = $(this).parent().children("div:last-child").text() ;
        for(var i=0 ; i<data_list.length ; i++){
            if ( data_list[i]["TMS_title"] == title ){
                html ='<div class="modal-content"> \
                <div class="modal-header"> \
                    <h3 class="modal-title">'+title+'</h3> \
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"> \
                        <span aria-hidden="true">&times;</span> \
                    </button> \
                </div> \
                <div class="modal-body"> \
                    <div class="embed-responsive embed-responsive-16by9"> \
                        <iframe id="youtube" width="891" height="501" class="embed-responsive-item" src="'+data_list[i]["video_link"]+'" allowfullscreen></iframe> \
                    </div> \
                </div> \
                <div class="modal-footer"> \
                </div>'
                $("#window").empty();
                $("#window").append(html);
                return ;
            }
        }
    })
}

let getVideoList=function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/sonic/data/videoList/",
        data:{},
        dataType: "json",
        success: function(data, status){
            data = data["videoList"];
            videoList = data;
            showVideo(videoList)
            getSortList(videoList);
            showYoutube(videoList);
        },
    })
}

addLoadEvent(stop_video);
addLoadEvent(getVideoList);