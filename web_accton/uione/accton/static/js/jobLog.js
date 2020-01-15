let statusLoad = function() {
    getTestLog();
    // setFunctionInterval();
}
// let setFunctionInterval = function(){
//     get_test_log_id = setInterval(getTestLog, 1000);
// }
let logList = []
let download_html = ""
let getTestLog = function(){
    $.ajax({
        type: "get",
        url: "http://"+ Config.ip_address + Config.port + "/test/jobDetail/testLog/",
        data:{job_id: getUrlParameter("jobId"),test_id: getUrlParameter("testId")},
        dataType: "json",
        success: function(data, status){
            $("#test_name").text(data["test_name"]);
            $("#log").empty();
            logList = data["log"]
            html = ""
            for(var i = 0; i < logList.length;i++)
            {
                download_html += logList[i] + '\r\n'
                html += "<div>" + logList[i] +" "+ "</div>"
            }
            $("#log").append(html);
        },
    })
}

let downloadLog = function(){
    var link = document.createElement('a');
    link.download = "log.txt";
    // Construct the uri
    var uri = 'data:text;charset=utf-8,' + encodeURIComponent(download_html)
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    // Cleanup the DOM
    document.body.removeChild(link);
}
addLoadEvent(statusLoad);
