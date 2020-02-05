let InitLoadFunction = function(){
    showDeviceList();
    createDeivceList();
    getDeviceList();
    changeDeivceList();
}

let getDeviceList = function(){
    $.ajax({
        type:'get',
        dataType:'json',
        url: window.location.origin + "/test/get/deviceList/",
        success:function(data){
            data = data["data"]
            taipeiRack1_html = ''
            hsinchuRack1_html = ''
            hsinchuRack2_html = ''
            hsinchuRack3_html = ''
            tainanRack1_html = ''
            tainanRack2_html = ''
            tainanRack3_html = ''
            for (var i=0 ; i< data.length ; i++){
                if (data[i]["rack"] == "taipeiRack1"){
                    taipeiRack1_html = write_html(taipeiRack1_html,data[i])
                }
                else if (data[i]["rack"] == "hsinchuRack1"){
                    hsinchuRack1_html = write_html(hsinchuRack1_html,data[i])
                }
                else if (data[i]["rack"] == "hsinchuRack2"){
                    hsinchuRack2_html = write_html(hsinchuRack2_html,data[i])
                }
                else if (data[i]["rack"] == "hsinchuRack3"){
                    hsinchuRack3_html = write_html(hsinchuRack3_html,data[i])
                }
                else if (data[i]["rack"] == "tainanRack1"){
                    tainanRack1_html = write_html(tainanRack1_html,data[i])
                }
                else if (data[i]["rack"] == "tainanRack2"){
                    tainanRack2_html = write_html(tainanRack2_html,data[i])
                }
                else if (data[i]["rack"] == "tainanRack3"){
                    tainanRack3_html = write_html(tainanRack3_html,data[i])
                }
            }
            $("#taipeiRack1").empty()
            $("#taipeiRack1").append(taipeiRack1_html)
            $("#hsinchuRack1").empty()
            $("#hsinchuRack1").append(hsinchuRack1_html)
            $("#hsinchuRack2").empty()
            $("#hsinchuRack2").append(hsinchuRack2_html)
            $("#hsinchuRack3").empty()
            $("#hsinchuRack3").append(hsinchuRack3_html)
            $("#tainanRack1").empty()
            $("#tainanRack1").append(tainanRack1_html)
            $("#tainanRack2").empty()
            $("#tainanRack2").append(tainanRack2_html)
            $("#tainanRack3").empty()
            $("#tainanRack3").append(tainanRack3_html)
            $(".tablesorter").tablesorter();
        }
    })
}

let write_html = function(html,data){
    html += '<tr> \
                <td data-th="Location">' + data["location"] + '</td> \
                <td data-th="Model">' + data["model"] + '</td> \
                <td data-th="Platform">' + data["platform"] + '</td> \
                <td data-th="Console">' + data["console"] + '</td> \
                <td data-th="PDU">' + data["PDU"] + '</td> \
                <td data-th="Default IP">' + data["IP"] + '</td> \
                <td data-th="User">' + data["user"] + '</td> \
                <td data-th="Power Schedule">' + data["power"] + '</td> \
                <td data-th="Lease Ends at">' + data["status"] + '</td> \
            </tr>'
    return html
}

let createDeivceList = function(){
    $("#createDeviceList").click(function(){
        var rack = $("#rack").val();
        var Dlocation = $("#location").val() + "U";
        var model = $("#model").val();
        var platform = $("#platform").val();
        var console_server = $("#console").val();
        var console_port = $("#port").val();
        var PDU = $("#PDU").val();
        var Pport = $("#Pport").val();
        var IP = $("#IP").val();
        var user = $("#user").val();
        var power = $("#power").val();
        var status = $("#status").val();
        var console_server = console_server + ":" + console_port;
        var PDU = PDU + "#" + Pport;
        if ( PDU == "" | rack == "" | Dlocation == "" | model == "" | platform =="" | console_server == "" | console_port == "" | IP == "" | user == "" | power == "" | status == ""){
            alert("Any cell can't be empty !")
        }
        else{
            $.ajax({
                type: 'post',
                url: window.location.origin + "/test/save/deviceList/",
                data:{rack:rack,
                    location:Dlocation,
                    model:model,
                    platform:platform,
                    console:console_server,
                    IP:IP,
                    PDU:PDU,
                    user:user,
                    power:power,
                    status:status,},
                dataType:'json',
                success:function(data){
                    location.href = window.location.origin + "/test/deviceManagement"
                }
            })
        }
    })
}

let showDeviceList = function(){
    var rack = $("#changeRack").val()
    $.ajax({
        type: 'get',
        url: window.location.origin + "/test/get/deviceListByRack/",
        data:{rack:rack},
        dataType:'json',
        success:function(data){
            data = data["data"]
            $("#deviceChoose").empty()
            html = ''
            for(var i=0 ; i<data.length ; i++){
                html += '<option>' + data[i]["location"] + ' : ' + data[i]["model"] + '</option>'
            }
            $("#deviceChoose").append(html)
        }
    })
    $("#changeRack").click(function(){
        showDeviceList();
    })
}

let changeDeivceList = function(){
    $("#changeDeviceList").click(function(){
        var rack = $("#changeRack").val();
        var Dlocation = $("#deviceChoose").val().split(" ")[0];
        var type = $("#deviceType").val();
        var content = $("#changeContent").val();
        if(type!="PDU"){
            type = type.toLowerCase()
        }
        if(type =="power schedule"){
            type = "power"
        }
        if(type =="default ip"){
            type = "IP"
        }
        // if ( PDU == "" | rack == "" | Dlocation == "" | model == "" | platform =="" | console_server == "" | console_port == "" | IP == "" | user == "" | power == "" | status == ""){
        //     alert("Any cell can't be empty !")
        // }
        // else{
            $.ajax({
                type: 'post',
                url: window.location.origin + "/test/change/deviceList/",
                data:{rack:rack,
                    location:Dlocation,
                    type:type,
                    content:content,},
                dataType:'json',
                success:function(data){
                    location.href = window.location.origin + "/test/deviceManagement"
                }
            })
        // }
    })
}

addLoadEvent(InitLoadFunction);