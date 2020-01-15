function addLoadEvent(func){
    var oldOnload = window.onload;
    if (typeof window.onload != "function"){
        window.onload = func ;
    }
    else{
        window.onload = function(){
            oldOnload();
            func();
        }
    }
}

let getCurrentPath=function(){
    var path = window.location.href ;
    updatePath(path);
}

let updatePath=function(path){
    $("#path").empty();/*清空path*/
    mainSort = "#"+path.split("/")[1];/*split將path分開，以/為分割點*/
    $(mainSort).children("ul").attr("style","display:block;")/*mainSort之下的children找到ul，新增他們的style*/
    $(mainSort).addClass("active");/*新增mainSort的Class active*/
    roadmap = path.split("/")
    let html = '<li class="breadcrumb-item"><a href="/">Home</a></li>';
    let link = '';
    if (roadmap[roadmap.length]){
        argument = roadmap.length - 1 ;
    }
    else{
        argument = roadmap.length - 2 ; 
    }
    for (let i=3 ; i<roadmap.length - 1 ; i++){
        if (roadmap[i] != ''){
            link += roadmap[i] ;
            substr = roadmap[i].substr(0,1);
            newsubstr = substr.toUpperCase();
            roadmap[i] = newsubstr+roadmap[i].substr(1);
            if (roadmap[i] == 'Sonic'){
                roadmap[i]='SONiC';
            }
            if (roadmap[i] == 'Test'){
                roadmap[i]='Network Test Center';
            }
            if (roadmap[i] == 'Tmsadmin'){
                roadmap[i] = 'TMS Admin';
            }
            if (roadmap[i] == 'Kb'){
                roadmap[i] = 'Knowledge Base';
            }
            if (roadmap[i] == 'Contact_us'){
                roadmap[i] = 'Contact Us';
            }
            if (roadmap[i] == 'LabInformation'){
                roadmap[i] = 'Lab Information';
            }
            if (roadmap[i] == 'Iot'){
                roadmap[i] = 'IoT';
            }
            if (roadmap[i] == "VOLT"){
                roadmap[i] = "vOLT"
            }
            if (roadmap[i] == "Dcsg"){
                roadmap[i] = "DCSG"
            }
            if (roadmap[i] == "Roadm"){
                roadmap[i] = "ROADM"
            }
            if (roadmap[i] == "Pm"){
                roadmap[i] = "Project Management"
            }
            // html += '<li class="breadcrumb-item"><a href=/'+link+'>'+roadmap[i]+'</a></li>';
            html += '<li class="breadcrumb-item"><a onclick=history.go(' + (i-argument) + ')>'+roadmap[i]+'</a></li>';
            if (roadmap[i+1] != ''){
                link += '/';
            }
        }
    }
    $("#path").append(html);/*append增加()內的內容*/
}

let goTop=function(){
    $('#gotop').click(function(){
        $('html,body').animate({ scrollTop: 0 }, 'slow');   /* 返回到最頂上 */
        return false;
    });    
    /* 偵測卷軸滑動時，往下滑超過400px就讓GoTop按鈕出現 */
    $(window).scroll(function() {
        if ( $(this).scrollTop() > 400){
            $('#gotop').fadeIn();
        } else {
            $('#gotop').fadeOut();
        }
    });
}

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};

addLoadEvent(getCurrentPath);
addLoadEvent(goTop);
addLoadEvent(getUrlParameter);