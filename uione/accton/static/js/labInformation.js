const local_url = window.location.origin
let createIXIAInformation = function(){
    $("#createIXIAInformation").click(function(){
        var Lab = $("#createLocation").val()
        var model = $("#createModel").val()
        var port_number = 'Port ' + $("#createPortNumber").val()
        var status = "Available Now"
        var ToRack = $("#createToRack").val() + ' U'
        var ToDevice = $("#createToDevice").val()
        var owner = $("#createOwner").val()
        var description = "NULL"
        if ( Lab=="" | model=="" | port_number=="" | ToRack=="" | ToDevice=="" | owner==""){
            alert("")
            createIXIAInformation()
        }
        else{
            $.ajax({
                type: "post",
                url: local_url + "/test/save/IXIAInformation/",
                data:{Lab:Lab,
                    model:model,
                    port_number:port_number,
                    status:status,
                    ToRack:ToRack,
                    ToDevice:ToDevice,
                    owner:owner,
                    description:description,},
                dataType: "json",
                success: function(data, status){
                    if ( status == "success"){
                        location.href = local_url + "/test/labInformation"
                    }
                    else{
                        alert("Create ERROR!")
                    }
                },
            })}
        })
}

let showIXIAInformation = function(){
    $.ajax({
        type: "get",
        url: local_url + "/test/save/getIXIAInformation/",
        data:{},
        dataType: "json",
        success: function(data, status){
            var taipei_html = ''
            var hsinchu_html = ''
            var taichung_html = ''
            var tainan_html = ''
            data_list = data["IXIA_Info"]
            data_list.forEach(element => {
                element = JSON.parse(element)
                if ( element["location"] == "Tainan" ){
                    tainan_html += addHTMLCode("'tainan'",element)
                }
                else if ( element["location"] == "Hsinchu" ){
                    hsinchu_html += addHTMLCode("'hsinchu'",element)
                }
                else if ( element["location"] == "Taichung" ){
                    taichung_html += addHTMLCode("'taichung'",element)
                }
                else if ( element["location"] == "Taipei" ){
                    taipei_html += addHTMLCode("'taipei'",element)
                }
            });
            $(".Table tbody").empty();
            $(".Table tbody").append(taipei_html);
            $(".Table tbody").append(hsinchu_html);
            $(".Table tbody").append(taichung_html);
            $(".Table tbody").append(tainan_html);
            },
    })
}

let addHTMLCode = function(lab,element){
    html = '<tr> \
				<td class='+lab+'data-th="Location">'+element["location"]+'</td> \
				<td class='+lab+'data-th="IXIA Model">'+element["model"]+'</td> \
			    <td class='+lab+'data-th="Port Number">'+element["port_number"]+'</td> \
				<td class='+lab+'data-th="Status">'+element["status"]+'</td> \
				<td class='+lab+'data-th="Connect to Rack">'+element["ToRack"]+'</td> \
				<td class='+lab+'data-th="Connect to Device">'+element["ToDevice"]+'</td> \
			    <td class='+lab+'data-th="Start Time">'+element["start_time"]+'</td> \
				<td class='+lab+'data-th="End Time">'+element["end_time"]+'</td> \
				<td class='+lab+'data-th="Owner">'+element["owner"]+'</td> \
                <td class='+lab+'data-th="Description">'+element["description"]+'</td></tr>'
    return html
}

let updateIXIAInformation = function(){
    $("#updateIXIAInfo").click(function(){
        var Lab = $("#location").val()
        var model = $("#model").val()
        var port_number = $("#portNumber").val()
        var status = $("#status").val()
        var ToRack = $("#toRack").val()
        var ToDevice = $("#toDevice").val()
        var owner = $("#owner").val()
        var description = $("#description").val()
        $.post( local_url + "/test/save/updateIXIAInformation/",{
            Lab:Lab,
            model:model,
            port_number:port_number,
            status:status,
            ToRack:ToRack,
            ToDevice:ToDevice,
            owner:owner,
            description:description,
        },function(data,status){
            if ( status == "success"){
                location.href = local_url + "/test/labInformation"
            }
            else{
                alert("Update ERROR!")
            }
        })
    })
}

