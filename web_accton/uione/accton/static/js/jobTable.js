let getJobTable = function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/test/management/jobTable/",
        data:{},
        dataType: "json",
        success: function(data, status){
            // console.log(data)
            $(".table tbody").empty();
            let html = ""
            data = data["data"]
            for(var i=0,x=data.length-1 ; x >= 0 ; x--,i++)
            {
                element = JSON.parse(data[x])
                html +=  
                "<tr>" +
                "<td data-th='#'>"+ parseInt(i+1) + "</th>" +
                "<td data-th='Job Name' job_id='" + element["_id"] + "'>" + element["job_name"] + "</td>" +
                "<td data-th='Job Description'>" + element["job_describe"] + "</td>" +
                "<td data-th='Status'>" + element["status"] + "</td>" +
                "<td data-th='Start Time'>" + element["start_time"] + "</td>" +
                "<td data-th='End Time'>" + element["end_time"] + "</td>" +
                "<td data-th='Result'>" + element["result"] + "</td>" +
                "<td data-th='Detail'>" + "<button class='button' id='status_button' type='button'>detail</button>"+"</td>" +
                "</tr>"
            }
            $(".table tbody").append(html);
            $(".button").click(function(){
                localStorage.setItem("jobId",$(this).parent().parent().children().first().next().attr("job_id"));
                // console.log($(this).parent().parent().children().first().next().text());
                location.href = "http://" + Config.ip_address + Config.port + "/test/jobDetail"
            });
        },
    })
}

let updateTable = function(){
    setInterval(getJobTable, 2000);
}

addLoadEvent(getJobTable);