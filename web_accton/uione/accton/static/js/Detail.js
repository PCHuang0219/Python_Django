let onloadfunction = function(){
    $('#status_button').click(function(){
        location.href = document.referrer;
    });
    getJobStatus();
    setInterval(getJobStatus, 1000);
}

let getJobStatus = function(){
    let job_id = localStorage.getItem("jobId");
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/test/detail/testTableInJob/",
        data:{job_id: job_id},
        dataType: "json",
        success: function(data, status){
            data = data['testTable']
        $(".table tbody").empty();
        let html = ""
        for(var i = 0; i < data.length;i++)
        {
            element = data[i]
            // if ( element["test_topo"] == "vms-t0"){
            //     element["test_topo"] = "T0";
            // }
            // else if (element["test_topo"] == "vms-t1"){
            //     element["test_topo"] = "T1";
            // }
            // else if (element["test_topo"] == "ptf1-32"){
            //     element["test_topo"] = "PTF32";
            // }
            // else if (element["test_topo"] == "vms-t1-lag"){
            //     element["test_topo"] = "T1-LAG"
            // }
            html +=  
            "<tr>" +
            "<td data-th='#'>"+ parseInt(i+1) + "</th>" +
            "<td data-th='Test Name'>" + element["test_name"] + "</td>" +
            "<td data-th='TOPO'>" + element["test_topo"] + "</td>" +
            "<td data-th='Status'>" + element["test_status"] + "</td>" +
            "<td data-th='Result'>" + element["test_result"] + "</td>" +
            "<td data-th='Start Time'>" + element["test_start_time"] + "</td>" +
            "<td data-th='End Time'>" + element["test_end_time"] + "</td>" 
            if(element["test_status"] != "Finished"){
                html += "<td data-th='Log'><button disabled data-toggle='modal' data-target='#exampleModalLong'>" + "log" + "</button></td>"
            }
            else{
                // html += "<td><button data-toggle='modal' data-target='#exampleModalLong'>" + "log" + "</button></td>"
                html += "<td data-th='Log'><button data-toggle='modal' data-target='#exampleModalLong'>" + "log" + "</button></td>"
            }
            "</tr>"
        }
        $(".table tbody").append(html);
        $("button").click(function(){
            test_id = $($(this).parent().parent().children()[0]).text();
            test_id = test_id - 1;
            localStorage.setItem("testId",test_id);
            localStorage.setItem("jobId",job_id);
            location.href = "http://" + Config.ip_address + Config.port + "/test/jobLog"
        });
        },
    })
}

let getLog = function(job_id,test_name){
    $.ajax({
        type: "post",
        url: "http://"+ Config.ip_address + Config.port + "/test/jobDetail/testLog/",
        data:{job_id: job_id,test_string: test_name},
        dataType: "json",
        success: function(data, status){
            let html = ""
            data = data['log']
            for(var i = 0; i < data.length;i++)
            {
                html += '<div>'+data[i]+'</div>';   
            }
            $("#log_content").empty();
            $("#log_content").append(html);
        },
    })
}
addLoadEvent(onloadfunction);

