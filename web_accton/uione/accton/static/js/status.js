let statusLoad = function() {
    // console.log(localStorage.getItem("jobId"))
    $("#ok_button").click(function(){
        location.href = document.referrer;
    });
    $("#finish_button").click(function(){
        location.href = "http://" + Config.ip_address + Config.port +"/test/jobLog";
    });
    $("#select_job_button").click(function(){
        getRunningJobList();
    });
    chooseJobId();
    getConfigure();
    getRunningTestName();
    getJobStatus();
    getJobProgress();
    getTestLog();
    getJobExecuteTime();
    checkJobId();
    setFunctionInterval();
}
let conf_id;
let run_test_name_id;
let job_status_id;
let job_progress_id;
let get_test_log_id;
let job_execure_time_id;
let job_status;

window.onunload = function() {
    localStorage.setItem("jobId","");
    localStorage.setItem("platform","");
}

let chooseJobId = function() {
    $("#dropdown-job-list li").click(function(){
        let job_id = $(this).text().split('(')[1].split(')')[0]
        localStorage.setItem("jobId",job_id);
        $.ajax({
            type:"get",
            url:"http://" + Config.ip_address + Config.port + "/test/status/getPlatformByJobID/",
            data:{job_id:job_id},
            dataType:"json",
            success:function(data){
                platform = data[0]["platform"]
                localStorage.setItem("platform",platform)
            }

        })
    });
}

let checkJobId = function() {
    let job_id = localStorage.getItem("jobId")
    if(job_id == ''){
        alert('please select job!')
    }
}

let setFunctionInterval = function(){
    conf_id = setInterval(getConfigure, 1000);
    run_test_name_id = setInterval(getRunningTestName, 1000);
    job_status_id = setInterval(getJobStatus, 1000);
    job_progress_id = setInterval(getJobProgress, 1000);
    job_execure_time_id = setInterval(getJobExecuteTime, 1000);
    check_jo_id_id = setInterval(checkJobId,6000);
}

let clearFunctionInterval = function(){
    clearInterval(conf_id);
    clearInterval(run_test_name_id);
    clearInterval(job_status_id);
    clearInterval(job_progress_id);
    clearInterval(get_test_log_id);
    clearInterval(job_execure_time_id);
    clearInterval(check_jo_id_id);
}

let getRunningJobList = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/jobRunningList/",
    {
    },function(data, status){
        data = data["data"]
        $("#dropdown-job-list").empty();
        let html = ""
        data.forEach((element) => {
            element = JSON.parse(element)
            html += '<li><a href="#">'+element["job_name"]+'('+element["_id"]+')</a></li>';
        });
        $("#dropdown-job-list").append(html);
        chooseJobId();
    });
}

let getJobExecuteTime = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/jobExecuteTime/",
    {
        job_id: localStorage.getItem("jobId")
    },function(data, status){
        data = data["time"]
        if ( job_status == "Active" ){
            hour = parseInt(data.split(':')[0])
            minute = parseInt(data.split(':')[1])
            second = parseInt( data.split(':')[2])
            $("#spend_time").text("Time spend: " + String(hour) + " h " + String(minute) + " m " + String(second) + " s");
        }
    });
}

let getConfigure = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/testConfigure/",
    {
        job_id: localStorage.getItem("jobId")
    },function(data, status){
        // console.log(data)
        $("#platform").text(data["job_platform"]);
        $("#model").text(data["job_model"]);
        $("#topo").text(data["job_topo"]);
    });
}

let getRunningTestName = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/currentRunningName/",
    {
        job_id: localStorage.getItem("jobId")
    },function(data, status){
        if ( data["name"] == "Finish"){
            location.href = "http://" + Config.ip_address + Config.port + "/test/jobManagement"
        }
        else {
            $("#test_name").text(data["name"])
        }
    });
}

let getJobStatus = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/jobStatus/",
    {
        job_id: localStorage.getItem("jobId")
    },function(data, status){
        job_status = data["job_status"]
        $("#current_status").text(job_status)
        if(data["status"] == "Finished")
        {
            $("#finish_button").removeClass("disabled");
        }
        else{
            getTestLog()
        }
    });
}

let getJobProgress = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/jobProgress/",
    {
        job_id: localStorage.getItem("jobId")
    },function(data, status){
        $("#jobProgress").css("width",data["progress"]+"%")
        $("#jobProgress").text(data["progress"].toFixed(2)+"%")
    });
}

let getTestLog = function(){
    $.get("http://"+ Config.ip_address + Config.port + "/test/status/nowTestLog/",
    {
        job_id: localStorage.getItem("jobId"),
        platform: localStorage.getItem("platform")
    },function(data, status){
        $("#test_name").text(data["test_name"]);
        $("#log").empty();
        let html = ""
        data = data["job_log"]
        for(var i = 0; i < data.length;i++)
        {
            html += "<div>" + data[i] +" "+ "</div>"
        }
        $("#log").append(html);
    });
}

let jumpJobDetail = async function(){
    location.href = "http://" + Config.ip_address + Config.port + '/test/jobDetail'
}

function real_Time_clicked(){
    document.getElementById("refresh").disabled = false;
    document.getElementById("real_time").disabled = true;
    setFunctionInterval();
}

function refresh_clicked(){
    document.getElementById("refresh").disabled = true;
    document.getElementById("real_time").disabled = false;
    clearFunctionInterval();
}

addLoadEvent(statusLoad);