let getChangeView = function(this_event="location"){
    var model = $("#model").val()
    var port_number = $("#portNumber").val()
    if ( this_event == "location" ){
        var model = ''
        var port_number = ''
    }
    var Lab = $("#location").val()
    $.get( local_url + "/test/save/updateIXIAChangeView/",{
        Lab:Lab,
        model:model,
        port_number:port_number,
    },function(data,status){
        data = data["data"]
        if ( this_event == "model" ){
            updateChangeView("Model",data)
        }
        else if ( this_event == "location" ){
            updateChangeView("Location",data)
        }
        })
}

let updateChangeView = function(condition,data){
    model_html = '';
    port_number = '';
    data.forEach(element => {
        element = JSON.parse(element)
        model_html += '<option>'+element["model"]+'</option>'
        port_number += '<option>'+element["port_number"]+'</option>'
    })
    if ( condition == "Location"){
        $("#model").empty();
        $("#model").append(model_html);
        $("#portNumber").empty();
        $("#portNumber").append(port_number);
    }
    else if ( condition == "Model"){
        $("#portNumber").empty();
        $("#portNumber").append(port_number);
    }
}

let card = ''
let statusClick = function(){
    $("td").click(function(){
        card = $(this).parent().parent().parent().siblings(":first").text();
        port = $(this).siblings(":first").text();
        date = $(this).attr("data-th")
        status = $(this).text();
        if ( status != "Null"){
            alert("Can not reserve Date: "+date)
        }
        else if ( date != "Port / Speed" ){
            $("#modal").attr("style","display:block");
            showModal(port,date)
            closeModal();
        }
    })
}

let closeModal = function(){
    $(".close").click(function(){
        $(".modal").attr("style","display:none");
    })
}

let showModal = function(port,date){
    $("#portNumber").empty();
    $("#portNumber").append(port);
    $("#startTime").empty();
    $("#startTime").append(date);
}

let createSchedule = function(){
    $("#createSchedule").click(function(){
        port = $("#portNumber").text();
        start_time = $("#startTime").text();
        end_time = $("#endTime").val();
        cable = $("#cable").val();
        toDevice = $("#toDevice").val();
        speed = port.split("/ ")[1];
        cable_speed = cable.split(" ")[0];
        endTime = new Date( end_time.split("-")[0] , end_time.split("-")[1] , end_time.split("-")[2])
        startTime = new Date( start_time.split("-")[0] , start_time.split("-")[1] , start_time.split("-")[2])
        if (startTime.valueOf() > endTime.valueOf() ){
            alert("Can not choose the day before "+start_time)
            return
        }
        if ( end_time.length == 0 ){
            alert("End Time can not be empty.")
            return
        }
        if ( speed != cable_speed ){
            alert("Can not match the cable with IXIA port.")
            return
        }
        else{
            $.post( local_url + "/test/save/ixiaSchedule/",{
                card:card,
                port:port,
                start_time:start_time,
                end_time:end_time,
                cable:cable,
                toDevice:toDevice,
            },function(data,status){
                data = data["data"]
                if ( data == "Failed" ){
                    alert("Create Error !")
                }
                else{
                    location.href = local_url + "/test/labInformation"
                }
            })
        }
    })
}
let first_date = ''
let getWeekDate = function(){
    var week_list = []
    $.get( local_url + "/test/get/weekDate/",{
    },function(data,status){
        data = data["data"]
        first_date = data[0][0]
        data.forEach(week =>{
            week.forEach(day =>{
                week_list.push(day)
            })
        })
        trTitle_html = '<th style="text-align:center">Port / Speed</th>'
        trTitle_html = writeTrTitle(trTitle_html,week_list)
        $(".tr-only-hide").empty()
        $(".tr-only-hide").append(trTitle_html)
        getIXIAStatus(week_list)
    })
}

