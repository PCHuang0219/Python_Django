let jenkins_jobs = []
let build_html = ''
let jenkins_html = ''

let getJenkinsJobs = async function(){
    await $.ajax({
        type: "get",
        url: window.location.origin + "/test/jenkins/getJobs/",
        data:{},
        dataType: "json",
        success: function(data, status){
            data = data["jobs"]
            jenkins_jobs = {"job_name":data}
            build_html = '<ul><li style="color: crimson">Jenkins<ul><li style="color:brown">broadcom<ul>'
            jenkins_html = '<ul><li style="color: crimson">Jenkins<ul><li style="color:brown">broadcom<ul>'
        },
    })
}

let showJenkins = function(){
    $("#imageCase").empty()
    $("#imageCase").append(build_html)
}

let showJenkinsJobs = function(){
    $("#jenkins").empty()
    $("#jenkins").append(jenkins_html)
}

let getJenkinsBuilds = async function(job_name){
    await $.ajax({
        type: "get",
        url: window.location.origin + "/test/jenkins/getBuilds/",
        data:{job_name:job_name},
        dataType: "json",
        success: function(data, status){
            data = data["builds"]
            addJobs(job_name)
            data.forEach(async function(element){
                job_name = element["job_name"]
                build_number = element["build_number"]
                result = element["result"]
                if (result == "SUCCESS"){
                    result = '<span style="color:green;">Success</span>'
                }
                else if (result == "FAILURE"){
                    result = '<span style="color:red;">Failed</span>'
                }
                else{result = '<span style="color:blue;">Running</span>'}
                value = job_name+'/'+build_number
                content = job_name+'  /  '+build_number+'  /  '+result
                addBuilds(value,content)
            })
            build_html += '</div></li>'
        },    
    })
    showJenkins();
    showJenkinsJobs();
}

let addJobs = function(job_name){
    build_html+= '<li style="color: black">'+job_name+'<div style="margin-left: 2em">'
    jenkins_html+= '<label style="color: black"><input name="jenkins_job_name" type="radio" value="'+job_name+'">'+job_name+'</label><br>'
}
let addBuilds = function(value,content){
    build_html += '<label style="color: blueviolet"><input name="select_image" type="radio" value="'+value+'">'+content+'</label><br>'
}

let submitJenkinsJob = function(){
    $("#buildJob").click(function(){
        var radios = document.getElementsByName('jenkins_job_name');
        for (var i = 0, length = radios.length; i < length; i++){
            if (radios[i].checked){
                job_name = radios[i].value
                }
        }        
        $.ajax({
            type: "get",
            url:window.location.origin + "/test/jenkins/buildjob/",
            data:{job_name:job_name},
            dataType: "json",
            success: function(data,status){
                location.href =window.location.origin + "/test/jenkinsViews" 
            }
        })
    })
}

let submitImageVersion = function(){
    var radios = document.getElementsByName('select_image');
    radios.forEach(function(element){
        if (element.checked){
            status = element.parentElement.textContent.split("/  ")[2]
            value = element.value
        }
    })
    if ( status != "Success"){
        alert("Only can select success build")
    }
    else{
        localStorage.setItem("change_page","1");
        if (getUrlParameter("test_plan_id")){
            url = "?test_plan_id=" + getUrlParameter("test_plan_id") + "&"
        }
        else{
            url = "?"
        }
        project = getUrlParameter("project")
        job_name = getUrlParameter("job_name")
        job_description = getUrlParameter("job_description")
        url += "job_name=" + job_name + "&job_description=" + job_description + "&image_path=" + value + "&project=" + project
        location.href = window.location.origin + "/test/" + url
    }
}

let windowsLoad = async function(){
    await getJenkinsJobs();
    await jenkins_jobs["job_name"].forEach(function(element){
        getJenkinsBuilds(element);
    })
    submitJenkinsJob()
}
addLoadEvent(windowsLoad)