let writeTrTitle = function(html,week){
    week.forEach(data => {
        data = data.split("-")[1] + '/' + data.split("-")[2]
        html += '<th style="text-align:center">'+data+'</th>'
    })
    return html
}

let getIXIAStatus = function(week){
    $.get( local_url + "/test/get/ixiaSchedule/",{
    },function(data,status){
        data = data["data"]
        showIXIASchedule(week,data)
    })
}

let showIXIASchedule = function(week,reserveData){
    i = 0
    card = ["Card #1","Card #2"]
    port = {"Card #1": ["Port1 / 100G","Port2 / 100G","Port3 / 100G","Port4 / 100G"],"Card #2": ["Port1 / 100G","Port2 / 100G","Port3 / 100G","Port4 / 100G"]}
    card.forEach(card_data =>{
        i += 1
        td_html = ''
        port[card_data].forEach(port_number =>{
            id = "card"+String(i)+port_number.split(" ")[0]
            td_html += writeTdHTML(id,port_number,week,td_html)
        })
        selection = "#card"+ String(i)
        $(selection).empty()
        $(selection).append(td_html)
    })
    updateIXIAReservation(reserveData)
    statusClick()
}

let updateIXIAReservation = function(reserveData){
    reserveData.forEach(reservation =>{
        owner = reservation["owner"]
        card_data = reservation["card"]
        port_number = reservation["port"]
        start_time = reservation["start_time"].split(" ")[0]
        end_time = reservation["end_time"].split(" ")[0]
        if ( card_data == "Card #1"){ id = "card1"}
        if ( card_data == "Card #2"){ id = "card2"}
        if ( start_time == end_time ){
            id = id + port_number.split(" ")[0] + start_time
            id = "#" + id
            $(id).empty();
            $(id).append(owner);
        }
        else{
            start_id = id + port_number.split(" ")[0] + start_time
            end_id =  id + port_number.split(" ")[0] + end_time
            select_id = "#" + start_id
            select_end_id = "#" + end_id
            if ( document.getElementById(start_id) ){
                next_id = $(select_id).next().attr("id")
                $(select_id).empty()
                $(select_id).append(owner);
                count = $(select_id).nextUntil($(select_end_id)).length
            }
            else{
                first_id = id + port_number.split(" ")[0] + first_date
                select_id = "#" + first_id
                $(select_id).empty()
                $(select_id).append(owner);
                if (select_id == select_end_id){
                    count = -1
                }
                else{
                    count = $(select_id).nextUntil($(select_end_id)).length
                }
            }
            for ( i = -1 ; i < count ; i++ ){
                next_id = $(select_id).next().attr("id")
                select_id = "#" + next_id
                $(select_id).empty();
                $(select_id).append(owner);
            }
        }
    })
}

let writeTdHTML = function(id,port_number,week,td_html){
    td_html = '<tr><td data-th="Port / Speed">'+port_number+'</td>'
    week.forEach(date =>{
        select_id = id + date
        td_html += '<td id="'+ select_id +'" data-th="'+date+'">Null</td>'
    })
    td_html += '</tr>'
    return td_html
}

let showIXIAConfig = function(){
    $("#showConfig").click(function(){
        $("#IXIAconfig").attr("style","display:block")
        closeModal();
    })
}

let updateIXIAConfig = function(){
    $.get( local_url + "/test/get/updateIXIAConfig/",{
    },function(data,status){
        data = data["data"]
        today = data.pop()
        $("#startTime_config").empty();
        $("#startTime_config").append(today);
        html = ''  
        data.forEach(element =>{
            element = JSON.parse(element)
            console.log(element)
            html += element["toDevice"]
        })
    })
}

addLoadEvent(createSchedule);
addLoadEvent(getWeekDate);
addLoadEvent(showIXIAConfig);
addLoadEvent(updateIXIAConfig);

// addLoadEvent(createIXIAInformation);
// addLoadEvent(showIXIAInformation);
// addLoadEvent(updateIXIAInformation);
// addLoadEvent(getChangeView);
